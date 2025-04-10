# 🧠 Research Paper Summarizer & Podcast Generator

A full-stack AI-powered app that lets users **upload research papers (PDFs)**, automatically **summarizes them using NLP**, and generates a **podcast-style audio** of the summary using text-to-speech (TTS).

Built with **FastAPI + Streamlit + Transformers + gTTS**, and Dockerized for easy deployment.

---

## 🚀 Features

- 📄 Upload PDF research papers
- 🧠 AI-generated summaries using Hugging Face transformers
- 🎧 Convert summary to audio using gTTS
- 🎛️ Streamlit-based user interface
- 🐳 Fully Dockerized (1-line launch)
- ⚡ FastAPI backend with REST API support

---

## 🛠️ Tech Stack

| Layer        | Technology                  |
|--------------|-----------------------------|
| 🧠 NLP Model  | HuggingFace Transformers (`bart-large-cnn`) |
| 🎧 TTS        | `gTTS` (Google Text-to-Speech) |
| 📦 Backend    | FastAPI + Uvicorn          |
| 🎛️ Frontend   | Streamlit                  |
| 🐳 Container  | Docker + Docker Compose     |

---

## 🧪 Local Development

### ✅ 1. Clone the Repo

```bash
git clone https://github.com/your-username/research-paper-summarizer.git
cd research-paper-summarizer
