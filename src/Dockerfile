FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN  python manage.py collectstatic --noinput
