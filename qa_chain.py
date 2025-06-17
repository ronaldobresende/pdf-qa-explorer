from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def get_qa_chain(llm, retriever):
    prompt_template = """
    Use estritamente os trechos de contexto a seguir para responder à pergunta no final.
    Se a resposta não estiver no contexto, diga "Com base nos documentos, não encontrei a resposta.". Não tente inventar uma resposta.
    Responda de forma clara e em português.

    Contexto:
    {context}

    Pergunta: {question}

    Resposta completa e detalhada em português, listando todos os itens encontrados no contexto:"""
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )