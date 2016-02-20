FROM python:2.7-alpine

COPY . /tmp/package
RUN pip install /tmp/package[worker]
RUN rm -rf /tmp/package

