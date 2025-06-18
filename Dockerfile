FROM python:3.11-slim

# تثبيت ffmpeg وأساسيات النظام
RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    apt-get clean

# تحديد مجلد العمل
WORKDIR /app

# نسخ ملفات المشروع
COPY . /app

# تثبيت مكتبات البايثون
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Railway بيوفر PORT تلقائيًا في البيئة
ENV PORT=8080

# ✅ هذا السطر بيشتغل محليًا وعلى Railway
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
