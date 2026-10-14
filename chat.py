import chromadb
import ollama

EMBEDDING_MODEL = "hf.co/CompendiumLabs/bge-base-en-v1.5-gguf"
LANGUAGE_MODEL = "hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF"

# Connect to the existing disk-backed database
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="srd_docs")


def retrieve(query, top_n=5):
    # Get embedding for the user query
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)[
        "embeddings"
    ][0]

    # Query ChromaDB directly
    results = collection.query(
        query_embeddings=[query_embedding], n_results=top_n
    )

    # Return retrieved text documents
    return results["documents"][0]


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