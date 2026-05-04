from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()
model_id = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model=model_id)
texts =["Hello this is Anshu Arora",
        "I am a software engineer",
        "I love coding in Python"]
vectors = embeddings.embed_documents(texts)
print(vectors)  
