from dotenv import load_dotenv
import os

# Load environment variables from a .env file (if it exists)
load_dotenv()

# --- FIX START ---
# Make sure to set your TAVILY_API_KEY either in a .env file
# or directly in the code like this:
os.environ["TAVILY_API_KEY"] = "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"
# Replace "YOUR_TAVILY_API_KEY" with your actual key.
# If you don't have one, you can get it from: https://tavily.com/

# Make sure to set your MISTRAL_API_KEY either in a .env file
# or directly in the code like this:
# os.environ["MISTRAL_API_KEY"] = "YOUR_MISTRAL_API_KEY"
# Replace "YOUR_MISTRAL_API_KEY" with your actual key.
# If you don't have one, you can get it from: https://mistral.ai/
# --- FIX END ---

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

search_tool=TavilySearchResults(max_results=5)
llm=ChatMistralAI(model="mistral-small-2506")
prompt=ChatPromptTemplate.from_template(
    """
you are a helpful assistant

summarize the following news into clear bullet points
"""

)

chain=prompt|llm|StrOutputParser()

news_reult=search_tool.run("latest AI news of 2026")


result=chain.invoke({"news":news_reult})
print(result)