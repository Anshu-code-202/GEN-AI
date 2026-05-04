import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from rich import print

from langchain_core.messages import HumanMessage

load_dotenv()


print("8k4uOxpgMPiq0Xz8ArJgVZx5Jx1FXDRC:", os.getenv("MISTRAL_API_KEY"))  # debug
#1 creating a tool 

@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)

tools = {
    "get_text_length" : get_text_length
}
llm = ChatMistralAI(model = "mistral-small-2506")

#tool binding 
llm_with_tool = llm.bind_tools([get_text_length])

#storing data
message = [] #maintains history
prompt = input("You: ")
query = HumanMessage(prompt)
message.append(query)

result=llm_with_tool.invoke(message)
message.append(result)
print(message)

if result.tool_calls:
    print(result.tool_calls[0])
    tool_name=result.tool_calls[0]["name"]
    tool_msg=tools[tool_name].invoke(result.tool_calls[0])
    message.append(tool_msg)
    print(message)


result=llm_with_tool.invoke(message)
print(result.content)

# #llm decides tools
# result = llm_with_tool.invoke("use the get_text_length tool to find the length of :hello")

# # message.append(result)


# #execute tool
# if result.tool_calls:
#     tool_call = result.tool_calls[0]
#     tool_result=get_text_length.invoke(["args"])
# #send back to llm
#     final_response = llm_with_tool.invoke(
#         f"the length of text is {tool_result}"
#         )
#     print(final_response)