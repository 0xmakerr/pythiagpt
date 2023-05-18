import os
from llama_index import SimpleDirectoryReader
from llama_index import LLMPredictor, GPTVectorStoreIndex, ServiceContext
from llama_index import StorageContext, load_index_from_storage
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = 'YOUR OPENAI TOKEN'


# builds new index from our data folder
def build_index():
    # load documents
    documents = SimpleDirectoryReader('data').load_data()
    # define LLM
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=False, max_tokens=256))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    # build index
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
    # store index in ./storage
    index.storage_context.persist()


def pyth_gpt(message):
    # define LLM
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=False, max_tokens=256))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)
    # query the index
    query_engine = index.as_query_engine(
        service_context=service_context,
        similarity_top_k=3,
        streaming=False,
    )
    response = query_engine.query(f"{message}")
    return response
