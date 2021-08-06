FROM python:3.8

WORKDIR /

RUN apt update
RUN apt-get -y install libsndfile1
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
COPY . /
