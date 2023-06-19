import os
from dotenv import load_dotenv
from llama_index import (SimpleDirectoryReader,
                         GithubRepositoryReader,
                         PromptHelper,
                         GPTVectorStoreIndex,
                         ServiceContext,
                         StorageContext,
                         load_index_from_storage)
from langchain.chat_models import ChatOpenAI
from llama_index.llm_predictor.chatgpt import ChatGPTLLMPredictor
from base_prompt import CHAT_REFINE_PROMPT, CHAT_QA_PROMPT

load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
GITHUB_API_KEY = os.environ["GITHUB_API_KEY"]

# define prompt helper
# set maximum input size
max_input_size = 4096
# set number of output tokens
num_output = 1000
# set maximum chunk overlap
max_chunk_overlap = 20
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)
# define LLM
llm_predictor = ChatGPTLLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-0613", streaming=False, max_tokens=num_output))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)


# builds new index from our data folder and GitHub repos
def build_index():
    global service_context

    combined_documents = []
    # load directory documents
    directory_document = SimpleDirectoryReader('./data', recursive=True).load_data()
    combined_documents += directory_document
    # load github documents
    github_token = GITHUB_API_KEY
    owner = "pyth-network"
    repos = ["pyth-client-py", "pyth-client-js", "pyth-client-rs", "pyth-sdk-solidity", "pyth-sdk-rs", "pyth-gitbook", "pyth-crosschain"]
    branch = "main"
    # build documents out of all repos
    for repo in repos:
        document = GithubRepositoryReader(github_token=github_token, owner=owner, repo=repo, use_parser=False, verbose=False).load_data(branch=branch)
        combined_documents += document
    # build index
    index = GPTVectorStoreIndex.from_documents(combined_documents, service_context=service_context)
    # store index in ./storage
    index.storage_context.persist()


# used to add documents to existing stored index
def add_to_index():
    github_token = GITHUB_API_KEY
    owner = "pyth-network"
    repos = ["pyth-serum", "publisher-utils", "solmeet-workshop-june-22", "oracle-sandbox", "pyth-sdk-js",
             "program-authority-escrow", "pyth-observer", "audit-reports", "example-publisher", "pyth-agent",
             "program-admin", "pyth-client", "pythnet", "governance"]
    branch = "main"

    combined_documents = []
    for repo in repos:
        if repo == "governance":
            document = GithubRepositoryReader(github_token=github_token, owner=owner, repo=repo, use_parser=False, verbose=False).load_data(branch="master")
        elif repo == "pythnet":
            document = GithubRepositoryReader(github_token=github_token, owner=owner, repo=repo, use_parser=False, verbose=False).load_data(branch="pyth")
        else:
            document = GithubRepositoryReader(github_token=github_token, owner=owner, repo=repo, use_parser=False, verbose=False).load_data(branch=branch)
        combined_documents += document

    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
    for doc in combined_documents:
        index.insert(doc)
    index.storage_context.persist()


def pyth_gpt(message):
    global service_context

    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)
    # query the index
    query_engine = index.as_query_engine(text_qa_template=CHAT_QA_PROMPT,
                                         refine_template=CHAT_REFINE_PROMPT,
                                         similarity_top_k=3,
                                         streaming=False,
                                         service_context=service_context)
    # enter your prompt
    response = query_engine.query(message)
    return str(response)
