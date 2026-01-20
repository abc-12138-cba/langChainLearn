# 01 是format_messages调用，另外还有 invoke 方式

#%%
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate(
  [
    ("system", "你是一个AI开发工程师，你的名字是{name}。"),
    ("human", "你能帮我做什么?"),
    ("ai", "我能开发很多{thing}。"),
    ("human", "{user_input}"),
  ]
)

prompt = template.invoke({"name": "小谷AI", "thing": "AI", "user_input": "行"}) # 需传入字典形式数据
print(prompt)
# [
# SystemMessage(content="你是一个AI开发工程师，你的名字是小谷AI。",...),
# HumanMessage(content="你能帮我做什么?", ...),
# AIMessage(content="我能开发很多AI。", ...),
# HumanMessage(content="行", ...),
# ]