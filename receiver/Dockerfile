FROM python:3.9.0-alpine3.12

WORKDIR /usr/local/app

RUN apk add \
    curl

COPY receiver/requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt

COPY common .
COPY receiver .

EXPOSE 7000

ENTRYPOINT ["gunicorn"]

CMD ["--bind", "0.0.0.0:7000", "--statsd-host=192.168.10.20:9125", "--statsd-prefix=api", "--workers", "1", "app:app"]
