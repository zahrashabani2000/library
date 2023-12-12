FROM python:3.12.0

ENV PYTHONBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY . /code

CMD python manage.py runserver 0.0.0.0:8000