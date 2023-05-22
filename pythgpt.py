import os
from base_prompt import base_prompt
from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex, ServiceContext
from llama_index import StorageContext, load_index_from_storage
from llama_index.prompts.prompts import QuestionAnswerPrompt, RefinePrompt
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (AIMessagePromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)
from llama_index.llm_predictor.chatgpt import ChatGPTLLMPredictor

os.environ["OPENAI_API_KEY"] = 'YOUR OPENAI TOKEN'


# builds new index from our data folder
def build_index():
    # load documents
    documents = SimpleDirectoryReader('data').load_data()
    # define LLM
    llm_predictor = ChatGPTLLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=False, max_tokens=256))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    # build index
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
    # store index in ./storage
    index.storage_context.persist()


def pyth_gpt(message):
    # define LLM
    llm_predictor = ChatGPTLLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=False, max_tokens=256))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)
    # system prompt
    system_prompt = SystemMessagePromptTemplate.from_template(base_prompt)

    chat_refine_prompt_tmpl_msgs = [system_prompt, HumanMessagePromptTemplate.from_template("{query_str}"),
        AIMessagePromptTemplate.from_template("{existing_answer}"),
        HumanMessagePromptTemplate.from_template("We have the opportunity to refine the above answer "
                                                 "(only if needed) with some more context below.\n"
                                                 "------------\n"
                                                 "{context_msg}\n"
                                                 "------------\n"
                                                 "Given the new context, refine the original answer to better "
                                                 "answer the question. "
                                                 "If the context isn't useful, output the original answer again.", ), ]

    chat_refine_prompt_lc = ChatPromptTemplate.from_messages(chat_refine_prompt_tmpl_msgs)
    chat_refine_prompt = RefinePrompt.from_langchain_prompt(chat_refine_prompt_lc)

    chat_qa_prompt_tmpl_msgs = [system_prompt,
        HumanMessagePromptTemplate.from_template("Context information is below. \n"
                                                 "---------------------\n"
                                                 "{context_str}"
                                                 "\n---------------------\n"
                                                 "Given the context information and not prior knowledge, "
                                                 "answer the question: {query_str}\n")]
    chat_qa_prompt_lc = ChatPromptTemplate.from_messages(chat_qa_prompt_tmpl_msgs)
    chat_qa_prompt = QuestionAnswerPrompt.from_langchain_prompt(chat_qa_prompt_lc)
    # query the index
    query_engine = index.as_query_engine(text_qa_template=chat_qa_prompt,
                                         refine_template=chat_refine_prompt,
                                         similarity_top_k=3,
                                         streaming=False,
                                         )
    # enter your prompt
    response = query_engine.query(message)
    return response
