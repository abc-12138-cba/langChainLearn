"""
  将大模型的自由文本输出转换为结构化JSON数据的工具
  JsonOutputParser 能够结合 Pydantic 模型进行数据验证，自动验证字段类型和内容（如字符串、数字、嵌套对象等）
"""
#%%
import os
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
    model="google_genai:gemini-2.5-flash-lite",
)

class Prime(BaseModel):
  prime: list[int] = Field(description="素数")
  count: list[int] = Field(description="小于该素数的素数个数")

json_parser = JsonOutputParser(pydantic_object=Prime)

messages = [
  {"role": "system", "content": json_parser.get_format_instructions()},
  {"role": "user", "content": "任意生成5个1000-100000之间素数，并标出小于该素数的素数个数"},
]
resp = llm.invoke(messages)
json_resp = json_parser.invoke(resp)
print(json_resp) # {'prime': [10007, 10009, 10037, 10039, 10061], 'count': [1229, 1230, 1236, 1237, 1240]}