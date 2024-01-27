FROM python:3.11 as requirements

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.11

WORKDIR /code

COPY --from=requirements /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip uninstall pycurl -y

ENV PYCURL_SSL_LIBRARY=openssl \
    OPENSSL_DIR=/usr/local/opt/openssl
RUN pip install pycurl

COPY app/. /code/app

CMD ["celery", "--app", "app.worker.task.app", "worker", "--concurrency", "1"]
