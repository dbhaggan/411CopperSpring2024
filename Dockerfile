FROM python:3.11

WORKDIR /usr/src/app

COPY percussatsight .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8080



CMD ["python", "percussatsight/manage.py", "runserver", "0.0.0.0:8080"]
