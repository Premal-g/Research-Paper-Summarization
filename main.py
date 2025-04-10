import os
import sys
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.responses import FileResponse

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Ensure app/ is importable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import agents
from app.agents.upload_agent import handle_pdf_upload
from app.agents.summarize_agent import summarize_text
from app.agents.audio_agent import text_to_audio  # 🎙️ Audio generation

# Initialize FastAPI app
app = FastAPI(
    title="Research Paper Summarizer",
    description="Upload a research paper PDF and get a concise summary and audio podcast.",
    version="1.0"
)

# ✅ Health check endpoint
@app.get("/")
def root():
    return {"message": "🚀 Research Paper Summarizer API is running!"}

# ✅ Upload and summarize a PDF
@app.post("/upload-and-summarize")
async def upload_and_summarize(file: UploadFile = File(...)):
    try:
        content = handle_pdf_upload(file)
        summary = summarize_text(content)
        return {"summary": summary}
    except Exception as e:
        logging.error(f"🔥 Error in /upload-and-summarize: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Something went wrong while processing the PDF.")

# ✅ Generate podcast/audio from summary text
@app.post("/generate-audio")
def generate_audio(summary_text: str = Query(..., description="Summary text to convert to audio.")):
    try:
        audio_path = text_to_audio(summary_text)
        if not audio_path:
            raise HTTPException(status_code=500, detail="Audio generation failed.")
        return FileResponse(
            path=audio_path,
            media_type="audio/mpeg",
            filename="summary.mp3"
        )
    except Exception as e:
        logging.error(f"🔥 Error in /generate-audio: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Upload PDF → Summarize → Generate Audio (Combined)
@app.post("/upload-summary-audio")
async def upload_summary_audio(file: UploadFile = File(...)):
    try:
        # Step 1: Extract text from PDF
        content = handle_pdf_upload(file)

        # Step 2: Summarize
        summary = summarize_text(content)

        # Step 3: Generate Audio
        audio_path = text_to_audio(summary)
        if not audio_path:
            raise HTTPException(status_code=500, detail="Audio generation failed.")

        # Step 4: Return both summary and downloadable URL
        audio_filename = os.path.basename(audio_path)
        return {
            "summary": summary,
            "audio_url": f"/get-audio?filename={audio_filename}"
        }

    except Exception as e:
        logging.error(f"🔥 Error in /upload-summary-audio: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Something went wrong while processing the PDF.")

# ✅ Serve audio file from its filename
@app.get("/get-audio")
def get_audio(filename: str):
    filepath = os.path.join("audio", filename)
    if os.path.exists(filepath):
        return FileResponse(path=filepath, media_type="audio/mpeg", filename=filename)
    else:
        raise HTTPException(status_code=404, detail="Audio file not found.")
