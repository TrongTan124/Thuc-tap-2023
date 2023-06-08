# Sử dụng image Python chứa Flask
FROM python:3.9-12

# Thiết lập biến môi trường
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Cài đặt các dependencies
WORKDIR /docker

COPY ./python/flask_mysql /docker/flask_mysql

WORKDIR /docker/flask_mysql

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Sao chép các file ứng dụng vào image
COPY . .

# Cài đặt MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Thiết lập và khởi chạy MySQL
ENV MYSQL_ROOT_PASSWORD 123
ENV MYSQL_DATABASE book_store
ENV MYSQL_USER hidro
ENV MYSQL_PASSWORD 123

# Chạy script khởi tạo database
COPY init.sql /docker-entrypoint-initdb.d/

# Mở cổng cho Flask
EXPOSE 5000

# Chạy ứng dụng Flask
CMD ["flask", "run"]