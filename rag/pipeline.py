# rag/pipeline.py

import os
from vector_store import build_or_load_index, retrieve
from generator import generate_with_gemini

def ask_rag(query):

    documents, model, index = build_or_load_index()

    retrieved_docs = retrieve(query, model, index, documents)

    context = "\n\n".join(retrieved_docs)

    prompt = f"""
    You are an AI assistant for India's Drone Intelligence System.

    Use the context below to answer clearly and professionally.

    Context:
    {context}

    Question:
    {query}
    """

    answer = generate_with_gemini(prompt)




  answer = ask_rag("Explain drone regulations in india")
print(answer)
    return answer


if __name__ == "__main__":

    os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_KEY"

    question = "Explain drone regulations in India"

    print(ask_rag(question))