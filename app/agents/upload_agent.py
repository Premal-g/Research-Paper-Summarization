import fitz  # PyMuPDF

def handle_pdf_upload(file) -> str:
    try:
        contents = file.file.read()
        with open("temp_uploaded_file.pdf", "wb") as f:
            f.write(contents)

        doc = fitz.open("temp_uploaded_file.pdf")
        full_text = ""
        for page in doc:
            full_text += page.get_text()

        return full_text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        raise e
