"""
  StrOutputParser 是一个简单的解析器，从结果中提取 content 字段
"""
#%%
import os
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
    model="google_genai:gemini-2.5-flash-lite",
)

messages = [
  {"role": "system", "content": "你是一个机器人"},
  {"role": "user", "content": "你好"},
]

resp = llm.invoke(messages)
print(resp) # content='你好！有什么我可以帮忙的吗？' additional_kwargs=...

str_resp = StrOutputParser().invoke(resp)
print(str_resp) # 你好！有什么我可以帮忙的吗