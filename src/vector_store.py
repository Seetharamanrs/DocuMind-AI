import faiss
import numpy as np
from src.text_splitter import split_text
from src.document_loader import load_pdf
from src.embeddings import generate_embeddings

def create_vector_store(chunks_embeddings):
    embeddings=np.array(chunks_embeddings).astype("float32")
    dimension=embeddings.shape[1]
    index=faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index
if __name__=="__main__":
    file_path=r"D:\my_git\DocuMind-AI\data\policy document.pdf"
    text=load_pdf(file_path)
    chunks=split_text(text)
    chunks_embeddings=generate_embeddings(chunks)
    index = create_vector_store(chunks_embeddings)
    print(index.ntotal)