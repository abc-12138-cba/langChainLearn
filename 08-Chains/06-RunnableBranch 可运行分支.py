"""
  RunnableBranch 使用 (条件,Runnable) 对列表和默认分支进行初始化。对输入进行操作时,选择第一个计算结果为 True 的条件,并在输入上运行相应的 Runnable。如果没有条件为 True,则在输入上运行默认分支
"""

#%%
from langchain_core.runnables import RunnableBranch

branch = RunnableBranch(
 (lambda x: isinstance(x, str), lambda x: x.upper()),
 (lambda x: isinstance(x, int), lambda x: x + 1),
 (lambda x: isinstance(x, float), lambda x: x * 2),
 lambda x: "goodbye",
)

result = branch.invoke("hello")
print(result) # HELLO

result = branch.invoke(None)
print(result) # goodbye