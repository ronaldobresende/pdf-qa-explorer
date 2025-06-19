import os
from langchain_community.llms import HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI

def create_huggingface_llm(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", temperature=0.1, max_new_tokens=1024):
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        temperature=temperature,
        max_new_tokens=max_new_tokens
    )
    return llm

def create_llm(google_api_key=os.environ["GEMINI_API_KEY"], model="gemini-2.5-flash", temperature=0.1, max_output_tokens=1024):
    llm = ChatGoogleGenerativeAI(
        model=model,
        google_api_key=google_api_key,
        temperature=temperature,
        max_output_tokens=max_output_tokens
    )
    return llm