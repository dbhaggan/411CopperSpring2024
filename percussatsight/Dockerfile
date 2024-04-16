FROM python:3.11

RUN apt install bash \ timidity \ alsa-base

WORKDIR /usr/src/app

COPY requirements.txt .
COPY startup.sh .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 3306
EXPOSE 8080

COPY . .

ENTRYPOINT "./startup.sh"
