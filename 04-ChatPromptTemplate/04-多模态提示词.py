"""
  可以使用提示模板来格式化多模态输入，比如将图片链接作为输入
"""

#%% 
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
   model="google_genai:gemini-2.5-flash-lite",
)

template = ChatPromptTemplate(
  [
    {"role": "system", "content": "用中文简短描述图片内容"},
    {"role": "user", "content": [{"image_url": "{image_url}"}]},
  ]
)

prompt = template.format_messages(
  image_url="https://img2.baidu.com/it/u=2976763563,2523722948&fm=253&app=138&f=JPEG?w=800&h=1200"
)

resp = llm.invoke(prompt)
print(resp.content) # 这是一张边境牧羊犬的肖像照...