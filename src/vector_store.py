import faiss
import pickle
import numpy as np


def create_vector_store(chunks_embeddings):
    embeddings=np.array(chunks_embeddings).astype("float32")
    dimension=embeddings.shape[1]
    index=faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index
def save_vector_store(index):
    faiss.write_index(index,"vector_store/faiss_index.bin")

def load_vector_store():
    index = faiss.read_index("vector_store/faiss_index.bin")
    return index


def save_chunks(chunks):
    with open("vector_store/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)


def load_chunks():
    with open("vector_store/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return chunks 


# if __name__=="__main__":
#     file_path=r"D:\my_git\DocuMind-AI\data\policy document.pdf"
#     text=load_pdf(file_path)
#     chunks=split_text(text)
#     chunks_embeddings=generate_embeddings(chunks)
#     index = create_vector_store(chunks_embeddings)
#     print(index.ntotal)