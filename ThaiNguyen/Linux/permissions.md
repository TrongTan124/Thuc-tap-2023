## Quyền truy cập:
Quyền truy cấp được sử dụng để bảo mật hệ thống, tránh những bên không được cấp phép truy cập vào file.
Có 3 loại quyền truy cập:
1. Đọc: cho phép người dùng đọc thông tin trên file
2. viết: cho phép người dùng sửa đổi thông tin trên file
3. thực thi:cho phép người dùng chạy file(ví dụ file .py)
## 3 lớp người dùng:
Có 3 lớp người dùng chính để kiểm soát các nhóm quyền truy cập khác nhau.
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

2. chown: thay đổi quyền sở hữu của 1 file, dùng syntax như sau:
```
chown owner_name file_name
```
3. setuid:set quyền chạy của 1 file cho giống với user tạo ra file, dùng syntax như sau:
```
chmod [groupName]+[permissionName] [file name]
```
+ setuid:
```
chmod u+s file name
```
+ bỏ setuid:
``` 
chmod u-s filename
```
4. getuid:hiển thị user id thật của user
5. umask:hiển thị 1 hệ số theo hệ cơ số 8 thể hiện quyền truy cập của user hiện tại và có thể đổi quyền truy cập mặc định của các file hoặc thư mục user vừa tạo ra
+ cách tính umask value
- 0: no permission
- 1: only execute
- 2: only write
- 3: write and execute
- 4: only read
- 5: read and execute
- 6: read and write
- 7: read,write,execute
```
umask [value X]
```
X bao gồm 3 số, lần lượt cho owner, người trong nhóm, và những người khác
Hệ số umask được tính bằng cách như sau:
umask = 777- value X
## Nguồn tham khảo:
1. [Nguồn 1](https://www.geeksforgeeks.org/)
2. [Nguồn 2](https://www.javatpoint.com/linux-file-permissions)
