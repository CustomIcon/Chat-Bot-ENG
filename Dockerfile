FROM python:3.8.4-slim-buster

ENV PIP_NO_CACHE_DIR 1

RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

WORKDIR /app/

# Pypi package Repo upgrade
RUN pip3 install --upgrade pip setuptools


# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt


COPY . .

# Starting Worker
CMD ["python3","-m","chatbot"]