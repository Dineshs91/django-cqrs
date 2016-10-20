FROM phusion/baseimage

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3 python-pip python3-dev libpq-dev postgresql-client
RUN apt-get install -y libssl-dev
RUN apt-get install build-essential

ADD ./ /app/

WORKDIR /app/

RUN pip install -r requirements.txt
