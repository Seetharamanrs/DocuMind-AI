from flask import Flask,request,jsonify
from src.rag_pipeline import initialize_rag,ask_question
from src.preprocessing import preprocess_document
app=Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024

model,index,chunks=initialize_rag()

@app.post("/ask")
def ask():
    data=request.get_json()
    question=data["question"]
    response=ask_question(question, model, index, chunks)
    return jsonify({
        "answer": response.output_text
    })

@app.post("/upload")
def upload():
    global model,index,chunks
    if "file" not in request.files:
        return jsonify({
        "error": "No file uploaded."
    }), 400

    uploaded_file=request.files['file']
    if not uploaded_file.filename.lower().endswith(".pdf"):
        return jsonify({
        "error": "Only PDF files are allowed."
    }), 400
    
    file_path= f"data/{uploaded_file.filename}"
    uploaded_file.save(file_path)
    preprocess_document(file_path)
    model, index, chunks = initialize_rag()
    return jsonify({
    "message": "Document uploaded and vector store updated successfully"
}), 200

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
