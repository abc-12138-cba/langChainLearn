"""
  当希望在格式化过程中插入消息列表时，比如 Agent 暂存中间步骤，需要使用 MessagesPlaceholder，负责在特定位置添加消息列表
"""

#%%
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
  [
    ("system", "你是一个助手。"),
    ("placeholder", "{conversation}"),
  # 等同于 MessagesPlaceholder(variable_name="conversation", optional=True)
  ]
)

prompt = template.format_messages(
 conversation=[
  ("human", "你好！"),
  ("ai", "想让我帮你做些什么？"),
  ("human", "能帮我做一个冰淇凌吗？"),
  ("ai", "不能"),
 ]
)

print(prompt)