from flask import Flask,request,jsonify
from src.rag_pipeline import initialize_rag,ask_question
app=Flask(__name__)

model,index,chunks=initialize_rag()

@app.post("/ask")
def ask():
    data=request.get_json()
    question=data["question"]
    response=ask_question(question, model, index, chunks)
    return jsonify({
        "answer": response.output_text
    })

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
