FROM ubuntu:18.04

RUN apt-get update && apt-get install -y git python3  python3-pip netcat\
    && rm -rf /var/lib/apt/lists/*  
      
RUN ln -s /usr/bin/python3 /usr/bin/python & \
    ln -s /usr/bin/pip3 /usr/bin/pip

EXPOSE 8000

RUN mkdir /weather

WORKDIR /weather

ADD . .

RUN pip install -r requirements.txt

CMD [ "/weather/start.sh" ]
