# نبدأ من Python slim image
FROM python:3.11-slim

# تثبيت ffmpeg وأساسيات النظام
RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    apt-get clean

# نسخ الملفات الخاصة بالمشروع
WORKDIR /app
COPY . /app

# تثبيت مكتبات البايثون
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# فتح البورت اللي Railway بيستخدمه
ENV PORT=8080

# تشغيل التطبيق
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
