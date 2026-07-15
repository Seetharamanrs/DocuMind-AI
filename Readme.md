# DocuMind AI – End-to-End RAG Question Answering System
## Overview

- DocuMind AI is an end-to-end Retrieval-Augmented Generation (RAG) application that enables users to ask natural language questions about a PDF document. The system retrieves the most relevant information using semantic search (FAISS + Sentence Transformers) and generates context-aware answers using the OpenAI API.

- The project is designed with a modular architecture and separates preprocessing from inference to improve performance by avoiding repeated embedding generation.
