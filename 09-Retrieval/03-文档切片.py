"""
  RecursiveCharacterTextSplitte （递归字符文本切分器）是最常用的切分器，它由一个字符列表作为参数，默认列表为 ["\n\n", "\n", " ", ""]，并且会尝试按顺序使用这些字符进行切分，直到块足够小。由此尽可能地将所有段落（然后是句子，最后是词）保持在一起，因为这些段落通常看起来是语义上最相关的文本片段

"""

#%%
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
import os
# 获取当前脚本所在的目录（不是工作目录！）
script_dir = os.path.dirname(os.path.abspath(__file__))
# 拼接出 sample.docx 的绝对路径
file_path = os.path.join(script_dir, "sample.docx")

# 加载文档
docs = UnstructuredWordDocumentLoader(
  file_path=file_path, mode="single"
).load()
# print(123, docs)
# # 切分为文本块
chunks = RecursiveCharacterTextSplitter(
  separators=["\n\n", "\n", "。", "！", "？", "……", "，", ""], # 分隔符列表
  chunk_size=400, # 每个块的最大长度
  chunk_overlap=50, # 每个块重叠的长度
  length_function=len, # 可选：计算文本长度的函数，默认为字符串长度，可自定义函数来实现按 token 数切分
  add_start_index=True, # 可选：块的元数据中添加此块起始索引
).split_documents(docs)

print(chunks) # [Document(metadata={..},page_content='...'), Document(metadata={..},page_content='...'), ...]