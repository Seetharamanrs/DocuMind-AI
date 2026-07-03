from src.document_loader import load_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,
    chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    return chunks

if __name__=="__main__":
    file_path=r"D:\my_git\DocuMind-AI\data\policy document.pdf"
    text=load_pdf(file_path)
    split_text(text)
