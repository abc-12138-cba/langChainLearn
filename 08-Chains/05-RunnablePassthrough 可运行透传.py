"""
  RunnablePassthrough 接收输入并将其原样输出。RunnablePassthrough 是 LangChain LCEL 体系中的“无操作节点”，用于在流水线中透传输入或保留上下文，也可以用于向输出中添加键
"""
# 举例1、保留中间结果
#%%
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

chain = RunnableParallel(
  original=RunnablePassthrough(), # 保留中间结果
  word_count=lambda x: len(x),
)

result = chain.invoke("hello world")
print(result) # {'original': 'hello world', 'word_count': 11}

 
#%%
# 举例2：使用 assign() 向输出中添加键
from langchain_core.runnables import RunnablePassthrough

chain = {
  "text1": lambda x: x + " world",
  "text2": lambda x: x + ", how are you",
} | RunnablePassthrough.assign(word_count=lambda x: len(x["text1"] + x["text2"])) # 添加 word_count 键

result = chain.invoke("hello")
print(result) # {'text1': 'hello world', 'text2': 'hello, how are you', 'word_count': 29}
# %%
