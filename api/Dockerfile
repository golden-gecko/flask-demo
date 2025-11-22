FROM python:3.9.0-alpine3.12

WORKDIR /usr/local/app

RUN apk add \
    curl \
    gcc \
    libc-dev \
    postgresql-dev

COPY api/requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt

COPY api .
COPY common .

EXPOSE 4000

ENTRYPOINT ["gunicorn"]

CMD ["--bind", "0.0.0.0:4000", "--statsd-host=192.168.10.20:9125", "--statsd-prefix=api", "--workers", "1", "app:app"]
