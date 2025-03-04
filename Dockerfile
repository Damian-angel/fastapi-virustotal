
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-multipart

COPY . .

EXPOSE 8000

ENV VIRUSTOTAL_API_KEY=${VIRUSTOTAL_API_KEY}

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]