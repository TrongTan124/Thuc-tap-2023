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
2. top: hiển thị trạng thái chạy của tất cả các tiến trình trên hệ điều hành và cập nhật trạng thái liên tục
3. kill: dùng để dừng chạy tiến trình
4. nice -N: khởi động process mới với độ ưu tiên được chỉ định( số N)
## Nguồn tham khảo:
1. [Nguồn 1](https://hoclaptrinh.vn/tutorial/hoc-unix/quan-ly-tien-trinh-trong-unix-linux)

