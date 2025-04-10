import streamlit as st
import requests

st.set_page_config(page_title="Research Paper Summarizer", layout="centered")

st.title("📄 Research Paper Summarizer + Podcast ")

# Upload PDF
uploaded_file = st.file_uploader("Upload a research paper PDF", type="pdf")

if uploaded_file is not None:
    with st.spinner(" Summarizing and generating audio..."):

        # Send PDF to FastAPI backend
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        response = requests.post("http://127.0.0.1:8000/upload-summary-audio", files=files)

        if response.status_code == 200:
            data = response.json()
            st.subheader(" Summary")
            st.write(data["summary"])

            audio_url = f"http://127.0.0.1:8000{data['audio_url']}"
            st.subheader(" Audio Podcast")
            st.audio(audio_url, format="audio/mp3")
        else:
            st.error("Something went wrong while processing the PDF.")
