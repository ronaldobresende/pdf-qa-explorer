from langchain_community.llms import HuggingFaceEndpoint

def create_llm(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", temperature=0.1, max_new_tokens=1024):
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        temperature=temperature,
        max_new_tokens=max_new_tokens
    )
    return llm