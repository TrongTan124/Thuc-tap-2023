# Use Python image containing Flask
FROM python:3.9

# Cài đặt các dependencies
WORKDIR /docker

COPY /flask_mysql /docker/flask_mysql

WORKDIR /docker/flask_mysql

RUN apt-get update && apt-get install -y default-mysql-client

# Sao chép các file ứng dụng vào image
COPY . .

# Cài đặt các dependencies  
COPY flask_mysql/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng cho Flask
EXPOSE 5000


CMD  flask db migrate && flask db upgrade && flask run 


