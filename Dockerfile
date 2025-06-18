FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# خلي السكريبت قابل للتنفيذ
RUN chmod +x /app/start.sh

# استخدم السكريبت كأمر تشغيل
CMD ["/app/start.sh"]
