# Cấu trúc cây thư mục trong Linux
![Cấu trúc cây thư mục trong CentOS 7](https://wiki.matbao.net/wp-content/uploads/2016/12/Linux-filesystem-structure.png)


1. `/` - Root
   Đúng với tên gọi của mình: nút gốc (root) đây là nơi bắt đầu của tất cả các file và thư mục. Chỉ có root user mới có quyền ghi trong thư mục này. Chú ý rằng `/root` là thư mục home của root user chứ không phải là `/`.

2. `/bin` - Chương trình của người dùng
   Thư mục này chứa các chương trình thực thi. Các chương trình chung của Linux được sử dụng bởi tất cả người dùng được lưu ở đây. Ví dụ như: `ps`, `ls`, `ping`...

3. `/sbin` - Chương trình hệ thống
   Cũng giống như `/bin`, `/sbin` cũng chứa các chương trình thực thi, nhưng chúng là những chương trình của admin, dành cho việc bảo trì hệ thống. Ví dụ như: `reboot`, `fdisk`, `iptables`...

4. `/etc` - Các file cấu hình
   Thư mục này chứa các file cấu hình của các chương trình, đồng thời nó còn chứa các shell script dùng để khởi động hoặc tắt các chương trình khác. Ví dụ: `/etc/resolv.conf`, `/etc/logrotate.conf`

5. `/dev` - Các file thiết bị
   Các phân vùng ổ cứng, thiết bị ngoại vi như USB, ổ đĩa cắm ngoài, hay bất cứ thiết bị nào gắn kèm vào hệ thống đều được lưu ở đây. Ví dụ: `/dev/sdb1` là tên của USB bạn vừa cắm vào máy, để mở được USB này bạn cần sử dụng lệnh mount với quyền root: `# mount /dev/sdb1 /tmp`

6. `/tmp` - Các file tạm
   Thư mục này chứa các file tạm thời được tạo bởi hệ thống và các người dùng. Các file lưu trong thư mục này sẽ bị xóa khi hệ thống khởi động lại.

7. `/proc` - Thông tin về các tiến trình
   Thông tin về các tiến trình đang chạy sẽ được lưu trong `/proc` dưới dạng một hệ thống file thư mục mô phỏng. Ví dụ thư mục con `/proc/{pid}` chứa các thông tin về tiến trình có ID là pid (pid ~ process ID). Ngoài ra đây cũng là nơi lưu thông tin về các tài nguyên đang sử dụng của hệ thống như: /proc/version, /proc/uptime...

8. `/var` - File về biến của chương trình
Thông tin về các biến của hệ thống được lưu trong thư mục này. Như thông tin về log file: /var/log, các gói và cơ sở dữ liệu /var/lib...

1. `/usr` - Chương trình của người dùng
Chứa các thư viện, file thực thi, tài liệu hướng dẫn và mã nguồn cho chương trình chạy ở level 2 của hệ thống. Trong đó:

- `/usr/bin` chứa các file thực thi của người dùng như: `at`, `awk`, `cc`, `less`... Nếu bạn không tìm thấy chúng trong /bin hãy tìm trong `/usr/bin`
- `/usr/sbin` chứa các file thực thi của hệ thống dưới quyền của admin như: `atd`, `cron`, `sshd`... Nếu bạn không tìm thấy chúng trong /sbin thì hãy tìm trong thư mục này.
- `/usr/lib` chứa các thư viện cho các chương trình trong `/usr/bin` và `/usr/sbin`
- `/usr/local` chứa các chương trình của người dùng được cài từ mã nguồn. Ví dụ như bạn cài apache từ mã nguồn, nó sẽ được lưu dưới `/usr/local/apache2`

10. `/home` - Thư mục người dùng
Thư mục này chứa tất cả các file cá nhân của từng người dùng. Ví dụ: `/home/john`, `/home/marie`

11. `/boot` - Các file khởi động
Tất cả các file yêu cầu khi khởi động như `initrd`, `vmlinux`, `grub` được lưu tại đây. Ví dụ `vmlinuz-2.6.32-24-generic`

12. `/lib` - Thư viện hệ thống
Chứa các thư viện hỗ trợ cho các file thực thi trong `/bin` và `/sbin`. Các thư viện này thường có tên bắt đầu bằng ld* hoặc lib*.so.*. Ví dụ như ld-2.11.1.so hay libncurses.so.5.7

13. `/opt` - Các ứng dụng phụ tùy chọn
Tên thư mục này nghĩa là optional (tùy chọn), nó chứa các ứng dụng thêm vào từ các nhà cung cấp độc lập khác. Các ứng dụng này có thể được cài ở `/opt` hoặc một thư mục con của `/opt`

14. `/mnt` - Thư mục để mount
Đây là thư mục tạm để mount các file hệ thống. Ví dụ như `# mount /dev/sda2 /mnt`

15. `/media` - Các thiết bị gắn có thể gỡ bỏ
Thư mục tạm này chứa các thiết bị như CD-ROM `/media/cdrom`, floppy /media/floppy hay các phân vùng đĩa cứng /media/Data (hiểu như là ổ D:/Data trong Windows)

16. `/srv` - Dữ liệu của các dịch vụ khác
Chứa dữ liệu liên quan đến các dịch vụ máy chủ như `/srv/svs`, chứa các dữ liệu liên quan đến CVS.

# Các lệnh dòng lệnh tương tác với thư mục trong Linux

Dưới đây là một số lệnh dòng lệnh phổ biến được sử dụng để tương tác với thư mục trong hệ điều hành Linux.

## 1. Lệnh `cd`

Lệnh `cd` được sử dụng để di chuyển đến một thư mục khác.

| Tùy chọn       | Mô tả                                        |
|----------------|----------------------------------------------|
| cd [đường_dẫn] | Di chuyển vào thư mục được chỉ định           |
| cd -           | Di chuyển đến thư mục trước đó                |
| cd ~           | Di chuyển đến thư mục người dùng               |
| cd ..          | Di chuyển đến thư mục cha                      |
| cd /           | Di chuyển đến thư mục gốc                        |


## 2. Lệnh `ls`

Lệnh `ls` được sử dụng để liệt kê các tệp và thư mục trong thư mục hiện tại.

| Tùy chọn        | Mô tả                                           |
|-----------------|-------------------------------------------------|
| ls              | Liệt kê tất cả các tệp và thư mục trong thư mục hiện tại |
| ls -l           | Liệt kê chi tiết với thông tin như quyền truy cập, kích thước, ngày tạo, v.v.   |
| ls -a           | Liệt kê tất cả các tệp và thư mục, bao gồm cả các tệp ẩn (bắt đầu bằng dấu chấm)     |
| ls -h           | Liệt kê với đơn vị kích thước dễ đọc (KB, MB, GB)           |
| ls -S           | Sắp xếp kết quả theo kích thước từ lớn đến nhỏ                  |
| ls -t           | Sắp xếp kết quả theo thời gian sửa đổi từ mới nhất đến cũ nhất         |
| ls -r           | Liệt kê theo thứ tự đảo ngược                                      |
| ls -R           | Liệt kê đệ quy, bao gồm cả các thư mục con                          |
| ls --color=auto | Hiển thị kết quả với màu sắc                                        |
 

## 3. Lệnh `mkdir`

Lệnh `mkdir` được sử dụng để tạo mới một thư mục.

| Tùy chọn        | Mô tả                                            |
|-----------------|--------------------------------------------------|
| mkdir [tên]     | Tạo một thư mục với tên chỉ định                  |
| mkdir -p [đường_dẫn] | Tạo các thư mục theo đường dẫn, bao gồm cả các thư mục cha không tồn tại    |
| mkdir -m [quyền] [tên] | Tạo một thư mục với quyền truy cập được chỉ định   |
| mkdir -v [tên]  | Hiển thị thông báo chi tiết khi tạo thư mục       |


## 4. Lệnh `rm`

Lệnh `rm` được sử dụng để xóa tệp hoặc thư mục.

| Tùy chọn       | Mô tả                                                      |
|----------------|------------------------------------------------------------|
| rm [tệp/thư_mục] | Xóa tệp hoặc thư mục                                       |
| rm -r [thư_mục] | Xóa thư mục và nội dung bên trong (đệ quy)                  |
| rm -f [tệp]     | Xóa tệp mà không hiển thị cảnh báo                          |
| rm -i [tệp]     | Xóa tệp và yêu cầu xác nhận trước khi xóa                   |
| rm -v [tệp]     | Hiển thị thông báo chi tiết khi xóa tệp                     |
| rm -rf [thư_mục] | Xóa thư mục và nội dung bên trong mà không yêu cầu xác nhận |


## 5. Lệnh `mv`

Lệnh `mv` được sử dụng để di chuyển hoặc đổi tên tệp hoặc thư mục.

| Tùy chọn       | Mô tả                                                        | Ví dụ                                 |
|----------------|--------------------------------------------------------------|---------------------------------------|
| mv [nguồn] [đích] | Di chuyển (hoặc đổi tên) tệp/thư mục từ nguồn đến đích        | mv file.txt /thumuc/moi/file.txt       |
| mv -i [nguồn] [đích] | Di chuyển (hoặc đổi tên) và yêu cầu xác nhận trước khi ghi đè | mv -i file.txt /thumuc/moi/file.txt    |
| mv -u [nguồn] [đích] | Di chuyển (hoặc đổi tên) chỉ khi nguồn mới hơn hoặc khác đích | mv -u file.txt /thumuc/moi/file.txt    |
| mv -v [nguồn] [đích] | Hiển thị thông báo chi tiết khi di chuyển (hoặc đổi tên)      | mv -v file.txt /thumuc/moi/file.txt    |


## 6. Lệnh `cp`

Lệnh `cp` được sử dụng để sao chép tệp hoặc thư mục.

| Tùy chọn       | Mô tả                                                        | Ví dụ                                 |
|----------------|--------------------------------------------------------------|---------------------------------------|
| cp [nguồn] [đích] | Sao chép tệp/thư mục từ nguồn đến đích                      | cp file.txt /thumuc/moi/file.txt       |
| cp -r [thư_mục] | Sao chép thư mục và nội dung bên trong (đệ quy)               | cp -r /thumuc/goc /thumuc/dich         |
| cp -i [nguồn] [đích] | Sao chép và yêu cầu xác nhận trước khi ghi đè                 | cp -i file.txt /thumuc/moi/file.txt    |
| cp -u [nguồn] [đích] | Sao chép chỉ khi nguồn mới hơn hoặc khác đích                 | cp -u file.txt /thumuc/moi/file.txt    |
| cp -v [nguồn] [đích] | Hiển thị thông báo chi tiết khi sao chép                     | cp -v file.txt /thumuc/moi/file.txt    |


##7. Lệnh `tree`
- `tree`: chạy lệnh tree mà không có bất kỳ đối số nào, lệnh tree sẽ hiển thị tất cả nội dung của thư mục làm việc hiện hành ở định dạng cây. => lệnh tree trả về tổng số file và/hoặc thư mục được liệt kê
![Chạy lệnh tree không có bất kỳ đối số nào](https://st.quantrimang.com/photos/image/2020/11/20/cau-truc-cay-thu-muc-trong-linux-1.jpg)

- `tree /etc/`: liệt kê các file của thư mục cụ thể ở định dạng cây, chẳng hạn như /etc
- `tree -a /etc/`: Theo mặc định, lệnh tree sẽ không liệt kê các file ẩn. Nếu bạn muốn liệt kê các file ẩn, hãy sử dụng tham số -a
- `tree -C /etc/`: xem cấu trúc thư mục ở định dạng màu
  ![Xem cấu trúc thư mục ở định dạng màu](https://st.quantrimang.com/photos/image/2020/11/20/cau-truc-cay-thu-muc-trong-linux-4.jpg)
  
- `tree -d /etc/`: tất cả các lệnh trên đều liệt kê các thư mục con và file. Bạn cũng có thể chỉ liệt kê các thư mục sử dụng tham số `-d`

#### Tài liệu tham khảo
https://quantrimang.com/cong-nghe/cau-truc-cay-thu-muc-trong-linux-84056
https://wiki.matbao.net/kb/co-ban-cau-truc-thu-muc-trong-linux/
https://biquyetxaynha.com/cach-tao-cay-thu-muc-trong-linux
https://bizflycloud.vn/tin-tuc/tree-lenh-liet-ke-thu-muc-va-file-theo-dang-cay-tren-linux-20180309115852667.htm
https://www.geeksforgeeks.org/tree-command-unixlinux/


