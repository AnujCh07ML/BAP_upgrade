# ==========================================
# Base Image
# ==========================================
FROM python:3.12-slim

# ==========================================
# Environment Variables
# ==========================================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ==========================================
# Working Directory
# ==========================================
WORKDIR /app

# ==========================================
# Install Dependencies
# ==========================================
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ==========================================
# Copy Application
# ==========================================
COPY api ./api
COPY src ./src
COPY models/final ./models/final

COPY config.yaml .
COPY setup.py .

# ==========================================
# FastAPI Port
# ==========================================
EXPOSE 8000

# ==========================================
# Start FastAPI
# ==========================================
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]