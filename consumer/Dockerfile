FROM python:3.9.0-alpine3.12

WORKDIR /usr/local/app

COPY consumer/requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt

COPY common .
COPY consumer .

ENTRYPOINT ["python3"]

CMD ["__main__.py"]
