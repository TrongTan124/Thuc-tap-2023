## 3 loại người dùng:
1. Root: có quyền điều khiển tuyệt đối với hệ điều hành
2. Tài khoản hệ thống: tài khoản cần cho các hoạt động riêng như tài khoản mail
3. Tài khoản người dùng cá nhân: cho phép người dùng tương tác với hệ thống tuy nhiên có sự giới hạn về quyền truy cập
## Lệnh tương tác:
1. useradd:thêm người dùng vào hệ thống
+ Flags của useradd và tính năng của flag:
- b: sửa home directory
- g: chuyển đổi user group
- s: thay đổi shell mặc định /bin/bash với một shell mặc định khác
- e: điều chỉnh thời hạn để khóa tài khoản người dùng
- f: đặt số ngày trước khi tài khoản bị khóa và password hết hạn
2. groupadd:cho nhiều người dùng vào một nhóm để dễ kiểm soát quyền truy cập
```
groupadd [group name]
```
3. paswd:thay đổi mật khẩu của các tài khoản của người dùng
```
passwd[options] username
```
options :
- d: xóa password
- e: khiến cho password tài khoản hết hạn
- i D: số D là số ngày cho đến khi tài khoản bị vô hiệu hóa sau khi pasword hết hạn
- l: khóa password
- n N_Days: đặt số ngày trước khi người dùng có thể đổi password
- u : mở khóa password
- w X: đặt số ngày trước khi pasword hết hạn để bật cảnh báo
- x X: đặt số ngày tối đa để password còn hiệu lực
4. usermod:thay đổi thông tin về một user ví dụ home directory, login name,id
```
usermod [option] [command] [username]
```
option:
- -c: add comment
- -d : change home directory
- -e: change expiry date
- -g: change group
- -l: change user login name
- -L: lock user
- -U: unlock user
- -p: set up password for user
- -s: set up shell for user
5. userdel:xóa tài khoản của 1 user
```
userdel [options] login
```
options:
+ -f : force removal
+ -r : delete home directory along with user
+ -h: display help message and exit

## Nguồn tham khảo:
1. [Nguồn 1](https://www.geeksforgeeks.org/)
2. [Nguồn 2](https://www.makeuseof.com/user-management-linux-guide/)
