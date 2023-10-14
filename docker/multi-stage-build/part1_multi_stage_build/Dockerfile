FROM python:3.11-slim as build-env

RUN pip3 install --no-cache --upgrade pip setuptools

COPY helloworld /app/helloworld
RUN cd /app/helloworld && pip install .

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt && cp $(which uvicorn) /app

FROM python:3.11-slim

USER 1001

COPY --chown=1001:1001 server.py /app/server.py
COPY --from=build-env /app/uvicorn /app/uvicorn
COPY --chown=1001:1001 --from=build-env /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

WORKDIR /app

CMD ["./uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]