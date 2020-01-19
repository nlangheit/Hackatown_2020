FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc linux-headers musl-dev

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python", "app.py"]
