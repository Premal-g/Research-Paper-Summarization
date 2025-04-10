# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# ⚠️ SKIP pip upgrade to avoid timeout
# RUN pip install --upgrade pip  ❌ remove this

# Install Python dependencies with reliable mirror
RUN pip install -r requirements.txt -i https://pypi.org/simple --timeout=100

# Expose FastAPI and Streamlit ports
EXPOSE 8000
EXPOSE 8501

# Start both FastAPI and Streamlit
CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py --server.port 8501 --server.enableCORS false"]
