# rag/vector_store.py

vectorstore = FAISS.from_documents(chunks, embeddings)

print("Vector database created successfully!")