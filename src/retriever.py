from sentence_transformer import SentenceTransformer
from src.text_splitter import split_text
from src.document_loader import load_pdf
from src.embeddings import generate_embeddings
from src.vector_store import create_vector_store

def retrieve_chunks(query, model, index, chunks, k=3):
    query_embedding = model.encode([query])
    query_embedding = query_embedding.astype("float32")

    distances, indices = index.search(query_embedding, k)
    
    retrieved_chunks=[]
    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks


if __name__=="__main__":
    file_path=r"D:\my_git\DocuMind-AI\data\policy document.pdf"
    text=load_pdf(file_path)
    chunks=split_text(text)
    model = SentenceTransformer("models/all-MiniLM-L6-v2")
    chunks_embeddings=generate_embeddings(model,chunks)
    index = create_vector_store(chunks_embeddings)
    query=input("Enter the question: ")
    retrieved_chunks = retrieve_chunks(
        query,
        model,
        index,
        chunks
    )

    print("\nRetrieved Chunks:\n")
    for i, chunk in enumerate(retrieved_chunks, start=1):
        print(f"Chunk {i}:")
        print(chunk)
        print("-" * 80)
    