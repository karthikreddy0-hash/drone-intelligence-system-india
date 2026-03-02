# rag/loader.py

from docx import Document
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import os
print(os.listdir("data/raw"))

def load_docx(folder_path):
    documents = []
    
    for file in os.listdir(folder_path):
        if file.endswith(".docx"):
            doc = Document(os.path.join(folder_path, file))
            text = "\n".join([para.text for para in doc.paragraphs])
            documents.append(text)
    
    return documents

docs = load_docx("data/raw")

print("Documents loaded:", len(docs))

### chunkings
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.create_documents(docs)

print("Total chunks created:", len(chunks))