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

# CMD ["gunicorn", "--bind", "0.0.0.0:7000", "--statsd-host=192.168.10.20:9125", "--statsd-prefix=api", "--workers", "1", "app:app"]
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "7000", "app:app"]
