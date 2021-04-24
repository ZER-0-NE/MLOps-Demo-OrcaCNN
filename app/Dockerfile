FROM python:3.8
WORKDIR /app

ADD . /app

RUN apt update && apt upgrade -y && apt install -y python3 python3-pip  
RUN pip3 --no-cache-dir install --default-timeout=100 -r requirements.txt

CMD ["uwsgi", "app.ini"]