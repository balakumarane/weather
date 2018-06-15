FROM ubuntu:18.04

RUN apt-get update && apt-get install -y git python-pip\
    && rm -rf /var/lib/apt/lists/*  
      
EXPOSE 8000

RUN mkdir /weather

WORKDIR /weather

ADD . .

ENV DJANGO_SETTINGS_MODULE weather.production

RUN pip install -r requirements.txt

CMD [ "/weather/start.sh" ]