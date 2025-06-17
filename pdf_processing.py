from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_pdf(pdf_bytes, chunk_size=800, chunk_overlap=150):
    """
    Carrega um PDF dos bytes e divide em pedaços menores.
    Retorna uma lista de documentos.
    """
    with open("temp_cached.pdf", "wb") as f:
        f.write(pdf_bytes)

    loader = PyPDFLoader("temp_cached.pdf")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    docs = text_splitter.split_documents(documents)
    return docs