# 🧠 RAG-Based Customer Support Assistant (LangGraph + HITL)

## 📌 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG) based Customer Support Assistant** using **LangGraph workflows** and **Human-in-the-Loop (HITL)** validation.

The system answers user queries by retrieving relevant information from a knowledge base and generating context-aware responses. If the system is uncertain, it routes the response to a human for validation or correction.

---

## 🚀 Key Features

* 🔍 **RAG Pipeline**

  * Retrieves relevant documents using vector similarity search
  * Generates answers using retrieved context

* 🔁 **LangGraph Workflow**

  * Structured execution pipeline with nodes:

    * Retrieve
    * Generate
    * Confidence Check
    * Human Review

* 👨‍💻 **Human-in-the-Loop (HITL)**

  * Low-confidence responses are flagged
  * Human can approve or correct answers

* ⚡ **Fully Local Execution**

  * Uses HuggingFace models (no API key required)
  * Runs on CPU (Google Colab compatible)

---

## 🏗️ System Architecture

```
User Query
    ↓
Retriever (FAISS Vector DB)
    ↓
LLM (Answer Generator)
    ↓
Confidence Check
    ↓
 ┌───────────────┬───────────────┐
 │               │               │
High Confidence   Low Confidence
 │               │
 ▼               ▼
Final Answer   Human Review (HITL)
                    ↓
              Corrected Answer
```

---

## 🧰 Tech Stack

* Python
* LangChain (modular packages)
* LangGraph
* FAISS (vector database)
* HuggingFace Transformers
* Sentence Transformers

---

## 📂 Dataset

A **simulated customer support knowledge base** was created consisting of common troubleshooting queries such as:

* Device reset
* Battery issues
* Connectivity problems
* Warranty policies

This approach allows rapid prototyping without relying on proprietary data.

---

## ⚙️ Installation

Run the following in your environment (e.g., Google Colab):

```bash
pip install -U langchain langchain-community langchain-text-splitters faiss-cpu sentence-transformers transformers
```

---

## ▶️ Usage

Run the Python script:

```bash
python rag_support_assistant.py
```

Then enter queries such as:

```
How to reset the device?
Why is my battery not charging?
```

Type `exit` to stop the program.

---

## 🔁 Workflow Explanation

1. **Retrieve**

   * Finds relevant documents from vector database

2. **Generate**

   * LLM generates an answer using retrieved context

3. **Confidence Check**

   * Detects uncertainty (e.g., "I don't know")

4. **Human Review (HITL)**

   * User can approve or modify the response

---

## ⚠️ Limitations

* Uses a small, simulated dataset
* Basic confidence evaluation logic
* No graphical user interface (CLI-based)
* Not optimized for large-scale deployment

---

## 🚀 Future Improvements

* Add real-world document ingestion (PDF, web data)
* Implement advanced confidence scoring using LLMs
* Build a web interface (Streamlit)
* Store human feedback for continuous learning
* Deploy as an API service

---

## 🎯 Conclusion

This project demonstrates a **functional prototype of a RAG-based customer support system** with structured workflows and human oversight. It highlights how modern LLM pipelines can be enhanced with retrieval mechanisms and human validation for improved reliability.

---

## 👤 Author

Aditi Nilesh Badage

---

## 📜 License

This project is for academic and demonstration purposes.
