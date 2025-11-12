from langchain_openai import ChatOpenAI
import os, dotenv

dotenv.load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# 1、获取对话模型：
chat_model = ChatOpenAI(
    #必须要设置的3个参数
    model="gpt-4o-mini",   #默认使用的是gpt-3.5-turbo模型
)

# 2、调用模型
response = chat_model.invoke("什么是langchain?")

# 3、查看响应的文本
# print(response.content)
print(response)