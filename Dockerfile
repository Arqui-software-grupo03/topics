FROM node:7
FROM python:latest
ENV LANG C.UTF-8

RUN mkdir /appTopics

RUN apt-get -y update
RUN apt-get install -y python python-pip python-dev

WORKDIR /appTopics

COPY . /appTopics
RUN pip install -r /appTopics/requirements.txt

EXPOSE 8000