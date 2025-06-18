FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PORT=8080

# ✅ هنا التعديل
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
