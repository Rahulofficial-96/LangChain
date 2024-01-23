import os
from langchain_openai import OpenAI
openai_key='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'
os.environ["Open_api_key"]=openai_key

llm=OpenAI(openai_api_key=os.environ["Open_api_key"],temperature=0.6)

text = "What is capital of India?"
print(llm.predict(text))