#!/bin/sh

# طباعة قيمة البورت (للتأكد من أنه متعرف)
echo "🚀 Running on port ${PORT:-8080}"

# تشغيل التطبيق
uvicorn main:app --host 0.0.0.0 --port=${PORT:-8080}
