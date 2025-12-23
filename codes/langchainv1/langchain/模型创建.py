"""
File: 模型创建.py
Created Time: 2025-11-16
Author: falcon (liuc47810@gmail.com)
"""

from langchain_openai import ChatOpenAI
import os, dotenv

dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
model = ChatOpenAI(model="gpt-5-mini")
