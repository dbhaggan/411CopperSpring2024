FROM python:3.11

RUN apt install bash

WORKDIR /usr/src/app

COPY requirements.txt .
COPY startup.sh .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY . .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
ENTRYPOINT "./startup.sh"
