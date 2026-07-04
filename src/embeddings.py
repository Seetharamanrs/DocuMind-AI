from sentence_transformers import SentenceTransformer
from src.document_loader import load_pdf
from src.text_splitter import split_text
def generate_embeddings(chunks):
    model=SentenceTransformer("models/all-MiniLM-L6-v2")
    chunks_embedding=model.encode(chunks)
    return chunks_embedding

if __name__=="__main__":
    file_path=r"D:\my_git\DocuMind-AI\data\policy document.pdf"
    text=load_pdf(file_path)
    chunks=split_text(text)
    generate_embeddings(chunks)
