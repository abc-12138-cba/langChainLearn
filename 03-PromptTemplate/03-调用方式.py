# 除了 format 方法，也可以使用 invoke 方法调用

#%%
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("{foo} {bar}")

prompt = template.invoke({"foo": "hello", "bar": "world"})

print(prompt, type(prompt)) # text='hello world' <class 'langchain_core.prompt_values.StringPromptValue'>

# invoke 方法返回 PromptValue 对象，可以使用 to_string 方法将其转换为字符串
prompt_str = prompt.to_string()

print(prompt_str, type(prompt_str))# hello world <class 'str'>