"""
  RunnableParallel 同时运行多个可运行对象,并为每个对象提供相同的输入。
  对于同步执行,RunnableParallel 使用 ThreadPoolExecutor 来同时运行可运行对象。
  对于异步执行,RunnableParallel 使用 asyncio.gather 来同时运行可运行对象。
  在 LCEL 表达式中,字典会自动转换为 RunnableParallel
"""
#%%
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
  model="google_genai:gemini-2.5-flash-lite",
)

parser = StrOutputParser()

joke_chain = (
  PromptTemplate.from_template("讲一个关于{topic}的笑话") | llm | StrOutputParser()
)
poem_chain = (
  PromptTemplate.from_template("写一首关于{topic}的诗歌") | llm | StrOutputParser()
)

map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

resp = map_chain.invoke({"topic": "人工智能"})
print(resp) # {''joke': '好的，这是一个关于人工智能的笑话： xxxx', 'poem': '好的，这是一首关于人工智能的诗歌： xxxx'}
