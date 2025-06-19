# PDF-QA Explorer

O **PDF-QA Explorer** é uma aplicação web desenvolvida em Python com Streamlit que permite ao usuário fazer upload de arquivos PDF e interagir com o conteúdo por meio de perguntas em linguagem natural. Utilizando inteligência artificial, o sistema responde às dúvidas do usuário com base no material enviado, citando as fontes do próprio documento.

## Funcionalidades

- Upload de arquivos PDF
- Processamento automático do conteúdo em blocos inteligentes
- Busca semântica e respostas detalhadas com IA
- Citação das fontes do documento nas respostas
- Interface de chat simples e intuitiva

## Arquitetura do Aplicativo

A arquitetura do PDF-QA Explorer é composta pelos seguintes componentes principais:

- **Streamlit**: Responsável pela interface web, permitindo o upload de arquivos PDF, entrada de perguntas e exibição das respostas.
- **LangChain**: Biblioteca que integra o modelo de linguagem (LLM) ao fluxo de perguntas e respostas, gerenciando a extração de texto do PDF, a criação de retrievers (buscadores de contexto) e a orquestração das respostas.
- **Google Gemini (LLM)**: Modelo de linguagem de grande porte utilizado para interpretar perguntas e gerar respostas baseadas no conteúdo do PDF, acessado via API do Google.
- **FAISS**: Utilizado para indexação e busca vetorial eficiente dos blocos de texto extraídos do PDF.
- **Sentence Transformers**: Responsável pela geração de embeddings semânticos dos textos, facilitando a busca contextualizada das informações.

### Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)


## Instalação

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/study-assistant.git
   cd study-assistant
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   ```sh
   python -m venv study_env
   # No Windows:
   study_env\Scripts\activate
   # No Linux/Mac:
   source study_env/bin/activate
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Obtenha uma chave de API do Gemini (Google):**
   - Acesse [Google AI Studio](https://aistudio.google.com/app/apikey) e gere sua chave de API.

5. **Configure a chave de API do Gemini:**
   - Crie um arquivo `.env` na raiz do projeto com o conteúdo:
     ```
     GEMINI_API_KEY=sua_chave_aqui
     ```
   - Ou defina a variável de ambiente no terminal antes de rodar o app:
     ```sh
     set GEMINI_API_KEY=sua_chave_aqui

## Como Rodar

Execute o comando abaixo na raiz do projeto:

```sh
streamlit run app.py
```

Acesse o endereço exibido no terminal (geralmente http://localhost:8501) para utilizar a aplicação.

## Estrutura dos Arquivos

- `app.py` — Interface principal Streamlit e orquestração
- `pdf_processing.py` — Processamento e divisão do PDF em blocos
- `vector_store.py` — Criação do banco vetorial (FAISS)
- `llm_setup.py` — Configuração do modelo de linguagem (LLM)
- `retriever_setup.py` — Configuração do retriever inteligente
- `qa_chain.py` — Cadeia de perguntas e respostas (QA Chain)
- `requirements.txt` — Lista de dependências do projeto

## Como Usar

1. Faça upload de um arquivo PDF usando a interface.
2. Aguarde o processamento do documento.
3. Digite sua pergunta sobre o conteúdo do PDF no chat.
4. Receba respostas detalhadas e, quando aplicável, veja as fontes extraídas do próprio documento.

## Observações

- O processamento do PDF pode demorar alguns segundos, dependendo do tamanho do arquivo e da performance do seu computador.
- O modelo de linguagem utilizado roda na nuvem (HuggingFace Inference Endpoint). Certifique-se de ter conexão com a internet.
- Para uso em produção, recomenda-se proteger a aplicação e configurar variáveis de ambiente sensíveis.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por Ronaldo Barbosa Resende.