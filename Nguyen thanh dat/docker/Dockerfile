FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=123

# Create a new database and user
ENV MYSQL_DATABASE=book_store
ENV MYSQL_USER=hidro
ENV MYSQL_PORT = 8080:3306
ENV MYSQL_PASSWORD=123

COPY init.sql /docker-entrypoint-initdb.d/init.sql

# Use Python image containing Flask
FROM python:3.9



# Cài đặt các dependencies
WORKDIR /docker

COPY /flask_mysql /docker/flask_mysql

WORKDIR /docker/flask_mysql



# Thiết lập biến môi trường
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0


COPY flask_mysql/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



ENV DB_URL 'mysql://root:123@172.20.64.1:8080/book_store'

COPY . .

EXPOSE 5000

RUN flask db init
RUN flask db migrate -m "version 1.0"
RUN flask db upgrade

CMD [ "python", "app.py" ]



