from langchain.retrievers.multi_query import MultiQueryRetriever

def create_multi_query_retriever(vector_store, llm, k=5):
    base_retriever = vector_store.as_retriever(search_kwargs={"k": k})
    multi_query_retriever = MultiQueryRetriever.from_llm(retriever=base_retriever, llm=llm)
    return multi_query_retriever