"""
  创建模型实例，并通过 bind_tools 方法将工具绑定到大模型
  （1）大模型通过分析用户需求，判断是否需要调用工具。
  （2）如果需要则在响应的 additional_kwargs 参数中包含工具调用的详细信息。
  （3）使用模型提供的参数执行工具。
"""

#%%
import os
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
    model="google_genai:gemini-2.5-flash-lite",
)

@tool
def query_user_info(user_id: int) -> str:
  """查询用户信息"""
  return {1001: "Jack", 1002: "Tom", 1003: "Alice"}[user_id]

# 为模型提供工具
tools = [query_user_info]
llm_with_tools = llm.bind_tools(tools)
resp = llm_with_tools.invoke("帮我查下1001用户的信息")
# print(resp) # 返回的响应中 additional_kwargs 参数中包括了工具调用的信息，此时还没有调用工具，只是返回了要调用的工具及参数

# 手动执行工具
for tool_call in resp.tool_calls:
  tool_name = tool_call["name"] # 获取工具名称
  tool_args = tool_call["args"] # 获取工具参数
  tool_result = globals()[tool_name].invoke(tool_args) # 执行工具
  print(tool_name, tool_args, tool_result) # query_user_info {'user_id': 1001} Jack

