
from src.vector_store import  load_chunks, load_vector_store
from src.retriever import retrieve_chunks
from sentence_transformers import SentenceTransformer
from src.llm import generate_answer

def initialize_rag():
    model = SentenceTransformer("notebook/models/all-MiniLM-L6-v2")
    chunks=load_chunks()
    index = load_vector_store()
    return model, index, chunks

def ask_question(question, model, index, chunks):
    retrieved_chunks = retrieve_chunks(question,model,index,chunks)
    context=str(retrieved_chunks)
    prompt = f"""
        You are an AI assistant answering questions using the employee handbook.

        Context:
        {context}
        
        Question:
        {question}

        Instructions:
        - Answer only using the provided context.
        - If the answer is not present in the context, say:
        "The provided context does not contain this information."

        Answer:
        """
    response=generate_answer(prompt)
    return response

if __name__=="__main__":
    file_path=r"D:\my_git\DocuMind-AI\data\policy document.pdf"
    model,index,chunks=initialize_rag()

    print("DocuMind AI is ready!!!!")
    print(" Type exit to quit.\n")

    while True:
        question= input("Enter the question: ")
        if question.lower() == "exit":
            print("Goodbye!")
            break
        else:
            response=ask_question(question,model,index,chunks)
            print(f"{response.output_text}\n")
            