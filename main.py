import os
from dotenv import load_dotenv
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

openai_ef = OpenAIEmbeddingFunction(
    api_key=openai_key,
    model_name="text-embedding-3-small"
)

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(
    name="news_articles",
    embedding_function=openai_ef
)

collection.add(
    documents=["AI is transforming healthcare."],
    ids=["doc1"]
)

print("✅ Document added successfully")
