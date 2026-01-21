"""
  RunnableSequence 按顺序“链接”多个可运行对象，其中一个对象的输出作为下一个对象的输入。
  LCEL重载了 | 运算符，以便从两个 Runnables 创建 RunnableSequence

  chain = runnable1 | runnable2
  # 等同于
  chain = RunnableSequence([runnable1, runnable2])
"""
#%%
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
    model="google_genai:gemini-2.5-flash-lite",
)

prompt_template = PromptTemplate(
  template="讲一个关于{topic}的笑话",
  input_variables=["topic"],
)
parser = StrOutputParser()

chain = prompt_template | llm | parser

resp = chain.invoke({"topic": "人工智能"})
print(resp) # 直接输出笑话内容(好的，这是一个关于人工智能的笑话： xxxx)
