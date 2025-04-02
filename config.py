import os
from dotenv import load_dotenv

GOOGLE_API_KEY="AIzaSyDgBWzNA0wQ9-x4s-mwPXF_d4lBNlMF4zQ"
ASSEMBLYAI_API_KEY="f404822bcec346cf9009edbdccfcc52a"

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# Embedding model name
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ChromaDB path
CHROMA_DB_PATH =  "./chroma_db"

# AssemblyAI API key
ASSEMBLYAI_API_KEY=os.getenv("ASSEMBLYAI_API_KEY")