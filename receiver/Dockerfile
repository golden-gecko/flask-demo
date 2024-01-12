FROM python:3.12.1-bookworm

WORKDIR /app

COPY receiver/requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt

COPY common .
COPY receiver .

EXPOSE 7000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "7000", "app:app"]
