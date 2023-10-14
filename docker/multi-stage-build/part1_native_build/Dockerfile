FROM python:3.11-slim

COPY requirements.txt /app/requirements.txt
COPY server.py /app/server.py

WORKDIR /app

RUN python -m pip install -r requirements.txt

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]