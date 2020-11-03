FROM python:3.9.0

WORKDIR /usr/local/app

COPY requirements.txt .

RUN pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement requirements.txt
