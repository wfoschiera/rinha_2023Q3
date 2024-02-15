FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install build-essential -y

RUN mkdir -p /setup

COPY ./requirements.txt /setup

RUN pip install /setup/requirements.txt

EXPOSE 9999

