FROM  python:3.7
LABEL MAINTAINER Rodney Osodo
ENV PYTHONUNBUFFERED 1
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD secret
ENV POSTGRES_DB weather_api
ENV DB_PORT 1001
ENV APP_SECRET_KEY=qwerty12345
RUN mkdir -p /app
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
EXPOSE 5000
RUN apt-get update && apt-get install -y python-psycopg2 && pip3 install psycopg2 
COPY . /app
RUN rm -rf migrations
# RUN python3 manage.py db init && python3 manage.py db migrate && python3 manage.py db upgrade
#python3 app.py
