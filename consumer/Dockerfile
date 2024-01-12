FROM python:3.12.1-bookworm

WORKDIR /app

COPY consumer/requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt

COPY common .
COPY consumer .

CMD ["python3", "__main__.py"]
