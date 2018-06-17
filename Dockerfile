FROM ubuntu:18.04

RUN apt-get update && apt-get install -y git python-pip netcat\
    && rm -rf /var/lib/apt/lists/*  
      
EXPOSE 8000

RUN mkdir /weather

WORKDIR /weather

ADD . .

RUN pip install -r requirements.txt

CMD [ "/weather/start.sh" ]