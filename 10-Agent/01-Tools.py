"""
  工具封装了一个可调用函数及其输入模式。这些参数可以传递给兼容的聊天模型，从而允许模型决定是否调用工具以及调用哪些参数。在这种情况下，工具调用使模型能够生成符合指定输入模式的请求

  创建工具：一个 Tool 通常包括工具名称，工具描述，以及工具参数的类型注解。可以通过 @tool 装饰器来创建工具
"""

#%%
#举例1：通过 @tool 创建工具

from langchain.tools import tool

@tool
def add_number(a: int, b: int) -> int:
  """两个整数相加"""
  return a + b

print(f"{add_number.name=}\n{add_number.description=}\n{add_number.args=}")
# add_number.name='add_number'
# add_number.description='两个整数相加'
# add_number.args={'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}


#%%
# 举例2：通过 @tool 的参数修改属性

from langchain.tools import tool
from pydantic import BaseModel, Field

class FieldInfo(BaseModel):
  a: int = Field(description="第1个参数")
  b: int = Field(description="第2个参数")

@tool(
  name_or_callable="add_2_number",
  description="计算两整数之和",
  args_schema=FieldInfo, # 定义参数模式
)
def add_number(a: int, b: int) -> int:
  """两个整数相加"""
  return a + b

print(f"{add_number.name=}\n{add_number.description=}\n{add_number.args=}")

# add_number.name='add_2_number'
# add_number.description='计算两整数之和'
# add_number.args={'a': {'description': '第1个参数', 'title': 'A', 'type': 'integer'}, 'b': {'description': '第2个参数', 'title': 'B', 'type': 'integer'}}
