FROM python:2.7-alpine

pip install pip --upgrade

VOLUME /code
WORKDIR /code