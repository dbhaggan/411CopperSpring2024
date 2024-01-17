FROM python:3.11.0

COPY ./requirements.txt ./

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver"]
