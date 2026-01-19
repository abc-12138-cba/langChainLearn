import os
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
    model="google_genai:gemini-2.5-flash-lite",
)

messages = [
    SystemMessage(content="你是一个诗人"),
    HumanMessage(content="写一首关于春天的诗"),
]
resp = llm.invoke(messages)
print(type(resp)) # <class 'langchain_core.messages.ai.AIMessage'>
print(resp.content)