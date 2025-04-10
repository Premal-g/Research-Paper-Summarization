from gtts import gTTS
import os
import uuid
import logging

def text_to_audio(text: str) -> str:
    try:
        # Generate a unique filename
        filename = f"summary_{uuid.uuid4().hex}.mp3"
        output_dir = "audio"
        os.makedirs(output_dir, exist_ok=True)

        # Create full file path
        filepath = os.path.join(output_dir, filename)

        # Generate and save audio
        tts = gTTS(text)
        tts.save(filepath)

        logging.debug(f"✅ Audio saved at: {filepath}")
        return filepath
    except Exception as e:
        logging.error(f"❌ Error generating audio: {e}", exc_info=True)
        return ""
