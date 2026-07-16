# DocuMind AI – End-to-End RAG Question Answering System

## Overview

- DocuMind AI is an end-to-end Retrieval-Augmented Generation (RAG) application that enables users to ask natural language questions about a PDF document. The system retrieves the most relevant information using semantic search (FAISS + Sentence Transformers) and generates context-aware answers using the OpenAI API.

- The project is designed with a modular architecture and separates preprocessing from inference to improve performance by avoiding repeated embedding generation.

## Features
- Upload PDF documents through a REST API.
- Automatic PDF preprocessing and text extraction.
- Recursive text chunking using LangChain.
- Semantic embeddings generated with Sentence Transformers.
- FAISS vector database for efficient similarity search.
- Retrieval-Augmented Generation (RAG) pipeline using OpenAI.
- REST API for document upload and question answering.
- Amazon S3 integration for persistent storage of uploaded PDFs and vector store artifacts.
- AWS EC2 deployment for cloud-hosted inference.


## System Architecture

                  Upload PDF
                       │
                       ▼
                Flask Upload API
                       │
                       ▼
              PDF Preprocessing
                       │
         Text Extraction & Chunking
                       │
                       ▼
          Sentence Transformers Embeddings
                       │
                       ▼
                FAISS Index
                       │
             Save Vector Store
                       │
             Upload to Amazon S3
                       
────────────────────────────────────────────────────

                User Question
                       │
                       ▼
                Flask Ask API
                       │
                       ▼
        Download Vector Store (if needed)
                       │
                       ▼
             Semantic Retrieval
                       │
                       ▼
          Retrieved Context + Question
                       │
                       ▼
                 OpenAI GPT
                       │
                       ▼
                    Answer


## Tech Stack
### Backend
- Python
- Flask
- REST API
### Retrieval-Augmented Generation
- OpenAI API
- Sentence Transformers
- FAISS
- LangChain Text Splitters
### Cloud
- Amazon EC2
- Amazon S3
### Data Processing
- PyPDF
- NumPy

## Installation

### clone the repository:

``` git clone <repository-url>
cd DocuMind-AI
``` 
### Create a virtual environment:

python -m venv .venv

Activate it:

Windows
.venv\Scripts\activate
Linux / macOS
source .venv/bin/activate

### Install dependencies:

pip install -r requirements.txt

### Environment Variables

Create a .env file in the project root.

OPENAI_API_KEY=your_openai_api_key
Running the Application
python app.py

### The server starts on:

``` http://localhost:5000```
### REST API
Upload a Document

POST

/upload

Form Data

file : PDF

Example:

curl -X POST http://localhost:5000/upload \
-F "file=@policy_document.pdf"
Ask a Question

POST

/ask

Request

{
    "question":"What are the working hours?"
}

Response

{
    "answer":"Employees are expected to work from 9:00 AM to 5:30 PM."
}
### Deployment

- The application is deployed on Amazon EC2 using Flask.

- Persistent storage is handled by Amazon S3.

- Uploaded documents are stored in S3.

- Generated FAISS indexes and document chunks are also uploaded to S3, allowing the application to rebuild its retrieval pipeline without requiring users to upload the documents again.

## Future Improvements

- Integrate Amazon Secrets Manager or Parameter Store for secure API key management.
- Support multiple uploaded documents.
- Add document versioning.
- Store metadata in Amazon DynamoDB.
- Containerize the application using Docker.
- Deploy with Gunicorn and Nginx for production.
- Add user authentication and role-based access.
- Build a Streamlit or React frontend.
- Key Learnings

### This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Large Language Model Integration
- REST API Development
- Cloud Deployment with AWS
- Persistent Storage using Amazon S3
- Modular AI System Design