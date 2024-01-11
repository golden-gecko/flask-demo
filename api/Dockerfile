FROM python:3.12.1-bookworm

WORKDIR /app

COPY api/requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt

COPY api .
COPY common .

EXPOSE 4000

# CMD ["gunicorn", "--bind", "0.0.0.0:4000", "--statsd-host=192.168.10.20:9125", "--statsd-prefix=api", "--workers", "1", "app:app"]
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "4000", "app:app"]
