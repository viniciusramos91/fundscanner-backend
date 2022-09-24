FROM python:3.9.13-alpine3.16

RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev postgresql-libs ip6tables ufw

RUN addgroup -S fundscanner && adduser -S fundscanner -G fundscanner

ENV PYTHONBUFFERED 1
ENV PATH="/usr/local:$PATH"

RUN mkdir /fundscanner
WORKDIR /fundscanner
COPY . /fundscanner/

RUN chown -R fundscanner:fundscanner /fundscanner

RUN pip install -r requirements.txt

USER fundscanner

EXPOSE 8080

CMD ["gunicorn", "--bind=0.0.0.0:8080", "core.wsgi", "--workers=4", "--threads=2"]