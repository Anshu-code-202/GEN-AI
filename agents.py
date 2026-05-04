#first step -loading all libraries
from dotenv import load_dotenv
load_dotenv()
import os  
import requests #reading url online

from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tools
from langchain_core import messages,HumanMessages,ToolMessages
from tavily import TavilyClient

#NOw lets create some tools

#weather tool
@tool
def get_weather(city:str)->str:
    """Get current weather update of city"""
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    response=requests.gte(url)
    data=response.json()

    print("DEBUG:" , data)

    if str(data.get("cod"))!=200:
        return f"Error: {data.get ('message','could not fetch weather')}"