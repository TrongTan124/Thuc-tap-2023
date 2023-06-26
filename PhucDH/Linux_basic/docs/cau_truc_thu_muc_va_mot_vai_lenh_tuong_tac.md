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

9. `/usr` - Chương trình của người dùng
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

## Các lệnh dòng lệnh tương tác với thư mục trong Linux

Dưới đây là một số lệnh dòng lệnh phổ biến được sử dụng để tương tác với thư mục trong hệ điều hành Linux.

Hầu hết các lệnh trong Linux đều có thể xem được hướng dẫn với câu lệnh: `man`

ví dụ: man ls

Ta sẽ nhận được 1 hoặc nhiều trang giới thiệu cũng như hướng dẫn sử dụng của câu lệnh `ls`

## 1. Lệnh `cd`

Lệnh `cd` được sử dụng để di chuyển đến một thư mục khác.

**Cú pháp:** cd [đường_dẫn_thư_mục]

**Ví dụ:** cd /home/user/Documents

## 2. Lệnh `ls`

Trong các câu lệnh trong Linux, đây chắc hẳn là lệnh đầu tiên mà phần lớn người dùng Linux gặp. Lệnh này có nhiệm vụ liệt kê các file và folder có ở trong directory được chỉ định. Theo mặc định, ls sẽ tìm ở trong directory hiện tại. Bên cạnh đó, còn có nhiều option khác có thể được sử dụng với lệnh ls. Trong đó phổ biến có:

Liệt kê các file và folder trong directory hiện tại:

```sh
ls
```

Liệt kê các file và folder trong directory hiện tại, cùng option -l để hiển thị chi tiết hơn

```sh
ls -la
```

Option -h (human) để hiển thị kích thước các file thân thiện hơn với con người:

```sh
ls -lh
```

Liệt kê cả các file bị ẩn bằng option -a (all files):

```sh
ls -lha
```

**Ví dụ:** ls -l /home/user/Documents

## 3. Lệnh `mkdir`

Lệnh `mkdir` được sử dụng để tạo mới một thư mục.

**Cú pháp:** mkdir [tên_thư_mục]

**Ví dụ:** mkdir new_directory

## 4. Lệnh `rm`

Lệnh `rm` được sử dụng để xóa tệp hoặc thư mục.

**Cú pháp:** rm [tùy_chọn] [tên_tệp_được_xóa]

**Ví dụ:** rm file.txt

## 5. Lệnh `mv`

Lệnh `mv` được sử dụng để di chuyển hoặc đổi tên tệp hoặc thư mục.

**Cú pháp:** mv [đường_dẫn_nguồn] [đường_dẫn_đích]

**Ví dụ:** mv file.txt /home/user/Documents

## 6. Lệnh `cp`

Lệnh `cp` được sử dụng để sao chép tệp hoặc thư mục.

**Cú pháp:** cp [đường_dẫn_nguồn] [đường_dẫn_đích]

**Ví dụ:** cp file.txt /home/user/Documents

## 7. Lệnh `tree`

- `tree`: chạy lệnh tree mà không có bất kỳ đối số nào, lệnh tree sẽ hiển thị tất cả nội dung của thư mục làm việc hiện hành ở định dạng cây. => lệnh tree trả về tổng số file và/hoặc thư mục được liệt kê
![Chạy lệnh tree không có bất kỳ đối số nào](https://st.quantrimang.com/photos/image/2020/11/20/cau-truc-cay-thu-muc-trong-linux-1.jpg)

- `tree /etc/`: liệt kê các file của thư mục cụ thể ở định dạng cây, chẳng hạn như /etc
- `tree -a /etc/`: Theo mặc định, lệnh tree sẽ không liệt kê các file ẩn. Nếu bạn muốn liệt kê các file ẩn, hãy sử dụng tham số -a
- `tree -C /etc/`: xem cấu trúc thư mục ở định dạng màu
  ![Xem cấu trúc thư mục ở định dạng màu](https://st.quantrimang.com/photos/image/2020/11/20/cau-truc-cay-thu-muc-trong-linux-4.jpg)
  
- `tree -d /etc/`: tất cả các lệnh trên đều liệt kê các thư mục con và file. Bạn cũng có thể chỉ liệt kê các thư mục sử dụng tham số `-d`

## 8. dirs-pushd-popd

Trong trường hợp ta cần sử dụng nhiều thư mục và cần di chuyển qua lại giữa chúng. Thì việc gom chúng lại thành 1 danh sách sẽ là cách tối ưu và nhanh gọn nhất.

Để xem danh sách một cách đầy đủ thì:

```sh
dirs -l -v
```

Ban đầu sẽ không có bất kỳ danh sách nào. Ta sử dụng lệnh `pushd` để thêm vào danh sách. Lệnh sẽ thêm theo thứ tự cái nào thêm vào trước sẽ ở phía sau.

Ví dụ:

```sh
pushd /media
pushd /opt
```

ta sẽ nhận được danh sách

```sh
dirs -l -v
```

![dirs](../images/dirs.PNG)

Đã có danh sách, để di chuyển giữa các thư mục một cách nhanh chóng ta sử dụng:

```sh
pushd +<số thứ tự của vị trí cần đến>
```

ví dụ:

```sh
pushd +2
```

Ta sẽ được di chuyển về lại thư mục `/root`, đồng thời thư mục này cũng sẽ được chuyển lên đứng đầu danh sách.

Để chỉnh sửa danh sách, ta có câu lệnh `popd`. Câu lệnh cũng sẽ xoá từ đầu danh sách, và hỗ trợ xoá theo vị trí mong muốn.

## Tài liệu tham khảo

<https://vi.joecomp.com/pushd-popd-commands-linux>

<https://vietnix.vn/cac-cau-lenh-trong-linux/>

Date accessed: 24/05/2023
