FROM phusion/baseimage

RUN apt-get update
RUN apt-get install git
RUN apt-get install -y python3 python-pip python3-dev libpq-dev
RUN apt-get install -y libssl-dev
RUN apt-get install build-essential

ADD ./ /app/

WORKDIR /app/

RUN pip install -r requirements.txt

CMD ["python", "blog/manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
