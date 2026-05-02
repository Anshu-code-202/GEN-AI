from dotenv import load_dotenv
import os

load_dotenv()
from langchain_mistralai import ChatMistralAI

from langchain.tools import tool

from rich import print


@tool
def get_text_length(text:str)->int:
    """Return the number of characters in the input text"""
    return len(text)

llm=ChatMistralAI(model="mistral-small-2506")

#2 tool binding with llm
llm=llm.bind_tools([get_text_length])


result=llm.invoke("Return the number of characters in the input text:'hello'")

result2=llm.invoke_with_tools("Return the number of characters in the input text:'hello'")    

print(result)

print(f"\n \n \n {result2}")