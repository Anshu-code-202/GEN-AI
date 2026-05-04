from langchain.tools import tool
@tool
def get_greeting(name:str)->str:
     #type hints
    """Generate a greeting messages for a user""" #docstring
    return f"Hello {name},Welcome to Ai ERA"

result=get_greeting.invoke({"name":"Arora"})
print(result)

print(get_greeting.description)