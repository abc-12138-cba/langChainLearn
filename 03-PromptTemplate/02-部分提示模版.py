# 1、实例化过程中指定 partial_variables 参数
#%%
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
  template="{foo} {bar}",
  input_variables=["foo", "bar"],
  partial_variables={"foo": "hello"}, # 预先定义部分变量
)

prompt = template.format(bar="world") # foo 不传就读内置的值

print(prompt) # hello world


# 2、使用 partial 方法指定默认值
#%%
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("{foo} {bar}")

partial_template = template.partial(foo="hello") # 预先定义部分变量

prompt = partial_template.format(bar="world")

print(prompt) # hello world