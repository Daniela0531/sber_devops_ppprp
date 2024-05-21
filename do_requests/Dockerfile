FROM ubuntu:20.04

WORKDIR /request

RUN set -xe \
    && apt-get -y update \
    && apt-get -y install python3-pip python3

COPY req.txt .

RUN pip install -r req.txt  \
    && chown -R 1001:0 /request \
    && chmod -R g=u /request

COPY python_write_to_file.py .

USER 1001

CMD [ "python", "python_write_to_file.py" ]
