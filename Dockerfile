FROM python:3.10-slim

WORKDIR /app

RUN apt-get clean \
  && apt-get -y update

RUN  apt-get -y install python3-enchant \
  && apt-get -y install python3-dev \
  && apt-get -y install build-essential \
  && apt-get -y install nginx

RUN pip3 install --upgrade pip

COPY . .

RUN pip3 install -r requirements.txt

COPY nginx.conf /etc/nginx

RUN chmod +x ./start.sh

CMD ["./start.sh"]
