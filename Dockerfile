FROM python:3.11-slim

WORKDIR /app

COPY smartcomp/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY smartcomp/ .

EXPOSE 8501

CMD ["streamlit", "run", "smartcomp_app.py", "--server.port", "8501", "--server.address", "0.0.0.0", "--server.headless", "true"]
