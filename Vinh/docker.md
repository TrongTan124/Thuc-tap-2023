## Docker là một nền tảng mã nguồn mở cho việc tạo, triển khai và quản lý các ứng dụng trong một môi trường được cô lập gọi là container. Các container là các môi trường chứa mọi thứ cần thiết để chạy một ứng dụng, bao gồm mã nguồn, thư viện, công cụ hệ điều hành và các phụ thuộc khác. Docker cho phép bạn đóng gói ứng dụng vào các container và chạy chúng trên bất kỳ môi trường nào có cài đặt Docker, đảm bảo tính nhất quán và di động.

## Lợi ích của Docker:

1. Đơn giản hóa triển khai ứng dụng: Docker cho phép bạn đóng gói ứng dụng cùng với các phụ thuộc của nó vào một container duy nhất, giúp giảm thiểu các vấn đề liên quan đến việc cấu hình môi trường.
2 . Đảm bảo tính nhất quán: Docker container đảm bảo rằng ứng dụng sẽ chạy giống nhau trên mọi môi trường, từ máy cục bộ đến máy chủ sản phẩm.
3. Tiết kiệm tài nguyên: Các container chạy trên cùng một hạ tầng chia sẻ, do đó tiết kiệm tài nguyên máy chủ và giúp tăng hiệu suất.
4. Dễ dàng mở rộng: Docker giúp quản lý việc mở rộng ứng dụng, cho phép bạn triển khai và khởi chạy nhiều container cùng một lúc để đáp ứng lưu lượng truy cập tăng cao.
5. Sự khác biệt giữa Docker và chạy trên máy host hoặc sử dụng máy ảo (virtual machine) container:

## Chạy trên máy host: Ứng dụng chạy trực tiếp trên hệ điều hành của máy chủ mà không có cơ chế cô lập, dẫn đến sự phụ thuộc và xung đột giữa các ứng dụng.

Sử dụng máy ảo (virtual machine) container: Mỗi ứng dụng được chạy trong một máy ảo độc lập với tài nguyên riêng, tuy nhiên, việc triển khai và quản lý các máy ảo tốn kém về tài nguyên và thời gian.
## Các khái niệm cơ bản trong Docker:

1. Docker image: Một Docker image là một gói đóng gói có thể thực thi một ứng dụng hoặc một tập hợp các ứng dụng và các phụ thuộc của chúng. Image chứa mã nguồn, thư viện, tệp cấu hình và môi trường để chạy ứng dụng.

2. Image layer: Docker image được tạo thành từ các image layer. Mỗi lớp đại diện cho một phần cụ thể của image. Các lớp này có thể được sử dụng lại bởi các image khác, giúp tiết kiệm dung lượng đĩa và tăng tốc quá trình tải và xây dựng.

3. Docker container: Một Docker container là một phiên bản thực thi của một Docker image. Container chứa tất cả những gì cần thiết để chạy ứng dụng, bao gồm cả mã nguồn, thư viện và các tài nguyên khác.

### Quản lý Docker image và container command:

docker images: Liệt kê các image đã tải xuống.
docker ps: Liệt kê các container đang chạy.
docker stop <container_id>: Dừng container đang chạy.
docker start <container_id>: Khởi động container đã dừng.
docker rm <container_id>: Xóa container.
docker rmi <image_id>: Xóa image.

### Volume:

- Anonymous volume: Là một volume được tạo động và liên kết với container, không có tên giao diện. Khi container bị xóa, volume cũng sẽ bị xóa.
Mounted volume: Là một volume được tạo ra và liên kết với container, nhưng có thể tồn tại ngắn hạn sau khi container bị xóa.
Remove anonymous volume: Xóa các volume ẩn danh không được sử dụng bởi bất kỳ container nào.
Dockerignore: Một file .dockerignore cho phép bạn xác định các tệp và thư mục mà Docker nên bỏ qua khi đóng gói image.

### Biến môi trường và tệp .env: Docker cho phép bạn cấu hình biến môi trường trong container bằng cách sử dụng biến môi trường hoặc tệp .env.

### Dockerfile là một tệp văn bản có chứa các hướng dẫn để xây dựng một Docker image. Nó chứa một danh sách các chỉ thị cho việc sao chép các tệp, cài đặt các phụ thuộc, thiết lập biến môi trường và nhiều hơn nữa. Các chỉ thị trong Dockerfile bao gồm:

1. FROM: Xác định image cơ sở mà Docker image mới sẽ dựa trên.
2. RUN: Thực thi một lệnh trong quá trình xây dựng image.
3. COPY hoặc ADD: Sao chép tệp từ máy host vào image.
4. WORKDIR: Thiết lập thư mục làm việc mặc định cho các lệnh tiếp theo.
5. EXPOSE: Khai báo các cổng mà container lắng nghe.
6. CMD hoặc ENTRYPOINT: Chỉ định lệnh mặc định sẽ được thực thi khi container được khởi chạy.
7. Để chạy một Flask app trong một container, bạn cần tạo một Docker image và chạy container từ image đó. Bước chính bao gồm:


Tạo một Dockerfile trong thư mục của ứng dụng Flask:

```python
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

```python
#Xây dựng Docker image từ Dockerfile:
=
docker build -t flask-app .
```

Chạy container từ Docker image:

```python
docker run -p 5000:5000 flask-app
Sau đó, ứng dụng Flask sẽ chạy trong container và có thể được truy cập qua cổng 5000 trên máy host.
```
