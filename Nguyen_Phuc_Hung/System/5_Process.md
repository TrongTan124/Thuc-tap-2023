## Tiến trình
Tiến trình (processes) được hiểu đơn giản là một chương trình đang chạy trong trong hệ điều hành. Một tiến trình có thể phân thành một hay nhiều tiến trình con khác.
## Phân loại tiến trình
### Init process
Init process là tiến trình đầu tiên được khởi động sau khi bạn lựa chọn hệ điều hành trong boot loader. Trong cây tiến trình, init process là tiến trình cha của các tiến trình khác. Init process có đặc điểm sau:
•	PID = 1
•	Không thể kill init process
### Parents process – Child process
- Trong hệ điều hành linux các tiến trình được phân thành parents process và child process. Một tiến trình khi thực hiện lệnh fork() để tạo ra một tiến trình mới thì đưọc gọi là parents process. Tiến trình mới tạo được gọi là child process.
![](https://github.com/tronghuan98hd/thuctapsinh/raw/master/HuanTT/Process/images/process01.png)
### Các trạng thái của tiến trình:
![](https://scontent.xx.fbcdn.net/v/t1.15752-9/349093842_7021897297825347_6730953259127172965_n.png?stp=dst-png_p206x206&_nc_cat=102&ccb=1-7&_nc_sid=aee45a&_nc_ohc=HX3-o8q2nYQAX_pSgbE&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRM8fFxqWHMJGsOcbExftAfPMkzcFIpKsyzL4rxkW0qQA&oe=6494FB59)

**Note**: Một parents process có thể có nhiều child process nhưng một child process chỉ có một parents process. Khi quan sát thông tin của một tiến trình, ngoài PID (Processes ID) ta cần để ý tới PPID (Parent Processes ID). Nó sẽ cho ta thông tin về parents process của tiến trình đó:
```sh
ps -ef
```
![](https://scontent.xx.fbcdn.net/v/t1.15752-9/348361898_750678766766828_7593563652029599337_n.png?stp=dst-png_s403x403&_nc_cat=106&ccb=1-7&_nc_sid=aee45a&_nc_ohc=p5iVgek87A0AX_CXNky&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRuqXxA6HIH0lw57Tk_5jpqsVHaZFCtzAD4qUPg_I30Kg&oe=6494E9CD)

 
#### Top
- top – command top là đơn giản và phổ biến nhất để hiển thị tất cả những process chiếm nhiều tài nguyên máy tính nhất.  Khi thực hiện command  top trong terminal, chúng ta sẽ thấy cửa sổ tương tự như sau:
 
- top là ứng dụng, sau khi thực hiện lệnh, một layout hiện lên và danh sách process đang liên tục được cập nhật mỗi giây. Layout mới này có thể tương tác với bàn phím. Ví dụ:
- 
| Phím | Chức năng                                                  |
|------|------------------------------------------------------------|
| h hoặc ? | Hiện cửa sổ help với các câu lệnh hữu dụng                  |
| space | Cập nhật bảng process ngay lập tức thay vì phải chờ vài giây |
| f | Thêm trường mới để hiển thị layout hoặc xóa những field nhất định vì vậy bạn sẽ không thấy nó hiển thị |
| q | Thoát ứng dụng top hoặc mở thêm cửa sổ mới của ứng dụng top (ví dụ: sau khi dùng feature f) |
| l | Bật/tắt thông tin trung bình tải và thời gian uptime |
| m | Bật/tắt thông tin bộ nhớ |
| P (Shift + p) | Sắp xếp process bằng CPU usage |
| s | Đổi đột trễ giữa các lần refresh (bạn sẽ được hỏi bao nhiêu giây) |


- Với command top, bạn có thể dùng các tùy chọn sau, ví dụ:
  
| Tùy chọn | Chức năng                                                          |
|----------|--------------------------------------------------------------------|
| -d delay | Xác định độ trễ (thời gian giữa các lần cập nhật)                    |
| -n number | Refresh trang bao nhiêu lần, sau đó thoát                            |
| -p pid   | Chỉ hiển thị và giám sát process với đúng process ID được chọn      |
| -q       | Refresh mà không có delay                                           |

#### Ps
- ps – Một command hữu ích khác để hiển thị processes trong Linux. Sau đây là một số tùy chọn thường được dùng với command ps:
  
| Tùy chọn | Chức năng                                                               |
|----------|-------------------------------------------------------------------------|
| -e       | Hiển thị tất cả các processes                                            |
| -f       | Hiển thị toàn bộ danh sách được định dạng                                 |
| -r       | Chỉ hiển thị các process đang chạy                                       |
| -u       | Chỉ định username (hoặc nhiều usernames) để lọc                          |
| --pid    | Lọc các process dựa trên PID                                             |
| --ppid   | Lọc các process dựa trên Parent PID                                      |


#### Tắt và ưu tiên Process
##### Kill
- kill: gửi tín hiệu tới 1 tiến trình theo pid
- kill -9 vs kill -15:

| Tùy chọn | Chức năng                                                                                   |
|----------|---------------------------------------------------------------------------------------------|
| -9       | Kết thúc tiến trình ngay lập tức (SIGKILL).                                               |
| -15      | Gửi tín hiệu kết thúc tới tiến trình (SIGTERM). Tiến trình có thể thực hiện các công việc dọn dẹp trước khi kết thúc. |

##### Nice
- Một câu lệnh hữu dụng khác để quản lý process là **NICE**. Cơ bản, nó cho bạn ưu tiên process nào quan trọng trong trường hợp bạn chạy nhiều. Bằng cách này, máy tính sẽ biết process nào quan trong hơn và sẽ chạy chúng trước. 
- Process với độ ưu tiên thấp hơn sẽ chỉ chạy khi nó được yêu cầu (nếu CPU power hết mức sử dụng) Command này có thể cho gia trị từ -20 đến 19. Giá trị càng thấp, thì độ ưu tiên càng cao. Mặc định tất cả process là 0. Cấu trúc của lệnh sẽ như sau:

- Xem độ ưu tiên hiện tại của một tiến trình với PID là 1234:
```sh
nice -n 1234
```
- Chạy lệnh gzip với độ ưu tiên cao hơn (-10):
```sh
nice -n -10 gzip file.txt
```
- Chạy lệnh ffmpeg với độ ưu tiên thấp hơn (5):
```sh
nice -n 5 ffmpeg -i input.mp4 output.avi
```
- Thay đổi độ ưu tiên của tiến trình với PID là 5678 thành độ ưu tiên -15:
```sh
renice -n -15 -p 5678
```





 




