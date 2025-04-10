from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str, max_len: int = 300, min_len: int = 100) -> str:
    try:
        # Clean and validate text
        clean_text = text.strip().replace("\n", " ")
        if not clean_text:
            return "No readable text found in the PDF."

        # Limit input length (BART can handle ~1024 tokens)
        if len(clean_text) > 2000:
            clean_text = clean_text[:2000]

        summary = summarizer(clean_text, max_length=max_len, min_length=min_len, do_sample=False)
        return summary[0]['summary_text']
    
    except Exception as e:
        print(f"🔥 Summarization error: {e}")
        return "Error occurred during summarization."
