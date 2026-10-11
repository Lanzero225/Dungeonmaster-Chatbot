import faiss
import json
import ollama
import numpy as np
import os

# Get the directory where the current script is running
# Get the directory where the current script is running
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INDEX_FILE = os.path.join(BASE_DIR, "faiss.index")
TEXTS_FILE = os.path.join(BASE_DIR, "texts_store.json")

EMBEDDING_MODEL = "hf.co/CompendiumLabs/bge-base-en-v1.5-gguf"
LANGUAGE_MODEL = "hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF"

# Load FAISS index and text mapping from disk
print("Loading FAISS index and texts...")
index = faiss.read_index(INDEX_FILE)
with open(TEXTS_FILE, "r", encoding="utf-8") as f:
    texts = json.load(f)


def retrieve(query, top_n=10):
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)[
        "embeddings"
    ][0]
    query_np = np.array([query_embedding]).astype("float32")

    # Search FAISS index (returns distances and indices)
    distances, indices = index.search(query_np, top_n)

    # Retrieve matching text blocks using the returned indices
    retrieved_chunks = [texts[idx] for idx in indices[0]]
    return retrieved_chunks


# Chat Loop
while True:
    input_query = input("\nAsk me a question (or type 'exit' to quit): ")
    if input_query.lower() in ["exit", "quit"]:
        break

    retrieved_chunks = retrieve(input_query)
    context = "\n".join([f"- {chunk}" for chunk in retrieved_chunks])

    instruction_prompt = f"""You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
{context}
"""

    stream = ollama.chat(
        model=LANGUAGE_MODEL,
        messages=[
            {"role": "system", "content": instruction_prompt},
            {"role": "user", "content": input_query},
        ],
        stream=True,
    )

    print("\nChatbot response:")
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)
    print()