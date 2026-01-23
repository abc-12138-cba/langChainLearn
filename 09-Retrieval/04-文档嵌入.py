"""
  使用嵌入模型生成文档的嵌入向量，后续检索时用于与查询的嵌入向量进行相似度计算(将文本嵌入为简单的向量表示)

"""
# pip install sentence-transformers langchain_huggingface （mac版本太低无法安装成功，无法查看效果）
#%%
import os
from langchain_huggingface import HuggingFaceEmbeddings

# 加载嵌入模型
embed_model = HuggingFaceEmbeddings(
  model_name=os.path.expanduser("~/models/bge-base-zh-v1.5")
)

# 单文本嵌入
query = "你好，世界"
print(embed_model.embed_query(query))

# 多文本嵌入
# docs = ["你好，世界", "你好，世界"]
# print(embed_model.embed_documents(docs))