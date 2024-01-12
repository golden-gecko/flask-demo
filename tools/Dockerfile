FROM python:3.12.1-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt
