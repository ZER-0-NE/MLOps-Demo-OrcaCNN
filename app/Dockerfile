FROM tensorflow/tensorflow:2.1.0

WORKDIR /app

ADD . /app

RUN apt-get -y install python3-pip
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]