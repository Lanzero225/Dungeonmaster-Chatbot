import fitz
import re
import os
import json
import ollama
import faiss
import numpy as np

EMBEDDING_MODEL = "hf.co/CompendiumLabs/bge-base-en-v1.5-gguf"
INDEX_FILE = "faiss.index"
TEXTS_FILE = "texts_store.json"

# List the NEW documents you want to add to your existing database
NEW_DOCS_PATHS = ["New_Rules_Supplement.pdf", "patch_notes.txt"]


def parse_file(file_path):
    """Parses text chunks from either a PDF or a TXT file."""
    chunks = []
    if file_path.endswith(".pdf"):
        with fitz.open(file_path) as pdf:
            for page_number, page in enumerate(pdf, start=1):
                blocks = page.get_text("blocks", sort=False)
                page_width, page_height = page.rect.width, page.rect.height
                midpoint = page_width / 2

                left_column, right_column = [], []
                for block in blocks:
                    x0, y0, x1, y1, text = block[:5]
                    text = text.strip()
                    if not text or y1 <= 0 or y0 >= page_height:
                        continue
                    if (x0 + x1) / 2 < midpoint:
                        left_column.append((y0, text))
                    else:
                        right_column.append((y0, text))

                left_column.sort(key=lambda item: item[0])
                right_column.sort(key=lambda item: item[0])

                page_text = [t for _, t in left_column] + [
                    t for _, t in right_column
                ]
                cleaned_text = "\n\n".join(page_text)

                for chunk in re.split(r"\n\s*\n", cleaned_text):
                    chunk = re.sub(r"\s+", " ", chunk).strip()
                    if chunk:
                        chunks.append(chunk)
                print(
                    f"Processed PDF {file_path} - Page {page_number}/{len(pdf)}"
                )

    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            for chunk in re.split(r"\n\s*\n", content):
                chunk = re.sub(r"\s+", " ", chunk).strip()
                if chunk:
                    chunks.append(chunk)
        print(f"Processed TXT file: {file_path}")

    return chunks


# 1. Load existing FAISS index and text store
if os.path.exists(INDEX_FILE) and os.path.exists(TEXTS_FILE):
    print("Loading existing FAISS index and text store...")
    index = faiss.read_index(INDEX_FILE)
    with open(TEXTS_FILE, "r", encoding="utf-8") as f:
        texts = json.load(f)
else:
    raise FileNotFoundError(
        "Existing index or text store not found! Run your initial builder script first."
    )

# 2. Extract chunks from new documents
new_chunks = []
for path in NEW_DOCS_PATHS:
    if os.path.exists(path):
        new_chunks.extend(parse_file(path))
    else:
        print(f"Warning: File not found -> {path}")

if not new_chunks:
    print("No new chunks found to add. Exiting.")
    exit()

# 3. Generate embeddings for the new chunks only
print(f"Generating embeddings for {len(new_chunks)} new chunks...")
new_embeddings = []
for i, chunk in enumerate(new_chunks):
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)["embeddings"][0]
    new_embeddings.append(embedding)
    print(f"Embedded new chunk {i + 1}/{len(new_chunks)}")

# 4. Convert and add to FAISS index
new_embeddings_np = np.array(new_embeddings).astype("float32")
index.add(new_embeddings_np)  # Incrementally adds vectors to the HNSW graph

# 5. Append new text entries to the text store
texts.extend(new_chunks)

# 6. Save updated files back to disk
faiss.write_index(index, INDEX_FILE)
with open(TEXTS_FILE, "w", encoding="utf-8") as f:
    json.dump(texts, f)

print(
    f"\nSuccessfully added new documents! Total vectors in index now: {index.ntotal}"
)