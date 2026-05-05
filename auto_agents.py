# =========================
# STEP 1: Load Environment Variables & Libraries
# =========================
from dotenv import load_dotenv
# load_dotenv() 
#  # Loads variables from .env file
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

import os  
import requests  # Used to make API calls
from rich import print  # Better formatted printing

# LangChain & Tooling imports
from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

# Tavily for real-time news search
from tavily import TavilyClient
from langchain.agents import create_agent
# from langchain.agents import initialize_agent, AgentType

# =========================
# TOOL 1: WEATHER TOOL
# =========================
@tool
def get_weather(city: str) -> str:
    """
    Use this tool to get the CURRENT weather of any city using API.
    """
    
    # Get API key from environment
    api_key = os.getenv("OPENWEATHER_API_KEY")

    # API endpoint (restricted to India cities using ',IN')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"
    
    # # Make API request (with timeout to avoid hanging)
    response = requests.get(url, timeout=5)
    data = response.json()

    # Debugging: print full API response
    # print("DEBUG:", data)

    # Error handling
    if data.get("cod") != 200:
        return f"Error: {data.get('message', 'could not fetch weather')}"
    
    # Extract useful information
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    # Return formatted result
    return f"Weather in {city}: {desc}, {temp}°C"


# =========================
# TOOL 2: NEWS TOOL
# =========================
@tool
def get_news(city: str) -> str:
    """
    Use this tool to get LATEST news of any city using API """
    
    # Initialize Tavily client
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    # Perform search query
    response = tavily_client.search(
        query=f"latest news in {city}",
        search_depth="basic",  # balanced speed + accuracy
        max_results=3
    )

    # Extract results list
    results = response.get("results", [])

    # Handle no results case
    if not results:
        return f"No news found for {city}"

    news_list = []

    # Format each news result
    for r in results:
        title = r.get("title", "No title")
        url = r.get("url", "")
        snippet = r.get("content", "")

        news_list.append(
            f"- {title}\n  {url}\n  {snippet[:100]}...."
        )

    return f"Latest news in {city}:\n\n" + "\n\n".join(news_list)


# Test call (can be removed in production)
# print(get_news.invoke("Sirsa"))


# =========================
# STEP 2: Initialize LLM
# =========================
llm = ChatMistralAI(
    model="mistral-tiny",
    api_key=os.getenv("MISTRAL_API_KEY")
)

agent = create_agent(
    llm,
    tools=[get_weather,get_news],
    system_prompt="You are helpful city assistant"

)
print("City Agent : type exit to quit")

while True:
    user_input=input("you: ")
    if user_input.lower() == "exit":
        break

    result=agent.invoke(
        {
            "messages":[{"role":"user","content":user_input}]
        }
    )
    print("bot:" ,result['messages'][-1].content)
