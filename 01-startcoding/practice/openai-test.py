from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain_experimental.tools import PythonREPLTool
llm = ChatOpenAI()
tools = PythonREPLTool(),
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# result = agent.invoke("What are the prime numbers until 20?")
result = agent.invoke("Who are you?")
print(result)