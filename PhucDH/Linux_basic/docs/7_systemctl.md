Quản lý dịch vụ là một trong những trách nhiệm chính của quản trị viên hệ thống Linux. Bên cạnh đó, việc biết cách quản lý các dịch vụ hệ thống cũng rất quan trọng đối với người dùng Linux vì họ có thể phải xử lý các dịch vụ theo cách này hay cách khác.

Hướng dẫn này xem xét cách quản lý các dịch vụ systemd bằng lệnh systemctl.

## Systemd là gì?

Systemd là một trình quản lý hệ thống và dịch vụ cho hệ điều hành Linux. Nó là trình quản lý dịch vụ mặc định trong nhiều bản phân phối Linux bao gồm Ubuntu, Red RHEL, OpenSuse và Arch Linux. Systemd là sự kế thừa của các trình quản lý dịch vụ cũ hơn như System V và Upstart .

Không giống như trình quản lý dịch vụ System V, systemd hiệu quả hơn do khởi động các dịch vụ song song để tăng tốc quá trình khởi động Linux. Một tính năng độc đáo khác của systemd là nó cung cấp dịch vụ theo yêu cầu, tức là nó có thể trì hoãn việc bắt đầu dịch vụ cho đến khi hệ thống cần, điều này giúp cải thiện hiệu suất đáng kể.

Systemd không bị giới hạn trong việc quản lý các quy trình hoặc dịch vụ điều hành mà còn có thể được sử dụng để giám sát mạng, bộ định thời gian chạy (running timer) và hơn thế nữa.

Trong Linux, lệnh systemctl chịu trách nhiệm quản lý các dịch vụ systemd. Nếu bạn có thư mục `/usr/lib/systemd` trên hệ thống của mình, thì rất có thể bạn đang sử dụng trình quản lý dịch vụ systemd.

Bạn cũng có thể chạy bất kỳ lệnh nào sau đây để kiểm tra xem trình quản lý dịch vụ systemd có sẵn trên hệ thống của bạn hay không.

```sh
systemctl --version
hoặc
systemd --version
```

## Các thành phần của Systemd

Về cơ bản thì systemd tương đương với một chương trình quản lý hệ thống và các dịch vụ trong Linux. Nó cung cấp một số các tiện ích như sau

- `systemctl` dùng để quản lý trạng thái của các dịch vụ hệ thống (bắt đầu, kết thúc, khởi động lại hoặc kiểm tra trạng thái hiện tại)

- `journald` dùng để quản lý nhật ký hoạt động của hệ thống (hay còn gọi là ghi log)

- `logind` dùng để quản lý và theo dõi việc đăng nhập/đăng xuất của người dùng

- `networkd` dùng để quản lý các kết nối mạng thông qua các cấu hình mạng

- `timedated` dùng để quản lý thời gian hệ thống hoặc thời gian mạng

- `udev` dùng để quản lý các thiết bị và firmware

## Unit file

Tất cả các chương trình được quản lý bởi systemd đều được thực thi dưới dạng daemon hay background bên dưới nền và được cấu hình thành 1 file configuration gọi là unit file. Các unit file này sẽ bao gồm 12 loại:

    . service (các file quản lý hoạt động của 1 số chương trình)
    . socket (quản lý các kết nối)
    . device (quản lý thiết bị)
    - mount (gắn thiết bị)
    - automount (tự đống gắn thiết bị)
    - swap (vùng không gian bộ nhớ trên đĩa cứng)
    - target (quản lý tạo liên kết)
    - path (quản lý các đường dẫn)
    - timer (dùng cho cron-job để lập lịch)
    - snapshot (sao lưu)
    - slice (dùng cho quản lý tiến trình)
    - scope (quy định không gian hoạt động)


### Service

Mặc dù là có 12 loại unit file trong systemd, tuy nhiên có lẽ service là loại thường được quan tâm nhất. Loại này sẽ được khởi động khi bật máy và luôn chạy ở chế độ nền (daemon hoặc background) Các service thường sẽ được cấu hình trong các file riêng biệt và được quản lý thông qua câu lệnh systemctl Ta có thể sử dụng câu lệnh sau để xem các service đã được kích hoạt bởi hệ thống:

```sh
systemctl list-units | grep -e '.service'
```

hoặc

```sh
systemctl -t service
```

Bộ tùy chọn quen thuộc của systemctl sẽ dùng khi muốn bật/tắt một service

- **start**: bật service
- **stop**: tắt service
- **restart**: tắt service rồi bật lại (ngoài ra còn có reload để tải lại file cấu hình tuy nhiên chỉ có 1 số chương trình hỗ trợ như Apache/Nginx ...) Ba tùy chọn trên sẽ được sử dụng khi hệ thống đang hoạt động, tuy nhiên systemctl cũng cung cấp 2 tùy chọn khác để điều khiển việc hoạt động của service từ lúc khởi động hệ thống
- **enable**: service sẽ được khởi động cùng hệ thống
- **disable**: service sẽ không được khởi động cùng hệ thống

### Các hệ thống tương tự Systemd

Systemd mới chỉ xuất hiện từ 30-3-2010, còn trước đó có 2 hệ thống khác đã từng được sử dụng

Upstart: hệ thống init được phát triển bởi Canonical và được sử dụng trong Ubuntu Linux giai đoạn đầu.
SysV: hệ thống init cổ điển của UNIX BSD System V, được viết bằng shell script và đã quá lâu đời.


## Tạo service với Systemd

>Thông thường các dịch vụ được cài đặt thêm sẽ tự động tạo ra các file này, chỉ trong trường hợp quá trình cài đặt bị lỗi, hoặc ta cố ý thay đổi mặc định của dịch vụ thì mới cần cấu hình mới phải làm bằng tay. Tuyệt đối không thay đổi nếu bạn là người mới tìm hiểu.

Phần trên ta đã nói về việc các service của systemd được quản lý trong các file cấu hình riêng biệt. Vì vậy, chúng ta hoàn toàn có thể tạo ra một file service của chúng ta để phục vụ một công việc nào đó. Mình sẽ ví dụ với một file cấu hình đơn giản như sau

```sh
# Location: /etc/systemd/system/simple-echo.service
[Unit]
Description=Simple Echo

[Service]
Type = forking
ExecStart = /usr/local/bin/simple-echo start
ExecStop = /usr/local/bin/simple-echo stop
ExecReload = /usr/local/bin/simple-echo restart

[Install]
WantedBy = multi-user.target
```

Và đây là file thực thi của dịch vụ

```sh
#!/bin/bash
# Location: /usr/local/bin/simple-echo

function echo_start () {
  echo "Echo: starting service ..."
  sleep 1
  echo "Echo: starting done"
}

function echo_stop () {
  echo "Echo: stopping service ..."
  sleep 1
  echo "Echo: stopping done"
}

function echo_status () {
  echo "Echo service"
}

case "$1" in
  'start')
    echo_start
    ;;
  'stop')
    echo_stop
    ;;
  'restart')
    echo_start
    sleep 1
    echo_stop
    ;;
  'status')
    echo_status
    ;;
  *)
    echo "Usage: $0 {start|stop|status|restart}" >&2
    ;;
esac
```

Và giờ ta có thể thử với các câu lệnh

```sh
systemctl status simple-echo
```

hoặc

```sh
systemctl start simple-echo
```

, nếu các câu lệnh này không báo lỗi thì quá trình tạo một service đơn giản đã thành công.

>Đây chỉ một file cấu hình đơn giản của service, thực chất không có chương trình nào khác được thực thi.

## Kiểm tra trạng thái của dịch vụ

Để kiểm tra trạng thái của một dịch vụ cụ thể trên hệ thống của bạn, hãy sử dụng lệnh `status` (trạng thái) theo sau là tên của dịch vụ bạn muốn kiểm tra.

Ví dụ, để kiểm tra trạng thái của dịch vụ docker, bạn có thể chạy lệnh sau. Docker là một chương trình ảo hóa hiện đại được các nhà phát triển phần mềm sử dụng để xây dựng các ứng dụng một cách hiệu quả.

```sh
systemctl status docker
```

>Lưu ý: Hướng dẫn sử dụng systemctl cũng chỉ động từ sau systemctl như một lệnh, do đó, hướng dẫn này sẽ bám sát định nghĩa đó để có tính nhất quán.

Ngoài việc liệt kê trạng thái của dịch vụ, lệnh status cũng cung cấp cho bạn các thông tin quan trọng như ID quy trình (PID) của dịch vụ, mức sử dụng bộ nhớ và danh sách các thay đổi gần đây trong dịch vụ.

Biết trạng thái của dịch vụ là một trong những cách chính bạn sẽ sử dụng để khắc phục lỗi hoặc chẩn đoán sự cố. Trước khi đi vào chi tiết lý do tại sao một cái gì đó không hoạt động, quản trị viên hệ thống thường trước hết sẽ kiểm tra xem dịch vụ có vận hành hay không.

## Liệt kê dịch vụ với lệnh systemctl

Thông thường, bạn sẽ cần biết những dịch vụ nào có trên hệ thống của mình trước khi có thể tiến hành quản lý chúng. Bạn có thể sử dụng lệnh sau để liệt kê tất cả các dịch vụ hiện có trên hệ thống của mình.

```sh
systemctl list-unit-files --type service --all
```

Ngoài việc liệt kê các dịch vụ có trên hệ thống của bạn, lệnh cũng sẽ hiển thị trạng thái của các dịch vụ này. Các trạng thái phổ biến nhất bao gồm; enabled (đã bật), disabled (tắt), masked (bị che), v.v.

## Các lệnh cơ bản của systemctl

Lệnh systemctl có nhiều tùy chọn để quản lý các dịch vụ. Dưới đây là các lệnh cơ bản của systemctl:

- Khởi động dịch vụ: systemctl start service-name
- Dừng dịch vụ: systemctl stop service-name
- Khởi động lại dịch vụ: systemctl restart service-name
- Kiểm tra trạng thái của dịch vụ: systemctl status service-name
- Xem các thông tin chi tiết về dịch vụ: systemctl show service-name
- Bật dịch vụ tự động khởi

## Cách sử dụng lệnh systemctl

- Khởi động, dừng và khởi động lại dịch vụ

    Khởi động:

    ```sh
    sudo systemctl start service-name
    ```

    vd:

    ```sh
    sudo systemctl start apache2 
    ```

    để khởi động dịch vụ Apache.

    Dừng dịch vụ:

    ```sh
    sudo systemctl stop service-name
    ```

    vd:

    ```sh
    sudo systemctl stop apache2 
    ```

    để dừng dịch vụ Apache.

    khởi động lại dịch vụ:

    ```sh
    sudo systemctl restart service-name
    ```

    vd:

    ```sh
    sudo systemctl restart apache2
    ```

    để khởi động lại dịch vụ Apache.


- Kiểm tra trạng thái của dịch vụ

    cú pháp:

    ```sh
    sudo systemctl status service-name
    ```

    vd:

    ```sh
    sudo systemctl status sshd
    ```

    để kiểm tra trạng thái của dịch vụ SSH, Output có thể:

    ```sh
    ubuntu@ubuntu-2204:~$ ssudo systemctl status sshd
    ● ssh.service - OpenBSD Secure Shell server
        Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
        Active: active (running) since Fri 2023-05-26 08:31:37 +07; 4h 52min ago
        Docs: man:sshd(8)
                man:sshd_config(5)
    Main PID: 873 (sshd)
        Tasks: 1 (limit: 1860)
        Memory: 5.5M
            CPU: 416ms
        CGroup: /system.slice/ssh.service
                └─873 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"

    Thg 5 26 08:31:36 ubuntu-2204 systemd[1]: Starting OpenBSD Secure Shell server...
    Thg 5 26 08:31:37 ubuntu-2204 sshd[873]: Server listening on 0.0.0.0 port 22.
    Thg 5 26 08:31:37 ubuntu-2204 sshd[873]: Server listening on :: port 22.
    Thg 5 26 08:31:37 ubuntu-2204 systemd[1]: Started OpenBSD Secure Shell server.
    Thg 5 26 08:37:59 ubuntu-2204 sshd[2673]: Accepted password for ubuntu from 192.168.20.1 port 52407 ssh2
    Thg 5 26 08:37:59 ubuntu-2204 sshd[2673]: pam_unix(sshd:session): session opened for user ubuntu(uid=1000) by (uid=0)
    Thg 5 26 13:23:58 ubuntu-2204 sshd[10305]: Accepted password for ubuntu from 192.168.20.1 port 65247 ssh2
    Thg 5 26 13:23:58 ubuntu-2204 sshd[10305]: pam_unix(sshd:session): session opened for user ubuntu(uid=1000) by (uid=0)
    ubuntu@ubuntu-2204:~$
    ```

- Xem các thông tin chi tiết về dịch vụ

    cú pháp

    ```sh
    sudo systemctl show service-name
    ```

    vd

    ```sh
    sudo systemctl show sshd
    ```


    Kết quả trả về sẽ cho bạn biết các thông tin chi tiết về dịch vụ, bao gồm tên, mô tả, file cấu hình, và các thông số khác. Output có thể:

    ```sh
    ubuntu@ubuntu-2204:~$ sudo systemctl show sshd
    Type=notify
    Restart=on-failure
    NotifyAccess=main
    RestartUSec=100ms
    TimeoutStartUSec=1min 30s
    TimeoutStopUSec=1min 30s
    TimeoutAbortUSec=1min 30s
    TimeoutStartFailureMode=terminate
    TimeoutStopFailureMode=terminate
    RuntimeMaxUSec=infinity
    WatchdogUSec=0
    WatchdogTimestamp=n/a
    WatchdogTimestampMonotonic=0
    RootDirectoryStartOnly=no
    RemainAfterExit=no
    GuessMainPID=yes
    RestartPreventExitStatus=255
    MainPID=873
    ControlPID=0
    FileDescriptorStoreMax=0
    NFileDescriptorStore=0
    StatusErrno=0
    Result=success
    ReloadResult=success
    CleanResult=success
    UID=[not set]
    GID=[not set]
    NRestarts=0
    OOMPolicy=stop
    lines 1-29
    ```

- Quản lý các file cấu hình dịch vụ

    Lệnh systemctl cũng cho phép bạn quản lý các file cấu hình của dịch vụ. Các file cấu hình này có thể được tìm thấy trong thư mục `/etc/systemd/system`.

    Để xem các file cấu hình của một dịch vụ, bạn có thể sử dụng lệnh sau:

    ```sh
    sudo systemctl cat service-name
    ```

    Ví dụ:

    ```sh
    sudo systemctl cat apache2
    ```

    để xem các file cấu hình của dịch vụ Apache.

    Nếu bạn muốn chỉnh sửa các file cấu hình này, bạn có thể sử dụng trình soạn thảo văn bản để mở file và chỉnh sửa nội dung.

- Để khởi động một dịch vụ khi hệ thống khởi động

    Cú pháp:

    ```sh
    sudo systemctl enable service-name
    ```

    ví dụ:

    ```sh
    sudo systemctl enable apache2 
    ```

    để khởi động dịch vụ Apache khi hệ thống khởi động.

- Để ngăn chặn một dịch vụ khởi động khi hệ thống khởi động

    Cú pháp:

    ```sh
    sudo systemctl disable service-name
    ```

    vd:

    ```sh
    sudo systemctl disable apache2
    ```

    để ngăn chặn dịch vụ Apache khởi động khi hệ thống khởi động

- kiểm tra xem một dịch vụ đã được khởi động khi hệ thống khởi động

cú pháp:

```sh
sudo systemctl is-enabled service-name
```

ví dụ:

```sh
sudo systemctl is-enabled sshd
```

Kết quả trả về sẽ là “enabled” nếu dịch vụ đã được khởi động, hoặc “disabled” nếu dịch vụ chưa được khởi động.


**Đây là những lệnh rất cơ bản và thường sử dụng cho người mới bắt đầu. Để tìm hiểu rõ hơn ta có thể tham khảo bằng cách sử dụng lệnh: man systemctl hoặc systemctl --help**



Tham khảo tại:

<https://bkhost.vn/blog/lenh-systemctl/>

<https://viblo.asia/p/tim-hieu-va-van-dung-systemd-de-quan-ly-he-thong-linux-phan-co-ban-WAyK8kN65xX>
