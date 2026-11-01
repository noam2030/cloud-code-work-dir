# Use the official lightweight Python image.
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose default Cloud Run port
EXPOSE 8080

# Start Uvicorn binding to Cloud Run's PORT (default 8080)
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]
