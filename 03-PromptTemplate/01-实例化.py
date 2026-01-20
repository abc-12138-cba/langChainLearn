#%%
# 1、使用构造方法实例化提示词模板
from langchain_core.prompts import PromptTemplate
# 使用构造方法实例化提示词模板
template = PromptTemplate(
  template="请评价{product}的优缺点，包括{aspect1}和{aspect2}。",
  input_variables=["product", "aspect1", "aspect2"],
)

# 使用模板生成提示词
prompt_1 = template.format(product="智能手机", aspect1="电池续航", aspect2="拍照质量")
prompt_2 = template.format(product="笔记本电脑", aspect1="处理速度", aspect2="便携性")

print(prompt_1) # 请评价智能手机的优缺点，包括电池续航和拍照质量。
print(prompt_2) # 请评价笔记本电脑的优缺点，包括处理速度和便携性。


#%%
# 2、使用 from_template 方法实例化提示词模板
from langchain_core.prompts import PromptTemplate

# 使用 from_template 方法实例化提示词模板
template = PromptTemplate.from_template("请给我一个关于{topic}的{type}解释。")

# 使用模板生成提示
prompt = template.format(type="详细", topic="量子力学")

print(prompt) # 请给我一个关于量子力学的详细解释。