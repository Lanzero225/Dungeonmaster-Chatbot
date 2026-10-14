import fitz
import re
import ollama
import chromadb

PDF_PATH = ["SRD-OGL_V1.1.pdf", "SRD_CC_v5.2.pdf"]
EMBEDDING_MODEL = "hf.co/CompendiumLabs/bge-base-en-v1.5-gguf"


# 1. Parse PDF into chunks
def load_pdf_dataset(pdf_path):
    dataset = []
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

            page_text = [t for _, t in left_column] + [t for _, t in right_column]
            cleaned_text = "\n\n".join(page_text)

            for chunk in re.split(r"\n\s*\n", cleaned_text):
                chunk = re.sub(r"\s+", " ", chunk).strip()
                if chunk:
                    dataset.append(chunk)
            print(f"Processed page {page_number}/{len(pdf)}")
    return dataset


dataset = load_pdf_dataset(PDF_PATH)

# 2. Initialize ChromaDB persistent client
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="srd_docs")

# 3. Add chunks & embeddings to ChromaDB
for i, chunk in enumerate(dataset):
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)["embeddings"][0]

    collection.add(
        documents=[chunk],
        embeddings=[embedding],
        ids=[f"chunk_{i}"],
    )

print("\nDatabase built successfully in './chroma_db'!")