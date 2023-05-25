## Quyền truy cập:
1. Đọc: cho phép người dùng đọc thông tin trên file
2. viết: cho phép người dùng sửa đổi thông tin trên file
3. thực thi:cho phép người dùng chạy file(ví dụ file .py)
## 3 lớp người dùng:
1. Chủ sở hữu file
2. Các thành viên trong nhóm
3. Các người dùng khác
## Các lệnh
1. chmod: thay đổi quyền truy cập của 1 file
```
chmod [reference] [operator] [permission]
```
reference: 
- u: owner
- g: group
- o:others
- a: all
operator:
+: add permission
-: remove permission
= :specified value
permission:
r: read
w: write
x: execute

2. chown: thay đổi quyền sở hữu của 1 file
```
chown owner_name file_name
```
3. setuid:đổi setuid bit, đại diện cho quyền chạy 1 file của user
4. getuid:hiển thị user id thật của user
5. umask:hiển thị 1 hệ số thể hiện quyền truy cập của user hiện tại và có thể đổi quyền truy cập mặc định của các file hoặc thư mục user vừa tạo ra

## Nguồn tham khảo:
1. [Nguồn](https://www.geeksforgeeks.org/)
