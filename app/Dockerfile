FROM ubuntu:20.04

EXPOSE 3000

WORKDIR /app

RUN set -xe \
    && apt-get -y update \
    && apt-get -y install python3-pip python3

COPY req.txt /app

RUN pip install -r req.txt  \
    && chown -R 1001:0 /app \
    && chmod -R g=u /app

COPY queries.py /app

USER 1001

CMD [ "python3", "queries.py" ]
