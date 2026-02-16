from google import genai
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import os
import numpy as np
import faiss

# ------------------ Setup ------------------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)

# Load local embedding model (runs on your machine)
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# ------------------ 1. Load PDFs ------------------
def load_pdfs(folder="documents"):
    texts = []

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder, file)
            reader = PdfReader(file_path)

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    texts.append(text)

    return texts


# ------------------ 2. Chunk Text ------------------
def chunk_text(text, chunk_size=1500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks


# ------------------ 3. Create Local Embeddings ------------------
def embed_texts(texts):
    embeddings = embed_model.encode(texts, show_progress_bar=True)
    return np.array(embeddings).astype("float32")


# ------------------ 4. Build Vector Database ------------------
print("Loading PDFs...")
documents = load_pdfs()

print("Chunking text...")
chunks = []
for doc in documents:
    chunks.extend(chunk_text(doc))

print("Total chunks:", len(chunks))

print("Generating local embeddings...")
embeddings = embed_texts(chunks)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("Vector database ready.")


# ------------------ 5. Ask Question ------------------
def ask_question(question, k=3):
    question_embedding = embed_texts([question])
    distances, indices = index.search(question_embedding, k)

    retrieved_chunks = [chunks[i] for i in indices[0]]
    context = "\n".join(retrieved_chunks)

    prompt = f"""
    You are a financial assistant.
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# ------------------ Run ------------------
if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (type 'exit' to quit): ")
        if question.lower() == "exit":
            break

        answer = ask_question(question)
        print("\nAnswer:\n", answer)
