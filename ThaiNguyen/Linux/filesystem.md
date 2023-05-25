## Cấu trúc cây thư mục 
![directory tree](./images/directory%20tree.png)

một số thư mục chính:
- root: nơi bắt đầu của tất cả các file và thư mục
- bin: chứa các chương trình của người dùng
- sbin: chứa chương trình hệ thống
- dev: các file thiết bị,ví dụ như usb
- proc: chứa thông tin về các tiến trình
- home: thư mục của người dùng
- boot: các fie để khởi động hệ điều hành
- lib: thư viện của hệ thống
- srv: chứa dữ liệu của một số dịch vụ khác
## các lệnh tương tác với thư mục
1. cd: di chuyển đến thư mục, ví dụ như sau
```
cd [Directory]
```
- di chuyển đến thư mục trước như sau:
```
cd ..
```
2. mkdir: tạo thư mục
```
mkdir [directory name]
```
3. touch: tạo file
```
touch [file name]
```
4. rmdir: xóa thư mục 
```
rmdir [directory name]
```
5. rm: xóa file
```
rm [file name]
```
6. pwd: hiển thị path của thư mục hiện tại:
+ hiển thị path của thư mục hiện tại:
```
pwd
```
+ hiển thị path của thư mục cụ thể:
```
pwd [file name] 
```
7. mv: di chuyển file từ thư mục này đến thư mục khác:
+ đổi tên file
```
mv [source file name] [destination file name]
```
8. pushd: push thư mục lên directory stack:
+ push thư mục :
```
push [file name]
```
+ push thư mục đến vị trí nhất định:
- push từ vị trí thứ n từ trên xuống:
```
pushd +N // N is a number
```
- push từ vị trí thứ n từ dưới lên:
```
pushd -N //N is a number
```
9. popd: pop thư mục từ directory stack theo thứ tự LIFO (last-in-first-out)
- syntax tương tự như pushd ở trên 
10. tree: hiển thị sơ đồ của cây thư mục
+ hiển thị sơ đồ thư mục của cả hệ thống
```
tree
```
+ hiển thị sơ đồ của 1 thư mục:
```
tree [directory name]
```
một số flag của tree:
- d : hiển thị mỗi directory
- a : in hết toàn bộ file
- f: in hết bao gồm cả path
- p: in permission
- u: in username
- g: in tên nhóm
- P pattern: hiển thị toàn bộ file tương ứng với pattern
-l pattern: không hiển thị file tương ứng với pattern
## lệnh tương tác với tập tin
1. cat:hiển thị thông tin trong file trên terminal
2. head: lấy một phần văn bản của file cho đến dòng thứ n từ trên xuống
``` 
head [option] [file]
```
Option từ những flag sau:
- n: lines
- c : bytes
- q : quiet( không hiển thị tên file khi in)
- v: verbose( có hiển thị tên file khi in)
3. tail: lấy ra một phần văn bản của file cho đến dòng thứ n từ dưới lên
syntax giống head 
4. more: mở file và hiển thị nội dung file trên terminal, nhưng không cho phép người dùng điều hướng quay lại nội dung trước đó trong file
```
more [-options] [-num] [file name]
```
hướng dẫn dùng:
+ dùng spacebar để sang trang khác
+ bấm enter để xuống từng dòng một
+ b để quay lại 1 trang
num: số dòng hiển thị trên mỗi terminal screen
các options:
- d: hiển thị hướng dẫn đi kèm
- f: không wrap những dòng dài
- p: clear màn hình rồi hiển thị text
- s: dồn nhiều dòng trống vào cùng 1 dòng
5. less: giống lệnh more, tuy nhiên more sẽ hiển thị các file trên cùng terminal được cách bởi các khoảng trống, còn less thì cho phép người dùng tùy ý điều chỉnh file nào được hiện lên trên terminal. More khi xem hết file sẽ tự động thoát ra, còn less cho phép tùy ý điều chính quay lại các file trước.
```
less [filename]
```
6. vim:mở file trên text editor vim
7. nano:mở file trên text editor nano
8. rm: xóa file hoặc thư mục
9. grep: tìm từ trong 1 file
```
grep [options] pattern [files]
```
các options bao gồm:
 - c : hiển thị số dòng nhất định tương ứng với pattern
 - h hiển thị những dòng tương ứng, nhưng không hiển thị tên file
 - i: hiển thị không kể viết thường hay hoa
 - l: hiển thị mỗi tên các file
 - n: hiển thị các dòng tương ứng và số dòng trong file
 - v: hiển thị các dòng không tương ứng với pattern
 - w: hiển thị các dòng tương ứng theo từ
 - o: hiển thị duy nhất các phần tương ứng của mỗi dòng
  
### Nguồn tham khảo:
1. [Nguồn 1](https://quantrimang.com/cong-nghe/cau-truc-cay-thu-muc-trong-linux-84056)
2. [Nguồn 2] (https://www.cyberciti.biz/)
3. [Nguồn 3](https://www.geeksforgeeks.org/)
