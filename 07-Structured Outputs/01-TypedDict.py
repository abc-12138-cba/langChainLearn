"""
  要求模型按照给定的模式格式提供其响应，这有助于确保输出可以被轻松解析并在后续处理中使用。LangChain 支持多种模式类型和强制结构化输出的方法

  TypedDict 提供了一个使用 Python 内置类型的简单方案，但是没有验证功能
"""

#%%
import os
from typing import TypedDict, Annotated
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
    model="google_genai:gemini-2.5-flash-lite",
)
class Animal(TypedDict):
  animal: Annotated[str, "动物"]
  emoji: Annotated[str, "表情"]

class AnimalList(TypedDict):
  animals: Annotated[list[Animal], "动物与表情列表"]

messages = [{"role": "user", "content": "任意生成三种动物，以及他们的 emoji 表情"}]

llm_with_structured_output = llm.with_structured_output(AnimalList)
resp = llm_with_structured_output.invoke(messages)
print(resp) # {'animals': [{'animal': 'Dog', 'emoji': '🐶'}, {'animal': 'Cat', 'emoji': '🐱'}, {'animal': 'Rabbit', 'emoji': '🐰'}]}