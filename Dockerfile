FROM python:3.8.10

RUN mkdir -p /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -U pip
RUN pip install -r /usr/src/app/requirements.txt
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -e .
CMD ["make"]

