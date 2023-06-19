# Khá niệm REST API (Representational State Transfer API):

REST (Representational State Transfer) là một kiến trúc dựa trên giao thức HTTP và được sử dụng để thiết kế các hệ thống phân tán và giao tiếp giữa các thành phần của hệ thống. RESTful API là một tập hợp các quy tắc và hướng dẫn để xây dựng các dịch vụ web dựa trên nguyên tắc của REST.

RESTful API sử dụng các phương thức HTTP như GET, POST, PUT, DELETE để thực hiện các hoạt động trên các tài nguyên (resources) qua URL. Nó cho phép các ứng dụng giao tiếp và trao đổi dữ liệu với nhau một cách đơn giản và tiêu chuẩn.

### client gửi requests, server nhận và xử lý và đưa ra output là HTTP status code to tell the client what happens to the reqs:

- 200 level: Success
- 400 level: Sth wrong with the reqs
- 500 level: sth wrong with the server level.

RESTAPI: stateless

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
app = Flask(name)

@app.route('/api/sort', methods=['POST'])
def sort_list():
data = request.json['data']
sorted_data = sorted(data)
return jsonify(sorted_data)

if name == 'main':
app.run()
```

### Để kiểm tra API, bạn có thể sử dụng công cụ như Postman để gửi yêu cầu HTTP POST tới endpoint '/api/sort' và kiểm tra kết quả trả về.

## Thiết kế và khởi tạo REST API đơn giản bằng Flask và thực hiện kiểm tra API

Để thiết kế và khởi tạo REST API đơn giản bằng Flask và thực hiện kiểm tra API, hãy thực hiện các bước sau:

### Thiết kế API để sắp xếp danh sách

Import Flask và các modules cần thiết:

```python
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/api/sort', methods=['POST'])
def sort_list():
    data = request.json['data']
    sorted_data = sorted(data)
    return jsonify(sorted_data)
if __name__ == '__main__':
    app.run()
```

## Cách test API

Bạn có thể sử dụng Postman hoặc một công cụ tương tự để gửi yêu cầu HTTP POST tới địa chỉ "http://localhost:5000/api/sort" với body là một đối tượng JSON chứa danh sách cần sắp xếp. Sau đó, bạn sẽ nhận được một phản hồi JSON chứa danh sách đã được sắp xếp.

### Làm quen với SQLAlchemy để lưu trữ data vào SQL database

Import các modules cần thiết:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) # Cấu hình Flask-SQLAlchemy với ứng dụng Flask:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Định nghĩa URI của database
db = SQLAlchemy(app)
```

```python
- Tạo model (bảng) trong database:
class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
# Tạo và cập nhật database:
# Tạo database
db.create_all()

# Cập nhật database (thêm/sửa/xóa bảng)
db.session.commit()
# Thêm bản ghi mới
bug = Bug(title='Bug 1', description='This is a bug')
db.session.add(bug)
db.session.commit()

# Lấy danh sách các bug
bugs = Bug.query.all()

# Lấy bug theo ID
bug = Bug.query.get(1)

# Cập nhật bug
bug.title = 'New title'
db.session.commit()

# Xóa bug
db.session.delete(bug)
db.session.commit()
```

## Data migration sử dụng Alembic và Flask-Migrate

Flask-Migrate là một extension của Flask-SQLAlchemy để hỗ trợ việc data migration và quản lý phiên bản database.
Alembic là một công cụ migration độc lập có thể được sử dụng với Flask-Migrate để tạo, cập nhật và quản lý phiên bản của database.

Để sử dụng Alembic và Flask-Migrate, bạn cần làm như sau:

1. Cài đặt Flask-Migrate và Alembic:
   pip install flask-migrate
   pip install alembic

2. Khởi tạo migration:

```shell
flask db init

flask db migrate -m "Create bug table"
flask db upgrade
```

## Xây dựng Flask API để quản lý bugs (Get, Create, Update, Delete)

Bạn có thể xây dựng một Flask API để quản lý bugs bằng cách sử dụng các routes và thao tác với database qua SQLAlchemy như đã mô tả ở trên. Dưới đây là một ví dụ:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugs.db'
db = SQLAlchemy(app)

class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

@app.route('/api/bugs', methods=['GET'])
def get_bugs():
    bugs = Bug.query.all()
    bug_list = []
    for bug in bugs:
        bug_list.append({
            'id': bug.id,
            'title': bug.title,
            'description': bug.description
        })
    return jsonify(bug_list)

@app.route('/api/bugs', methods=['POST'])
def create_bug():
    title = request.json['title']
    description = request.json['description']
    bug = Bug(title=title, description=description)
    db.session.add(bug)
    db.session.commit()
    return jsonify({'message': 'Bug created successfully'})

@app.route('/api/bugs/<int:bug_id>', methods=['PUT'])
def update_bug(bug_id):
    bug = Bug.query.get(bug_id)
    if not bug:
        return jsonify({'error': 'Bug not found'})
    bug.title = request.json['title']
    bug.description = request.json['description']
    db.session.commit()
    return jsonify({'message': 'Bug updated successfully'})

@app.route('/api/bugs/<int:bug_id>', methods=['DELETE'])
def delete_bug(bug_id):
    bug = Bug.query.get(bug_id)
    if not bug:
        return jsonify({'error': 'Bug not found'})
    db.session.delete(bug)
    db.session.commit()
    return jsonify({'message': 'Bug deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
```
