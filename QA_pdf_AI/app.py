from flask import Flask, render_template, request
import os

from utils.pdf_reader import extract_text
from utils.chunking import chunk_text
from utils.embeddings import create_embeddings, model
from utils.vector_store import store_embeddings, search
from utils.llm import ask_llm

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():

    pdf = request.files["pdf"]

    path = os.path.join(UPLOAD_FOLDER, pdf.filename)

    pdf.save(path)

    text = extract_text(path)

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    store_embeddings(embeddings, chunks)

    return render_template("index.html", answer="PDF uploaded successfully!")

@app.route("/ask", methods=["POST"])
def ask():

    question = request.form["question"]

    question_embedding = model.encode(question)

    relevant_chunks = search(question_embedding)

    context = "\n".join(relevant_chunks)

    answer = ask_llm(context, question)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)