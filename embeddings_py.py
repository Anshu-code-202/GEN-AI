from langchain_openai import OpenAIEmbeddings 
import os

from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise RuntimeError("OPENAI_API_KEY not set. Export it before running this script.") 
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=openai_api_key)
texts =["Hello this is Anshu Arora",
        "I am a software engineer",
        "I love coding in Python"]

vectors = embeddings.embed_documents(texts)
print(vectors)