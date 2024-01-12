FROM python:3.12.1-bookworm

WORKDIR /app

COPY sender/requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt

COPY common .
COPY sender .

CMD ["python3", "__main__.py"]
