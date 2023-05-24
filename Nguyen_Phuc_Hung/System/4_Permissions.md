**Trong Linux mỗi một tập tin hay thư mục sẽ được cấp các quyền đọc, ghi, thực thi cho từng user khác nhau. Điều này giúp tăng cường bảo mật và tạo nên sức mạnh cho các hệ thống linux.**

![](https://kienthucvps.com/wp-content/uploads/2021/07/download.png)

# Các khái niệm
1.	Ownership
2.	Permissons
## Ownership
**Mỗi file hay thư mục trên Linux đều được gán bởi 3 loại chủ sở hữu là user, group, other**
### User
- Theo như mặc định trên Linux thì người tạo ra file hay thư mục nào đó thì sẽ trở thành chủ sở hữu của chính nó, giống như việc một người A tạo ra một vậy B thì mặc định người A sẽ là chủ sở hữu của vật B đó.
### Group
- Một nhóm có thể chứa nhiều người dùng cùng một lúc. Tất cả người dùng trong một nhóm sẽ có cùng quyền truy cập vào file hay thư mục đó. Giả sử có một tài liệu học tập cho một lớp học mà bạn không muốn cho lớp khác biết, chỉ muốn chia sẻ trong lớp. Thay vì bạn cấp quyền cho từng người trong lớp thì bạn có thể gom tất những người trong lớp thành một nhóm người dùng và bạn gán quyền cho một nhóm người dùng đó để chỉ có những người trong nhóm đó mới có quyền truy cập vào tài liệu.
### Other
- Other là bất kỳ người dùng nào không thuộc vào 2 đối tượng phía trên. Xét lại ví dụ trên, bạn không phải là thuộc nhóm lớp được truy cập vào tài liệu và bạn cũng không phải là người sở hữu tài liệu đó thì bạn được xét là other.
Bài toán đặt ra là làm sao để Linux phân biệt giữa ba loại người dùng này để người dùng A không ảnh hưởng đến một số file hay thư mục chứa thông tin hay dữ liệu của một người dùng B. Và đây chính là lúc permissions(quyền) được sử dụng để kiểm soát hình vi của người dùng.
## Permissions
Mỗi một file hay thư mục trong Linux đều có 3 quyền đọc, ghi, thực thi được xác định cho 3 chủ sở hữu ở trên.
- Đọc: Nếu là một file thì quyền này cho phép bạn mở file đó lên và đọc. Nếu là một thư mục thì nó cho phép bạn liệt kê danh sách file hay thư mục trong thư mục đó.
- Ghi: Quyền ghi cho phép bạn sửa đổi nội dung của file. Nếu là thư mục thì nó cho phép bạn có thể thêm, xóa và đổi tên các file trong thư mục đó.
- Thực thi: Với Windows bạn có thể chạy với một file có đuôi ".exe" một cách dễ dàng. Khác so với Windows, trong Linux bạn không thể chạy khi nó không được cấp quyền thực thi. Còn đối với thư mục thì bạn không thể truy cập(cd) nếu bạn không có quyền thực thi nó.

## Ví dụ thực hành 
Hình ảnh tổng quát nhất về quyền trong Linux:
![](https://kienthucvps.com/wp-content/uploads/2021/07/download.png)

*Ví dụ*


Với phần khoanh đỏ là phần permissions. Cấu trúc của phần permissions sẽ được chia ra thành từng phần như sau: đầu tiên là file type, sau đó sẽ đến đến quyền của từng owner trong hệ thống.
| file type | user | group | other | name  |
|-----------|------|-------|-------|-------|
| d         | rwx  | r-x   | r-x   | dir1  |
| -         | rw-  | r--   | r--   | file1 |

Đầu tiền trong phần permissions sẽ cho bạn biết nó là ở dạng file hay thư mục. Trong đó:
| Ký hiệu | Ý nghĩa     |
|---------|-------------|
| d       | Thư mục     |
| -       | File        |
Sau khi phân biệt được là file hay thư mục thì đến phần xem các quyền mình có thể làm đối với mỗi file hay thư mục đó. Nó được chia ra làm 3 phần là user,group, other. Ý nghĩa của r,w,x:
| Ký hiệu | Ý nghĩa            |
|---------|--------------------|
| r       | Đọc                |
| w       | Ghi                |
| x       | Thực thi           |
| -       | Không có quyền      |


## Thay đổi quyền với chmod
**chmod** là viết tắt của change mode dùng để thay đổi quyền của một thư mục hay file trên Linux.

**Phần quyền bằng số**
```sh
chmod <permissions-number> <filename>
```
![](https://images.viblo.asia/b9741f62-bb9f-492c-8bf1-8a865193edc5.png) 

Permissions -number về cơ bản sẽ có 3 chữ số một số với ý nghĩa số thứ nhất là quyền của user, số thứ 2 là quyền của group, số thứ 3 là quyền của other. Ý nghĩa của từng chữ số ở đây:
| Số | Ký hiệu | Ý nghĩa                |
|-----|---------|------------------------|
| 0   | ---     | Không có quyền          |
| 1   | --x     | Thực thi                |
| 2   | -w-     | Ghi                    |
| 3   | -wx     | Thực thi + Ghi         |
| 4   | r--     | Đọc                    |
| 5   | r-x     | Đọc + Thực thi         |
| 6   | rw-     | Đọc + Ghi             |
| 7   | rwx     | Đọc + Ghi + Thực thi  |

- Giả sử bạn cần phân quyền cho một file có tên là **file1** quyền rwxrw-r--. Nó có nghĩa là user có tất cả quyền đọc, ghi, thực thi. Group có quyền đọc và ghi và other thì chỉ có quyền đọc. Để làm điều này ta cần tính quyền cho từng chủ sở hữu.

> user: r + w +x = 4 + 2 + 1 = 7
> group: r + w = 4 + 2 = 6
> other: r = 4 = 4

Vậy quyền của cả file sẽ là 764, sau đó sử dụng lệnh sau để phân quyền:
```sh
chmod 764 file1
```
Hoặc
```sh
chmod u=rwx,g=rw,o=r (filename)
```
| Ký hiệu | Ý nghĩa |
|---------|---------|
| u       | user    |
| g       | group   |
| o       | other   |
| a       | tất cả   |

## Thay đổi owner và group
- Để thay đổi user:
```sh
sudo chown <username> <filename>
```
- Để thay đổi group:
```sh
sudo chgrp <groupname> <filename>
```
- Để thay đổi cả user và group:
```sh
sudo chown <username:groupname> <filename>
```
## Umask
- Trong hệ điều hành Linux, `umask` (viết tắt từ "user file creation mask") là một cơ chế kiểm soát quyền truy cập.
- Umask quản lý các quyền truy cập mặc định của các tệp tin và thư mục mới được tạo ra. Bằng cách thay đổi umask, bạn có thể kiểm soát quyền truy cập của các tệp tin và thư mục mà hệ thống tạo ra.
  
**Cú pháp**: 
```sh
umask [mode]
```
*Trong đó, `mode` là một chuỗi 3 chữ số (hoặc 4 chữ số nếu sử dụng biểu diễn octal).*


- Trong Linux, khi một file hay một thư mục được tạo ra thì các quyền hạn truy cập đối với chúng là (read, write, execute) cho các chủ thể (owner, group, other) sẽ được xác định dựa trên hai giá trị là quyền truy nhập cơ sở (base permission) và mặt nạ (mask).

 - Base Permission là giá trị được thiết lập sẵn từ trước, và ta không thể thay đổi được
  
   +đối với file thông thườnggiá trị base perm là 666 (rw-rw-rw-)

   +đối với thư mục (file đặc biệt) giá trị base perm là 777 (rwxrwxrwx)
- Giá trị Mask sẽ “che đi” một số bit trong Base Permission để tạo ra quyền truy cập chính thức cho file.

#### Giá trị mask được thiết lập như thế nào?
- Ban đầu, nếu bạn chưa thay đổi giá trị cho umask thì:

- Giá trị mask mặc định cho user thông thường là 002
=> Với mask này thì quyền hạn truy cập mặc định cho thư mục là 775 và file là 664

- Giá trị mask mặc định cho user root là 022
=> Với mask này thì quyền hạn truy cập mặc định cho thư mục là 755 và file là 644

- Cơ chế làm việc của umask khiến chúng ta không thể tạo ra các file với quyền execute mặc định. Vì Base permission của file luôn là 666, tức các bit ứng với quyền execute đều bằng 0, nên bất kể giá trị mask bằng bao nhiêu thì quyền truy nhập chính thức của file đều không có execute.

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/348373451_248884497732817_1995593356780836385_n.png?stp=dst-png_p206x206&_nc_cat=106&ccb=1-7&_nc_sid=aee45a&_nc_ohc=276kEJb0Q9cAX9m4Bsj&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdTQvXNNgzNhxtYEFs0itxVD2ULI7FE0hlPECnuCOEcktw&oe=649506BA)




# Tổng kết
- Có 3 loại chủ sở hữu một file/thư mục trên Linux đó là user, group, other
- Các quyền đọc, ghi, thực thi được ký hiểu là r, w, x tương ứng với các số là 4, 2, 1.
- Lệnh chmod để thay đổi quyền, chown để thay đổi user sở hữu, chrgrp để thay đổi group sở hữu.
- Umask quản lý các quyền truy cập mặc định của các tệp tin và thư mục mới được tạo ra. Bằng cách thay đổi umask, bạn có thể kiểm soát quyền truy cập của các tệp tin và thư mục mà hệ thống tạo ra.











