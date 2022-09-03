FROM python:3
ENV  PYTHONUNBUFFERED 1 
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
# ARG FLAKE8_VERSION=3.0.4
# RUN pip install flake8==$FLAKE8_VERSION
# RUN flake8 --version