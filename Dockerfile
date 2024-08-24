FROM ubuntu:22.04

# installing Python
RUN apt-get update && apt-get install -y python3-pip

ENV PYTHONUNBUFFERED=1
WORKDIR /tone_app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .