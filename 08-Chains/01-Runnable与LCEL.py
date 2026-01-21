"""
  Runnable 是 LangChain 中可以调用、批处理、流式传输、转换和组合的工作单元

  LangChain 表达式语言（LCEL，LangChain Expression Language）是一种从现有的Runnable 构建新的 Runnable 的声明式方法，用于声明、组合和执行各种组件（模型、提示、工具、函数等）
  我们称使用 LCEL 创建的 Runnable 为“链”，“链”本身就是 Runnable
"""

"""
prompt_text = prompt.format(topic="猫") # 方法1
model_out = model.generate(prompt_text) # 方法2
result = parser.parse(model_out) # 方法3


# 分步调用
prompt_text = prompt.invoke({"topic": "猫"}) # 方法1
model_out = model.invoke(prompt_text) # 方法2
result = parser.invoke(model_out) # 方法3



# LCEL管道式
chain = prompt | model | parser # 用管道符组合
result = chain.invoke({"topic": "猫"}) # 所有组件统一用invoke

"""