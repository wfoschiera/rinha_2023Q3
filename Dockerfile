FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install build-essential -y
RUN pip install --upgrade pip
RUN pip install pip-tools

RUN mkdir -p /setup

COPY ./requirements.in /setup
COPY ./requirements.txt /setup

RUN pip install -r /setup/requirements.txt

EXPOSE 8080

# CMD python wsgi.py