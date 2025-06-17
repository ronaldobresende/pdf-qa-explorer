import streamlit as st
import time
from pdf_processing import load_and_split_pdf
from vector_store import create_vector_store
from llm_setup import create_llm
from retriever_setup import create_multi_query_retriever
from qa_chain import get_qa_chain

st.set_page_config(page_title="Assistente de Estudos FocoTotal", layout="wide")

@st.cache_resource(show_spinner=False)
def process_pdf_and_create_retriever(pdf_bytes):
    # Processa o PDF e retorna retriever e llm, cacheando pelo conteúdo do arquivo
    progress_bar = st.progress(0, text="Iniciando o processamento do documento...")

    progress_bar.progress(10, text="Carregando e dividindo PDF...")
    docs = load_and_split_pdf(pdf_bytes)
    time.sleep(0.5)

    progress_bar.progress(30, text="Criando banco vetorial...")
    db = create_vector_store(docs)
    time.sleep(0.5)

    progress_bar.progress(50, text="Carregando modelo LLM...")
    llm = create_llm()
    time.sleep(0.5)

    progress_bar.progress(70, text="Configurando retriever inteligente...")
    retriever = create_multi_query_retriever(db, llm)
    time.sleep(0.5)

    progress_bar.progress(100, text="Pronto para perguntas!")
    time.sleep(1)
    progress_bar.empty()

    return retriever, llm

st.title("📚 Assistente de Estudos FocoTotal")
st.write("Faça o upload do seu material em PDF e tire suas dúvidas!")

uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

if uploaded_file is not None:
    pdf_bytes = uploaded_file.getvalue()
    retriever, llm = process_pdf_and_create_retriever(pdf_bytes)
    st.session_state.retriever = retriever
    st.session_state.llm = llm
    st.session_state.qa_chain_ready = True
    if 'processed_once' not in st.session_state:
        st.success(f"Documento '{uploaded_file.name}' processado com sucesso! Pronto para suas perguntas.")
        st.session_state.processed_once = True

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and "sources" in message:
            with st.expander("Fontes no Documento"):
                for doc in message["sources"]:
                    st.info(f"**Página {doc.metadata.get('page', 'N/A')}:**\n{doc.page_content[:300]}...")

if 'qa_chain_ready' in st.session_state and st.session_state.qa_chain_ready:
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = get_qa_chain(st.session_state.llm, st.session_state.retriever)

    if query := st.chat_input("Digite sua pergunta sobre o documento..."):
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                result = st.session_state.qa_chain.invoke({"query": query})
                response = result["result"]
                sources = result["source_documents"]
                st.markdown(response)
                if "não encontrei a resposta" not in response:
                    with st.expander("Fontes no Documento"):
                        for doc in sources:
                            st.info(f"**Página {doc.metadata.get('page', 'N/A')}:**\n{doc.page_content[:300]}...")
        st.session_state.messages.append({"role": "assistant", "content": response, "sources": sources})

#streamlit run app.py
#Explique o que é a variável TCB e seus agrupamentos?         