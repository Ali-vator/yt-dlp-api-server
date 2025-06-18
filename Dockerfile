FROM python:3.11-slim

# تثبيت ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    apt-get clean

# إعداد مجلد العمل
WORKDIR /app
COPY . /app

# تثبيت المكتبات
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Railway يستخدم متغير PORT
ENV PORT=8080

# ✅ هذا السطر مهم – بدون أقواس
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
