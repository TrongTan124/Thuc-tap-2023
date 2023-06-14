## Nội dung chính

- các kiểu người dùng
- Phân nhóm
- Phân quyền

## Có 3 kiểu tài khoản trên một hệ thống Linux

1. Tài khoản gốc (Root account): Nó còn được gọi là superuser và sẽ có sự điều khiển tuyệt đối tới hệ thống. Một superuser có thể chạy bất cứ lệnh nào mà không bị hạn chế. Người sử dụng này có thể được ví như người quản lý hệ thống.
2. Các tài khoản hệ thống: Các tài khoản hệ thống được cần cho các hoạt động riêng trong hệ thống như tài khoản mail và các tài khoản sshd. Những tài khoản này thường được cần cho một số chức năng riêng trên hệ thống của bạn, và bất cứ sự chỉnh sửa nào tới chúng có thể ảnh hưởng bất lợi tới hệ thống.
3. Các tài khoản người dùng cá nhân: Các tài khoản này cung cấp sự truy cập mang tính tương tác tới hệ thống với người dùng và nhóm sử dụng và thường bị giới hạn truy cập vào những file và thư mục có tính chất quan trọng.

## Quản lý người và nhóm sử dụng trong Linux

## Có 4 file chính quản lý người sử dụng

1. /etc/passwd: Giữ tài khoản người dùng và thông tin mật khẩu. File này giữ các thông tin quan trọng về các tài khoản trên hệ thống Unix.
2. /etc/shadow: Giữ mật khẩu được biên thành mật mã của tài khoản tương ứng. Không phải tất cả các hệ thống đều hỗ trợ file này.
3. /etc/group: File này giữ thông tin nhóm cho mỗi tài khoản.
4. /etc/gshadow: File này giữ các thông tin tài khoản nhóm bảo mật.

**Note**: *Chúng ta có thể kiểm tra tất cả các file trên với lệnh cat, sửa với lệnh vi.*

| Lệnh     | Miêu tả                                    |
|----------|--------------------------------------------|
| useradd  | Thêm các tài khoản cá nhân tới hệ thống.     |
| usermod  | Chỉnh sửa các thuộc tính của tài khoản cá nhân. |
| userdel  | Xóa các tài khoản cá nhân từ hệ thống.       |
| groupadd | Thêm các tài khoản nhóm tới hệ thống.        |
| groupmod | Chỉnh sửa các thuộc tính của tài khoản nhóm. |
| groupdel | Dỡ bỏ các tài khoản nhóm khỏi hệ thống.      |

## Tạo một nhóm trong Linux

- Chung ta sẽ cần tạo các nhóm trước khi tạo bất kỳ một tài khoản nào, nếu không thì phải sử dụng các nhóm đang tồn tại trên hệ thống. Bạn sẽ có tất cả các nhóm được liệt kê trong tệp /etc/groups.

- Tất cả các nhóm mặc định sẽ là các nhóm tài khoản cụ thể trên hệ thống và nó không được đề nghị để sử dụng chúng cho các tài khoản thông thường. Vì thế, dưới đây là cú pháp để tạo một nhóm tài khoản mới.

```sh
groupadd [-g gid [-o]] [-r] [-f] groupname
```

Bảng dưới liệt kê chi tiết các tham số:
| Tùy chọn   | Miêu tả                                                   |
|------------|-----------------------------------------------------------|
| -g GID     | Giá trị số của ID nhóm.                                    |
| -o         | Tùy chọn này cho phép để thêm nhóm với GID không duy nhất.  |
| -r         | Dấu hiệu này chỉ thị sự thêm nhóm tới tài khoản hệ thống.  |
| -f         | Tùy chọn này khiến cho nó chỉ thoát ra với trạng thái thành công nếu nhóm đã xác định đã tồn tại. Với –g, nếu GID đã tồn tại, thì GID khác (duy nhất) được chọn. |
| groupname  | Tên nhóm thực sự được tạo.                                 |

- Nếu không xác định bất cứ tham số nào thì hệ thống sẽ sử dụng các giá trị mặc định. Ví dụ sau sẽ tạo một nhóm developers với các giá trị mặc định, mà được chấp thuận bởi hầu hết các nhà quản lý.

```sh
groupadd developers
```

## Chỉnh sửa một nhóm trong Linux

- Để chỉnh sửa một nhóm, sử dụng cú pháp lệnh groupmod

```sh
groupmod -n new_modified_group_name old_group_name
```

- Để thay đổi tên nhóm developers_2 thành deverloper, bạn gõ như sau:

```sh
groupmod -n developer developer_2
```

- Dưới đây là cách thay đổi GID thành 545:

```sh
groupmod -g 545 developer
```

## Xóa một nhóm trong Linux

- Để xóa một nhóm đang tồn tại, tất cả thứ bạn cần làm là lệnh groupdel và tên nhóm đó. Để xóa nhóm developer, lệnh là:

```sh
groupdel developer
```

**Note**:Lệnh này chỉ gỡ bỏ nhóm, không phải bất kỳ file nào liên quan tới nhóm. Các file là vẫn có thể truy cập được bởi người sở hữu của nó.

## Tạo một tài khoản cá nhân trong Linux với useradd

- Dưới đây là cú pháp để tạo một tài khoản cá nhân:

```sh
useradd -d homedir -g groupname -m -s shell -u userid accountname
```

Bảng dưới liệt kê chi tiết các tham số:
| Tùy chọn       | Miêu tả                                                                  |
|----------------|--------------------------------------------------------------------------|
| -d homedir     | Xác định thư mục chính cho tài khoản.                                     |
| -g groupname   | Xác định một tài khoản nhóm cho tài khoản cá nhân này.                     |
| -m             | Tạo thư mục chính nếu nó không tồn tại.                                   |
| -s shell       | Xác định shell mặc định cho tài khoản cá nhân này.                         |
| -u userid      | Bạn có thể xác định ID cá nhân cho tài khoản này.                          |
| accountname    | Tên tài khoản cá nhân thực sự được tạo ra.                                 |

- Nếu bạn không xác định bất kỳ tham số nào thì hệ thống sẽ sử dụng các giá trị mặc định. Lệnh useradd chỉnh sửa các tệp /etc/passwd, /etc/shadow, /etc/group và tạo một thư mục chính.

*Ví dụ*:  

```sh
useradd -d /home/mcmohd -g developers  mcmohd
```

**Note**: *Trước khi thông báo lệnh trên, bảo đảm rằng đã có nhóm developers được tạo bằng lệnh groupadd.*

- Khi một tài khoản cá nhân được tạo, bạn có thể thiết lập mật khẩu cho nó bằng cách sử dụng lệnh passwd như sau

```sh
Changing password for user mcmohd20.
New LINUX password:
Retype new LINUX password:
passwd: all authentication tokens updated successfully.
```

**Note**: *Khi bạn gõ passwd accountname, nó cung cấp cho bạn tùy chọn để thay đổi mật khẩu được cung cấp nếu bạn là superuser, nếu không thì bạn chỉ có thể thay đổi mật khẩu sử dụng lệnh tương tự nhưng không xác định tên tài khoản của bạn.*

## Chỉnh sửa một tài khoản với usermod

- Lệnh usermod cho bạn khả năng để tạo các thay đổi tới một tài khoản cá nhân đang tồn tại từ dòng lệnh. Nó sử dụng các đối số như lệnh useradd, cộng với đối số -l, cho phép thay đổi tên tài khoản.
- Điều kiện tiên quyết là bạn có quyền truy cập vào tài khoản người dùng với quyền sudo (và tên người dùng phải được thay đổi).

Giả sử bạn cần đổi tên tài khoản testaccount (đã có trên hệ thống) thành hung.

```sh
sudo usermod -l hung testaccount
```

- Tại thời điểm này, tên người dùng đã thay đổi. Tuy nhiên, thư mục chính được liên kết với tên người dùng vẫn là testaccount. Để thay đổi điều đó, hãy nhập lệnh:

```sh
sudo usermod -d /home/hung -m hung
```

- Cuối cùng, tên nhóm của tài khoản người dùng phải được thay đổi từ testaccount thành hung. Để làm điều này, hãy nhập lệnh:

```sh
sudo groupmod -n hung testaccount
```

## Xóa một tài khoản trong Unix/Linux

- Lệnh userdel có thể được sử dụng để xóa một tài khoản cá nhân đang tồn tại. Lệnh này là rất nguy hiểm nếu không được sử dụng với sự cẩn trọng.
- Chỉ có một đối số hoặc một tùy chọn có sẵn cho lệnh: -r: để gỡ bỏ thư mục chính và mail của tài khoản.

- Ví dụ, để gỡ bỏ tài khoản hung, bạn cần thông báo lệnh sau:

```sh
userdel -r hung
```

- Nếu bạn muốn giữ thư mục chính cho các mục sau, bạn không sử dụng tùy chọn -r.
- Ngoài ra, có thể dùng lệnh deluser để xóa một tài khoản trong Linux.

Sự khác biệt giữa userdel và deluser là:

- userdel: Lệnh userdel được sử dụng để xóa tài khoản người dùng từ hệ thống. Khi sử dụng lệnh này, bạn cần chỉ định tên tài khoản người dùng cần xóa. Lệnh userdel sẽ xóa tài khoản người dùng khỏi hệ thống và xóa các thông tin người dùng từ các tệp tin hệ thống như /etc/passwd, /etc/shadow và /etc/group. Tuy nhiên, lệnh này không tự động xóa thư mục chính (home directory) của người dùng.

- deluser: Lệnh deluser cũng được sử dụng để xóa tài khoản người dùng từ hệ thống. Tuy nhiên, deluser được thiết kế để có một số tùy chọn bổ sung và thực hiện một số công việc liên quan đến việc xóa tài khoản người dùng. Ví dụ, có thể sử dụng deluser để tự động xóa thư mục chính của người dùng (-remove-home), xóa tất cả các tệp tin và thư mục con trong thư mục chính (-remove-all-files), hoặc xóa người dùng khỏi các nhóm mà người dùng đang tham gia (-remove-groups). deluser cũng có khả năng xóa người dùng từ các tệp tin hệ thống tương tự như userdel.



## Lệnh passwd

- Đơn giản là lệnh này dùng để quản lý mật khẩu của tài khoản, với một số cách sử dụng cơ bản như sau.

- Để thay đổi mật khẩu của tài khoản đang đăng nhập chỉ cần gõ

    ```sh
    passwd
    ```

    output có thể:

    ```sh
    Changing password for wpkdata
    (current) UNIX password:
    Enter new UNIX password:
    Retype new UNIX password:
    passwd: password updated successfully
    ```

- Để đổi mật khẩu cho tài khoản khác, chức năng này yêu cầu là người quản trị hoặc người đăng nhập có quyền quản trị. Gõ:

    ```sh
    passwd <user name>
    hoặc
    sudo passwd <user name>
    ```

    output có thể:

    ```sh
    passwd wpkdata
    ```

    ```sh
    Enter new UNIX password:
    Retype new UNIX password:
    passwd: password updated successfully
    ```

- Có thể đặt mật khẩu cho cả nhóm người dùng

    Khi tùy chọn -g được sử dụng, mật khẩu cho nhóm sẽ bị thay đổi. Trong ví dụ này, hãy thay đổi mật khẩu cho nhóm sales:

    ```sh
    passwd -g sales
    ```

    Tùy chọn -r được sử dụng với tùy chọn -g để xóa mật khẩu hiện tại khỏi nhóm. Điều này cho phép nhóm truy cập vào tất cả các thành viên. Tùy chọn -R được sử dụng với tùy chọn -g để hạn chế nhóm đối với tất cả người dùng.

- Buộc người dùng thay đổi mật khẩu trong lần đăng nhập tiếp theo. Chỉ người quản trị, hoặc người dùng có quyền quản trị mới có thể thực hiện.

    Cú pháp lệnh:

    ```sh
    sudo passwd -e {username}
    hoặc
    sudo passwd --expire {username}
    ```

    vd:

    ```sh
    sudo passwd -e marlena
    ```

    Thông báo xác nhận có thể như thế này:

    ```sh
    passwd: password expiry information changed.
    ```

    Khi người dùng cố gắng đăng nhập thông qua lệnh ssh, họ sẽ thấy những điều sau trên màn hình:

    ```sh
    ssh marlena@192.168.2.25
    Last login: Fri Dec 4 04:12:48 2020 from 192.168.2.105
    WARNING: Your password has expired.
    You must change your password now and login again!
    Changing password for marlena.
    Current password:
    New password:
    Retype new password:
    passwd: password updated successfully
    Connection to 192.168.2.25 closed.
    ```

- Khóa và mở khóa mật khẩu người dùng của tài khoản:

>lưu ý: tính năng này không vô hiệu hoá tài khoản của người dùng, mà chỉ ngăn người dùng tự ý thay đổi mật khẩu. Chỉ người quản trị hoặc người có quyền quản trị mới có thể thực hiện hành động này.

Cú pháp:

```sh
sudo passwd -l {username}
```

nó thêm dấu ! vào đầu mật khẩu trong file /etc/shadow. Muốn mở khóa mật khẩu, hãy thử:

```sh
sudo passwd -u {username}
```
