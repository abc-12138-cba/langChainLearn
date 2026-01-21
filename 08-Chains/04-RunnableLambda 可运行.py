"""
  RunnableLambda 可运行λ
    RunnableLambda 将 Python 可调用函数转换为 Runnable，使得函数可以在同步或异步上下文中使用
"""

#%%
from langchain_core.runnables import RunnableLambda

chain = {
  "text1": lambda x: x + " world",
  "text2": lambda x: x + ", how are you",
} | RunnableLambda(lambda x: len(x["text1"]) + len(x["text2"]))

result = chain.invoke("hello")
print(result) # 29 ("hello world" + "hello, how are you" 长度为29)
