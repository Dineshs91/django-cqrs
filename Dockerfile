FROM phusion/baseimage

RUN apt-get update
RUN apt-get install -y python3 python-pip python3-dev libpq-dev
RUN apt-get install -y libssl-dev
RUN apt-get install build-essential

ADD ./ /home/src/cqrs

WORKDIR /home/src/cqrs

RUN pip install -r requirements.txt

WORKDIR /home/src/cqrs/blog

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
