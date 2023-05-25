## Tiến trình
1. Foreground: chạy bằng cách nhận input từ bàn phím và hiển thị ouput ở trên terminal
2. Background: chạy khi không có input từ bàn phím
### các loại tiến trình:
- tiến trình mẹ và con: tiến trình con được chạy từ tiến trình mẹ
- tiến trình orphan: xuất hiện khi tiến trình mẹ bị khử trước tiến trình con
- tiến trình zombie: tiến trình bị khử nhưng khi chạy ps vẫn hiển thị tiến trình với trạng thái zombie
- tiến trình daemon: background process chạy với quyền truy cập root
## Lệnh tương tác:
1. ps: hiển thị các tiến trình và trạng thái của các tiến trình
```
process [options] 
```
process options:
-a:hiển thị process không liên quan đến terminal
-T : tất cả các process liên quan đến terminal
-A hoặc -e: viết thông tin cho tất cả process
-d : hiển thông tin cho tất cả process ngoại trừ session leader
-r: tất cả process đang chạy
-x: tất cả process được sở hữu bởi người dùng hiện tại
-ef: hiển thị các process đang chạy
-u <USERNAME>: hiển thị process của một người dùng nhất định
-p PID: hiển thị process với processID nhất định
-C command: hiển thị process với command chỉ định
2. top: hiển thị trạng thái chạy của tất cả các tiến trình trên hệ điều hành và cập nhật trạng thái liên tục
```
top [options]
```
options:
- n X: chạy cho đến vòng lặp thứ X
- u username: hiển thị tiến trình của một username nhất định
- c: bắt đầu top với tiến trình bị đóng gần nhất
- d X: đặt thời gian X ( hệ số X tính theo giây) trước khi terminal được cập nhật
Khi top đang chạy, có thể tiến hành bấm nút như sau:
- P: sort theo cột CPU
- M: sort theo cột memory
- N: sort theo cột PID
- T: sort theo cột Time
- u: hiển thị cho 1 user
- l: chỉ hiện thị task đang chạy
- n rồi đánh số: hiển thị một số dòng nhất định
- k: đóng một process theo Process ID
3. kill: dùng để dừng chạy tiến trình
Option:
+ 
hiển thị trang có nhiều loại signals khác nhau có thể được sử dụng
```
kill -l
```
+ 
hủy một process theo process ID
```
kill [pid]
```
+ 
hủy process theo tên của process 
```
killall [signal number] [process name]
```


4. nice -N: khởi động process mới với độ ưu tiên được chỉ định( số N)
```
nice -N [process name]
```
5. renice: thay đổi độ ưu tiên của một process đang chạy
```
renice -N [process name]
```
flag của nice và renice:
- u username: thay đổi độ ưu tiên của một user
- g groupname: thay đổi độ ưu tiên của một group
## Nguồn tham khảo:
1. [Nguồn 1](https://hoclaptrinh.vn/tutorial/hoc-unix/quan-ly-tien-trinh-trong-unix-linux)
2. [Nguồn 2](https://www.hostinger.vn/huong-dan/cach-kill-proccess-linux)

