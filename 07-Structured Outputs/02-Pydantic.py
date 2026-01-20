"""
  Pydantic 模型提供了丰富的功能集，包括字段验证、描述和嵌套结构
"""

#%%
import os
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
    model="google_genai:gemini-2.5-flash-lite",
)
class Animal(BaseModel):
  animal: str = Field(description="动物")
  emoji: str = Field(description="表情")

class AnimalList(BaseModel):
  animals: list[Animal] = Field(description="动物与表情列表")

messages = [{"role": "user", "content": "任意生成三种动物，以及他们的 emoji 表情"}]

llm_with_structured_output = llm.with_structured_output(AnimalList)
resp = llm_with_structured_output.invoke(messages)
print(resp) # animals=[Animal(animal='猫', emoji='😺'), Animal(animal='狗', emoji='🐶'), Animal(animal='兔子', emoji='🐰')]