from src.text_splitter import split_text
from src.document_loader import load_pdf
from src.embeddings import generate_embeddings
from src.vector_store import create_vector_store 
from src.retriever import retrieve_chunks
from sentence_transformers import SentenceTransformer

def build_rag_pipeline(file_path, question):
    model = SentenceTransformer("notebook/models/all-MiniLM-L6-v2")
    text=load_pdf(file_path)
    chunks=split_text(text)
    chunks_embeddings=generate_embeddings(model,chunks)
    index = create_vector_store(chunks_embeddings)
    retrieved_chunks = retrieve_chunks(question,model,index,chunks)
    context=str(retrieved_chunks)
    prompt = f"""
        You are an AI assistant answering questions using the employee handbook.

        Context:
        {retrieved_chunks}

        Question:
        {question}

        Instructions:
        - Answer only using the provided context.
        - If the answer is not present in the context, say:
        "The provided context does not contain this information."

        Answer:
        """
    return prompt

if __name__=="__main__":
    file_path=r"D:\my_git\DocuMind-AI\data\policy document.pdf"
    question= input("Enter the question: ")
    prompt=build_rag_pipeline(file_path, question)
    print(prompt)