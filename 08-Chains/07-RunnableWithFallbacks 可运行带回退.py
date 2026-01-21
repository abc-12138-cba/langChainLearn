"""
  RunnableWithFallbacks 使得 Runnable 失败后可以回退到其他 Runnable。可以直接在Runnable 上使用 with_fallbacks 方法
"""
#%%
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_core.runnables import RunnableLambda
load_dotenv(find_dotenv())

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
    model="google_genai:gemini-2.5-flash-lite",
)

chain = PromptTemplate.from_template("hello") | llm

chain_with_fallback = chain.with_fallbacks([RunnableLambda(lambda x: "sorry")])

result = chain_with_fallback.invoke("1") # 提示词模板中没有需要填充的变量，会报错
print(result) # sorry
