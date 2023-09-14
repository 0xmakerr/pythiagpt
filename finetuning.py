import os
import openai
import logging
import sys
import random
from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader, ServiceContext, download_loader
from llama_index.llms import OpenAI
from llama_index.evaluation import DatasetGenerator
from llama_hub.github_repo import GithubRepositoryReader, GithubClient
from llama_index.callbacks import OpenAIFineTuningHandler
from llama_index.callbacks import CallbackManager
from llama_index import VectorStoreIndex, load_index_from_storage, StorageContext
from llama_index.finetuning import OpenAIFinetuneEngine
from llama_index.indices.postprocessor import SentenceTransformerRerank
from base_prompt import CHAT_TEXT_QA_PROMPT, CHAT_REFINE_PROMPT
from llama_index.query_engine.router_query_engine import RouterQueryEngine
from llama_index.selectors.pydantic_selectors import PydanticSingleSelector
from llama_index.tools.query_engine import QueryEngineTool
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, faithfulness
import json
from collections import defaultdict

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().handlers = []
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
GITHUB_API_KEY = os.environ["GITHUB_API_KEY"]


def load_general_documents():
    general_documents = []
    directory_document = SimpleDirectoryReader('./data', recursive=True).load_data()
    general_documents += directory_document

    download_loader("GithubRepositoryReader")
    github_client = GithubClient(GITHUB_API_KEY)
    owner = "pyth-network"
    repo = "documentation"
    branch = "main"

    loader = GithubRepositoryReader(github_client, owner=owner, repo=repo, filter_directories=(
                                    ["images"], GithubRepositoryReader.FilterType.EXCLUDE), verbose=False,
                                    concurrent_requests=10, )
    document = loader.load_data(branch=branch)
    general_documents += document
    return general_documents


def load_code_documents():
    code_documents = []
    # load github documents
    download_loader("GithubRepositoryReader")
    github_client = GithubClient(GITHUB_API_KEY)
    owner = "pyth-network"
    repos = ["pyth-client-py", "pyth-client-js", "pyth-sdk-solidity", "pyth-sdk-rs", "pyth-crosschain"]
    branch = "main"
    # build documents out of all repos
    for repo in repos:
        loader = GithubRepositoryReader(github_client, owner=owner, repo=repo, filter_directories=(
        ["images"], GithubRepositoryReader.FilterType.EXCLUDE), verbose=False, concurrent_requests=10, )
        document = loader.load_data(branch=branch)
        code_documents += document
    return code_documents


def question_generation():
    general_documents = load_general_documents()
    random.seed(42)
    random.shuffle(general_documents)

    gpt_35_context = ServiceContext.from_defaults(
        llm=OpenAI(model="gpt-3.5-turbo", temperature=0.3)
    )

    question_gen_query = (
        "You are a Teacher/ Professor. Your task is to setup "
        "a quiz/examination. Using the provided context, formulate "
        "a single question that captures an important fact from the "
        "context. Restrict the question to the context information provided."
    )

    dataset_generator = DatasetGenerator.from_documents(
        general_documents[50:],
        question_gen_query=question_gen_query,
        service_context=gpt_35_context,
    )

    questions = dataset_generator.generate_questions_from_nodes(num=40)
    print("Generated ", len(questions), " questions")

    with open("train_questions.txt", "w") as f:
        for question in questions:
            f.write(question + "\n")


def fine_tune():
    finetuning_handler = OpenAIFineTuningHandler()
    callback_manager = CallbackManager([finetuning_handler])

    service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-4", temperature=0.3, max_tokens=1000), context_window=2048,  # limit the context window artifically to test refine process
        callback_manager=callback_manager, embed_model="local")

    questions = []
    with open("train_questions.txt", "r") as f:
        for line in f:
            questions.append(line.strip())

    # rebuild storage context
    general_storage_context = StorageContext.from_defaults(persist_dir="./storage/general_index")
    code_storage_context = StorageContext.from_defaults(persist_dir="./storage/code_index")
    # load index
    general_index = load_index_from_storage(general_storage_context, service_context=service_context)
    code_index = load_index_from_storage(code_storage_context, service_context=service_context)

    rerank = SentenceTransformerRerank(model="cross-encoder/ms-marco-MiniLM-L-2-v2", top_n=3)
    # query the index
    general_query_engine = general_index.as_query_engine(text_qa_template=CHAT_TEXT_QA_PROMPT, refine_template=CHAT_REFINE_PROMPT, similarity_top_k=10, streaming=False, service_context=service_context, node_postprocessors=[
        rerank])

    code_query_engine = code_index.as_query_engine(text_qa_template=CHAT_TEXT_QA_PROMPT, refine_template=CHAT_REFINE_PROMPT, similarity_top_k=10, streaming=False, service_context=service_context, node_postprocessors=[
        rerank])

    general_vector_tool = QueryEngineTool.from_defaults(query_engine=general_query_engine, description="Useful for retrieving general context related to the data source", )
    code_vector_tool = QueryEngineTool.from_defaults(query_engine=code_query_engine, description="Useful specifically for coding questions related to the data source ", )

    query_engine = RouterQueryEngine(selector=PydanticSingleSelector.from_defaults(), query_engine_tools=[
        general_vector_tool, code_vector_tool])
    # enter your prompt
    for question in questions:
        response = query_engine.query(question)
    finetuning_handler.save_finetuning_events("finetuning_events.jsonl")
    finetune_engine = OpenAIFinetuneEngine("gpt-3.5-turbo", "finetuning_events.jsonl",)
    finetune_engine.finetune()
    finetune_engine.get_current_job()
    ft_llm = finetune_engine.get_finetuned_model(temperature=0.3)


def evaluate_llm():
    questions = []
    with open("train_questions.txt", "r") as f:
        for line in f:
            questions.append(line.strip())
    service_context = ServiceContext.from_defaults(llm=OpenAI(model="ft:gpt-3.5-turbo-0613:pyth-network::7xwcT6yU", temperature=0.3, max_tokens=1000), context_window=2048, embed_model="local")
    # rebuild storage context
    general_storage_context = StorageContext.from_defaults(persist_dir="./storage/general_index")
    code_storage_context = StorageContext.from_defaults(persist_dir="./storage/code_index")
    # load index
    general_index = load_index_from_storage(general_storage_context, service_context=service_context)
    code_index = load_index_from_storage(code_storage_context, service_context=service_context)

    rerank = SentenceTransformerRerank(model="cross-encoder/ms-marco-MiniLM-L-2-v2", top_n=3)
    # query the index
    general_query_engine = general_index.as_query_engine(text_qa_template=CHAT_TEXT_QA_PROMPT, refine_template=CHAT_REFINE_PROMPT, similarity_top_k=10, streaming=False, service_context=service_context, node_postprocessors=[
        rerank])

    code_query_engine = code_index.as_query_engine(text_qa_template=CHAT_TEXT_QA_PROMPT, refine_template=CHAT_REFINE_PROMPT, similarity_top_k=10, streaming=False, service_context=service_context, node_postprocessors=[
        rerank])

    general_vector_tool = QueryEngineTool.from_defaults(query_engine=general_query_engine, description="Useful for retrieving general context related to the data source", )
    code_vector_tool = QueryEngineTool.from_defaults(query_engine=code_query_engine, description="Useful specifically for coding questions related to the data source ", )

    query_engine = RouterQueryEngine(selector=PydanticSingleSelector.from_defaults(), query_engine_tools=[
        general_vector_tool, code_vector_tool])

    contexts = []
    answers = []

    for question in questions:
        response = query_engine.query(question)
        contexts.append([x.node.get_content() for x in response.source_nodes])
        answers.append(str(response))

    ds = Dataset.from_dict({
        "question": questions,
        "answer": answers,
        "contexts": contexts,
    })

    result = evaluate(ds, [answer_relevancy, faithfulness])
    print(result)


def format_validation():
    # Load the dataset
    with open("finetuning_events.jsonl", 'r', encoding='utf-8') as f:
        dataset = [json.loads(line) for line in f]

    # Initial dataset stats
    print("Num examples:", len(dataset))
    print("First example:")
    for message in dataset[0]["messages"]:
        print(message)

    # Format error checks
    format_errors = defaultdict(int)

    for ex in dataset:
        if not isinstance(ex, dict):
            format_errors["data_type"] += 1
            continue

        messages = ex.get("messages", None)
        if not messages:
            format_errors["missing_messages_list"] += 1
            continue

        for message in messages:
            if "role" not in message or "content" not in message:
                format_errors["message_missing_key"] += 1

            if any(k not in ("role", "content", "name") for k in message):
                format_errors["message_unrecognized_key"] += 1

            if message.get("role", None) not in ("system", "user", "assistant"):
                format_errors["unrecognized_role"] += 1

            content = message.get("content", None)
            if not content or not isinstance(content, str):
                format_errors["missing_content"] += 1

        if not any(message.get("role", None) == "assistant" for message in messages):
            format_errors["example_missing_assistant_message"] += 1

    if format_errors:
        print("Found errors:")
        for k, v in format_errors.items():
            print(f"{k}: {v}")
    else:
        print("No errors found")
