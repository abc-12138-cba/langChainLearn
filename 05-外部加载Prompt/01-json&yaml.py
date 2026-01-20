"""
  可以将 prompt 保存为 JSON 或者 YAML 等格式的文件，通过读取指定路径的格式化文件，获取相应的 prompt。这样方便对 prompt 进行管理和维护
"""
#%%
from langchain_core.prompts import load_prompt

template = load_prompt("./prompt.json", encoding="utf-8")
print(template.format(name="张三", what="搞笑的")) # 请张三讲一个搞笑的的故事



#%%
from langchain_core.prompts import load_prompt

template = load_prompt("./prompt.yaml", encoding="utf-8")
print(template.format(name="年轻人", what="滑稽")) # 请年轻人讲一个滑稽的故事