# from langchain_community.llms import openai
import os
from langchain_openai import ChatOpenAI
# from langchain.llms.openai import OpenAIChat

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
llm = ChatOpenAI(api_key=OPENAI_API_KEY)
# llm = OpenAI(api_key=OPENAI_API_KEY)

# question = 'Are you hear me?'
question = 'LangChain 과 OpenAI API Key 를 사용하여 요청했어!\n잘 전달 되었어?'
# question = '혹시 LangChain 의 FakeListLLM 이라는 모듈을 알아? 모르면, 모른다고 말해줘'

response = llm.invoke(question)

print('response: ', response)
# print('response.content: ', response.content)
