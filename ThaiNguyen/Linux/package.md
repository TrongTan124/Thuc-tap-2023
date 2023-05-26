## Packages
Packages là 1 file nén bao gồm các file chứa các thông tin cần thiết để cho 1 phần mềm hoạt động. 
## Repository
- repositories là một tập hợp các mục bao gồm nhiều phần mềm và package khác nhau được cài đặt trên hệ thống
### Lệnh tương tác:
1. yum: dùng để quản lý các packages cho một số hệ điều hành linux ví dụ như red hat,có các tính năng như tải, cài đặt, xóa package,vv..
2. rpm:
- dùng để quản lý các RPM package
- RPM package manager là 1 phần mềm để cài đặt, xóa và quản lý các package trong linux
cài đặt rpm package
```
rpm [flag] [package name]
```
flag:
- i: install
- U: upgrade
- F : freshen(upgrade nhưng cho các package mà version hiện tại là version cũ)
- e: xóa package

3. dnf: 1 phần mềm quản lý package trên fedora linux
4. apt-get: dùng để quản lý package từ command-line 
```
apt-get [options] [command] [package]
```
options:
- y: yes cho tất cả các confirmation request khi cài package
-assume-no: no cho tất cả các confirmation request khi cài package
- d: tải package nhưng không cài đặt
- f: sửa lỗi dependencies trong quá trình cài package
- m: ignore missing packages
- q: không hiển thị lỗi hay cảnh báo
- reinstall: cài lại
commands:
- update
- upgrade
- install
- reinstall
- remove
- purge: xóa package và configuration files
- check: kiểm tra package và tìm broken dependencies
- source:tải về source code của package
 
## Nguồn tham khảo:
1. [Nguồn 1](https://www.geeksforgeeks.org/)
2. [Nguồn 2](https://phoenixnap.com/)
3. [Nguồn 3](https://access.redhat.com/)
