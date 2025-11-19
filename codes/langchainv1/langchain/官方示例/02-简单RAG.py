import os

import bs4
import dotenv
from langchain.agents import create_agent
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.tools import tool
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 加载环境配置
dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
# 创建向量模型
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Load and chunk contents of the blog
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

# Index chunks
vector_store = InMemoryVectorStore(embedding=embeddings)
_ = vector_store.add_documents(documents=all_splits)


# Construct a tool for retrieving context
@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


tools = [retrieve_context]
# If desired, specify custom instructions
prompt = (
    "You have access to a tool that retrieves context from a blog post. "
    "Use the `retrieve_context` tool to help answer user queries."
)
agent = create_agent("gpt-5-mini", tools, system_prompt=prompt)

# agent调用
query = "What is task decomposition?"
for step in agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        stream_mode="values",
):
    step["messages"][-1].pretty_print()
