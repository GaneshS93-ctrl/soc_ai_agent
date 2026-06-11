from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0,
    max_tokens=800,
    max_retries=0
)