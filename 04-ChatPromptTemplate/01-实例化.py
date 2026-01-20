
"""
  介绍: ChatPromptTemplate 是创建聊天消息列表的提示模板。相较于普通 PromptTemplate更适合处理多角色、多轮次的对话场景。支持 System/Human/AI 等不同角色的消息模板

  实例化时需要传入 messages 参数,messages 参数支持如下格式：
    tuple 构成的列表，格式为[(role, content)]
    dict 构成的列表，格式为[{“role”:... , “content”:...}]
    Message 类构成的列表
"""

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

prompt = template.format_messages(thing="AI2", name="小谷AI",  user_input="行")
print(prompt)
# [
# SystemMessage(content="你是一个AI开发工程师，你的名字是小谷AI。",...),
# HumanMessage(content="你能帮我做什么?", ...),
# AIMessage(content="我能开发很多AI。", ...),
# HumanMessage(content="行", ...),
# ]