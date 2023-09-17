# pull official base image
FROM ubuntu:22.04

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
#RUN apk add g++ gcc
RUN apt update && apt install python3-pip -y
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
#RUN apk add g++ build-base python3-dev
RUN pip install opentelemetry-sdk
RUN pip install opentelemetry-instrumentation-django
RUN pip install requests
RUN pip install opentelemetry-exporter-otlp
RUN pip install opentelemetry-distro
RUN pip install opentelemetry-instrumentation
RUN opentelemetry-bootstrap -a install

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN pip install gunicorn

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
