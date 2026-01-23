"""
  此 Agent 会在一个循环中反复调用模型和工具，直到某次模型输出中不再包含工具调用则结束
  使用 create_agent 创建 Agent 时，需传入模型和工具、可选地也可以传入系统提示词
"""

#%%
import os
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

llm = init_chat_model(
  model="google_genai:gemini-2.5-flash-lite",
)

# 定义 Tavily 搜索工具 tavily_api_key
search = TavilySearch(
  max_results=5,
  tavily_api_key=os.getenv("TAVILY_API_KEY")
)
tools = [search]

# 创建 Agent
agent = create_agent(
  model=llm, # 模型
  tools=tools, # 工具
  system_prompt="你是位助手，需要调用工具来帮助用户。", # 系统提示词
)

# 调用 Agent
# res = agent.invoke(
#   {"messages": [{"role": "user", "content": "今天北京的天气怎么样？"}]}
# )

# print(res) # { 'messages': [HumanMessage(), AIMessage(), ToolMessage()] }
#%%
# 调用 Agent,流式返回，避免卡住
for chunk in agent.stream(
  {
    "messages": [
      {"role": "system", "content": "你是位助手，需要调用工具来帮助用户。"},
      {"role": "user", "content": "今天北京的天气怎么样？"},
    ]
  }
):
  print(chunk, end="\n\n") 
  # {'model: { 'message': [AIMessage()]}}
  # {'tools: { 'message': [ToolMessage()]}}
  # {'model: { 'message': [AIMessage()]}}
