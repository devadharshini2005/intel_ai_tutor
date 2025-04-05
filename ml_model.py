from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data["question"]
    answer = qa_pipeline(question=question, context="General knowledge")
    return jsonify({"answer": answer["answer"]})

if __name__ == "__main__":
    app.run(port=8000)
