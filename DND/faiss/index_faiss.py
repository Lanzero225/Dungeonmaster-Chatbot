import fitz
import re
import ollama
import faiss
import numpy as np
import json

PDF_PATHS = ["SRD-OGL_V1.1.pdf", "SRD_CC_v5.2.pdf"]
EMBEDDING_MODEL = "hf.co/CompendiumLabs/bge-base-en-v1.5-gguf"
INDEX_FILE = "faiss/faiss.index"
TEXTS_FILE = "faiss/texts_store.json"


def load_pdf_dataset(pdf_paths):
    dataset = []
    for pdf_path in pdf_paths:
        with fitz.open(pdf_path) as pdf:
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
                    if len(chunk) < 30:
                        continue  # Skip very short chunks
                    if chunk:
                        dataset.append(chunk)
                print(f"Processed {pdf_path} - Page {page_number}/{len(pdf)}")
    return dataset


# Load text dataset
dataset = load_pdf_dataset(PDF_PATHS)

embeddings = []
texts = []

# Generate embeddings
for i, chunk in enumerate(dataset):
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)["embeddings"][0]
    embeddings.append(embedding)
    texts.append(chunk)
    print(f"Embedded chunk {i + 1}/{len(dataset)}")

# Convert to numpy array for FAISS (must be float32)
embeddings_np = np.array(embeddings).astype("float32")

# Initialize FAISS index based on vector dimension (bge-base is 768 dimensions)
dimension = embeddings_np.shape[1]
index = faiss.IndexFlatL2(dimension)  # L2 (Euclidean) distance index

# Add vectors to index
index.add(embeddings_np)

# Save FAISS index and text store to disk
faiss.write_index(index, INDEX_FILE)
with open(TEXTS_FILE, "w", encoding="utf-8") as f:
    json.dump(texts, f)

print(
    f"\nSuccessfully built and saved FAISS index ({index.ntotal} vectors) and text store!"
)