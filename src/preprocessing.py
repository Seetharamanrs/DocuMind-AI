from sentence_transformers import SentenceTransformer
from src.document_loader import load_pdf
from src.text_splitter import split_text
from src.embeddings import generate_embeddings
from src.vector_store import create_vector_store, save_vector_store, save_chunks
def preprocess_document(file_path):
    model = SentenceTransformer("notebook/models/all-MiniLM-L6-v2")

    text = load_pdf(file_path)

    chunks = split_text(text)

    chunk_embeddings = generate_embeddings(model, chunks)

    index = create_vector_store(chunk_embeddings)

    save_vector_store(index)

    save_chunks(chunks)

    print("Preprocessing completed successfully!")