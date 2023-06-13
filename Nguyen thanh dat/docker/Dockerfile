# Use Python image containing Flask
FROM python:3.9



# Cài đặt các dependencies
WORKDIR /docker

COPY /flask_mysql /docker/flask_mysql

WORKDIR /docker/flask_mysql

RUN apt-get update && apt-get install -y default-mysql-client

# Thiết lập biến môi trường
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Cài đặt MySQL client
ENV MYSQL_ROOT_PASSWORD 123
ENV MYSQL_DATABASE book_store
ENV MYSQL_USER hidro
ENV MYSQL_PASSWORD 123

# Kết nối với database 
ENV DB_URL 'mysql://root:123@172.20.64.1:8080/book_store'

# Sao chép các file ứng dụng vào image
COPY . .

# Cài đặt các dependencies  
COPY flask_mysql/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng cho Flask
EXPOSE 5000


CMD  ["python" "run"]


