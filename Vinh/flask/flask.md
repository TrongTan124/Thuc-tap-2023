# Khá niệm REST API (Representational State Transfer API):

REST (Representational State Transfer) là một kiến trúc dựa trên giao thức HTTP và được sử dụng để thiết kế các hệ thống phân tán và giao tiếp giữa các thành phần của hệ thống. RESTful API là một tập hợp các quy tắc và hướng dẫn để xây dựng các dịch vụ web dựa trên nguyên tắc của REST.

RESTful API sử dụng các phương thức HTTP như GET, POST, PUT, DELETE để thực hiện các hoạt động trên các tài nguyên (resources) qua URL. Nó cho phép các ứng dụng giao tiếp và trao đổi dữ liệu với nhau một cách đơn giản và tiêu chuẩn.

## Các tool hỗ trợ thiết kế API design:

### Swagger/OpenAPI:

Là một công cụ mạnh mẽ để thiết kế và tài liệu hóa RESTful API. Nó cung cấp một cách tiêu chuẩn để mô tả các endpoint, các tham số, và các phương thức của API. Swagger/OpenAPI cho phép tạo tài liệu API tự động và thử nghiệm API.

### Postman:

Là một công cụ phổ biến để thử nghiệm và kiểm tra API. Nó cung cấp một giao diện đồ họa cho phép bạn gửi các yêu cầu HTTP và nhận các phản hồi từ API. Bạn có thể tạo các bộ kiểm tra (test suite) để đảm bảo tính chính xác và hiệu suất của API.

## Flask framework:

Flask là một framework web nhẹ, linh hoạt và dễ sử dụng được xây dựng bằng ngôn ngữ Python. Nó giúp xây dựng các ứng dụng web nhanh chóng và dễ dàng.

### Tính ứng dụng của Flask:

- Flask được sử dụng rộng rãi trong phát triển các ứng dụng web nhỏ và trung bình.
- Nó cho phép xây dựng các ứng dụng web tĩnh, động, RESTful API, và cả các ứng dụng web phức tạp hơn.
- Flask có cấu trúc đơn giản và ít phức tạp, dễ học và dễ triển khai.
- Nó hỗ trợ các extension mạnh mẽ như Flask-SQLAlchemy, Flask-RESTful, Flask-JWT để xử lý các tác vụ phổ biến như lưu trữ dữ liệu, xây dựng API, xác thực và ủy quyền.

### Hạn chế của Flask:

- Flask là một framework nhỏ và linh hoạt, không cung cấp một số tính năng nâng cao có sẵn trong các framework lớn hơn như Django.
- Vì sự đơn giản của Flask, việc phát triển và quản lý các ứng dụng lớn và phức tạp có thể đòi hỏi sự quản lý mã nguồn tốt và hiểu rõ về cách tổ chức dự án.

## Thiết kế và khởi tạo REST API đơn giản bằng Flask và cách kiểm tra API:

Để thiết kế và khởi tạo REST API đơn giản bằng Flask, bạn có thể tuân thủ các nguyên tắc thiết kế RESTful API và sử dụng Flask để triển khai các endpoint của API. Dưới đây là một ví dụ:

Import Flask và tạo ứng dụng Flask:

```python
from flask import Flask
app = Flask(__name__)
```
