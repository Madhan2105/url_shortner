FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /url_shortner
WORKDIR /url_shortner
COPY . /url_shortner/
RUN pip install -r requiremests.txt