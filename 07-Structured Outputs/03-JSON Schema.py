"""
  若需最大程度的控制或互操作性，可以提供一个原始的 JSON Schema。详情可参考 https://platform.openai.com/docs/guides/structured-outputs/json-schema#supported-schemas。
  可以将原始响应与解析后的表示一起返回，可在调用 with_structured_output 时设置 include_raw=True 来实现。
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

schema = {
    "name": "animal_list",
    "schema": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "animal": {
                    "type": "string",
                    "description": "动物名称"
                },
                "emoji": {
                    "type": "string",
                    "description": "动物的emoji表情"
                },
            },
            "required": ["animal", "emoji"],
        },
    },
}

messages = [{"role": "user", "content": "任意生成三种动物，以及他们的 emoji 表情"}]

llm_with_structured_output = llm.with_structured_output(
  schema, method="json_schema", include_raw=True
)
resp = llm_with_structured_output.invoke(messages)
print(11, resp) # {'raw':, 'parsed':, parsing_error: None} 
print(22, resp["raw"]) # 原始的：AIMessage(content=,)
print(33, resp["parsed"]) # [{'animal': 'Lion', 'emoji': '🦁'}, {'animal': 'Dog', 'emoji': '🐶'}, {'animal': 'Cat', 'emoji': '🐱'}]
