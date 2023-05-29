# Khái niệm Systemd
- Systemd là một hệ thống khởi động và quản lý tiến trình (init system) được phát triển cho hệ điều hành Linux. Nó là một phần quan trọng của nhiều bản phân phối Linux. Systemd được thiết kế để cải thiện hiệu suất khởi động hệ thống và quản lý các tiến trình dễ dàng và linh hoạt hơn.





# Vai trò của Systemd trong hệ thống
- Bất cứ một chương trình nào trong Linux đều cần được thực thi dưới dạng một tiến trình (xem thêm Quản lý tiến trình trong Linux, và systemd cũng không ngoại lệ. Một trong các thành phần quan trọng này là khởi tạo hệ thống. Systemd cung cấp một chương trình đặc biệt là /sbin/init và nó sẽ là chương trình đầu tiên được khởi động trong hệ thống (PID = 1). Và khi hoạt động, /sbin/init sẽ giữ vai trò kích hoạt các file cấu hình cần thiết cho hệ thống, và các chương trình này sẽ tiếp nối để hoàn tất công đoạn khởi tạo.

# Các thành phần của Systemd

![]( https://www.linux.com/images/stories/41373/Systemd-components.png)

**1. Systemd Utilities**
| **Component** | **Description** |
|---------------|-----------------|
| systemctl     | Quản lý trạng thái của các dịch vụ hệ thống (bắt đầu, kết thúc, khởi động lại hoặc kiểm tra trạng thái hiện tại) |
| journald      | Quản lý nhật ký hoạt động của hệ thống (ghi log) |
| logind        | Quản lý và theo dõi việc đăng nhập/đăng xuất của người dùng |
| networkd      | Quản lý các kết nối mạng thông qua các cấu hình mạng |
| timedated     | Quản lý thời gian hệ thống hoặc thời gian mạng |
| udev          | Quản lý các thiết bị và firmware |


<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN0CVQoAVX1p5Z-sPXI3NOPftL9noaAUJnBA&usqp=CAU" style="width:500px;height:300px;">


**2. Systemd Daemons**
- Đây là các dịch vụ nền chạy dưới quyền quản lý của systemd

| **Daemon**        | **Description**                                                              |
|-------------------|------------------------------------------------------------------------------|
| systemd-logind    | Quản lý phiên đăng nhập và tương tác với người dùng                           |
| systemd-resolved  | Quản lý kết nối mạng và giải quyết tên miền                                   |
| systemd-networkd  | Quản lý cấu hình mạng                                                         |
| systemd-timesyncd | Đồng bộ thời gian hệ thống                                                   |

**3. Systemd cores**
- Tất cả các chương trình được quản lý bởi systemd đều được thực thi dưới dạng daemon hay background bên dưới nền và được cấu hình thành 1 file configuration gọi là unit file.

| **Service**  | **Description**                                   |
|--------------|---------------------------------------------------|
| service      | Quản lý hoạt động của một số chương trình          |
| socket       | Quản lý các kết nối                               |
| device       | Quản lý thiết bị                                  |
| mount        | Gắn thiết bị                                      |
| automount    | Tự động gắn thiết bị                              |
| swap         | Vùng không gian bộ nhớ trên đĩa cứng              |
| target       | Quản lý tạo liên kết                               |
| path         | Quản lý các đường dẫn                              |
| timer        | Dùng cho cron-job để lập lịch                     |
| snapshot     | Sao lưu                                           |
| slice        | Dùng cho quản lý tiến trình                        |
| scope        | Quy định không gian hoạt động                      |

![](https://1.bp.blogspot.com/-0Io5Fx0lCuo/X_nWDGr33VI/AAAAAAAADM0/LjCaSbLmnLMij22BWK-EpCBkKXb0gT5EACLcBGAsYHQ/w588-h451/Untitled%2BDiagram.jpg)

**Note**: Mặc dù là có 12 loại unit file trong systemd, tuy nhiên có lẽ service là loại thường được quan tâm nhất. Loại này sẽ được khởi động khi bật máy và luôn chạy ở chế độ nền (daemon hoặc background) Các service thường sẽ được cấu hình trong các file riêng biệt và được quản lý thông qua câu lệnh `systemctl`.

## Systemd Unit Files được tìn thấy ở đâu?
- Bản sao của hệ thống các tập tin đơn vị thường được lưu giữ trong thư mục `/lib/systemd/system`. Khi phần mềm cài đặt tập tin đơn vị trên hệ thống, đây là vị trí nơi họ được đặt theo mặc định.
![](https://scontent.xx.fbcdn.net/v/t1.15752-9/348992171_1654961894928511_8327556052688649805_n.png?stp=dst-png_p206x206&_nc_cat=107&ccb=1-7&_nc_sid=aee45a&_nc_ohc=l8vh6rdg9eEAX_YlsCb&_nc_oc=AQlG1Pot1PdU6IMBE4WD7uTVVzKMscWqOgz46bVSfCptfiKqiMBSsHS24BiDaGpmLAMTCbMyedBr1xwGwtuee-Pb&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQ4D_7REM1P0IHNCRdiiG3vgYnVewMmeEQW3XAzcSwLkQ&oe=64959594)
- Nếu bạn muốn thay đổi cách mà một đơn vị chức năng, vị trí tốt nhất để làm điều đó là trong thư mục `/etc/systemd/system/`
![](https://scontent.xx.fbcdn.net/v/t1.15752-9/346141882_792517359098690_3072946228129555804_n.png?_nc_cat=110&ccb=1-7&_nc_sid=aee45a&_nc_ohc=aSvRmdgGqFsAX-dmpJ_&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQPvW881Gw0AJhGdyh3XdIlgNh4yMlaXrzxYAKPJBLjBA&oe=6495B250)
- Ngoài ra còn có một vị trí cho định nghĩa đơn vị run-time ở `/run/systemd/system`

## Cấu trúc của một tập tin đơn vị
- Cơ cấu nội bộ các tập tin đơn vị được tổ chức với các section. section được biểu thị bằng một cặp dấu ngoặc vuông "[" và "]" với section name ở bên trong. Mỗi section mở rộng cho đến khi bắt đầu của section tiếp theo hoặc cho đến khi kết thúc của tập tin.

**1. [Unit] Section Directives**
- được sử dụng để xác định siêu dữ liệu cho các đơn vị và cấu hình các mối quan hệ của các đơn vị đến các đơn vị khác.
  
| Chỉ thị          | Mô tả                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Description=     | Chỉ thị này có thể được sử dụng để mô tả tên và chức năng cơ bản của các đơn vị.`                                                   |
| Documentation=   | Chỉ thị này cung cấp một vị trí cho một danh sách các URI cho tài liệu.`                                                             |
| Requires=        | Chỉ thị này liệt kê bất kỳ đơn vị mà đơn vị này chủ yếu phụ thuộc.`                                                                     |
| Wants=           | Chỉ thị này cũng tương tự như Requires=, nhưng ít nghiêm ngặt hơn.`                                                                     |
| BindsTo=         | Chỉ thị này cũng tương tự như Requires=, các đơn vị hiện tại dừng lại khi các đơn vị liên quan chấm dứt.`                               |
| Before=          | Các đơn vị được liệt kê trong chỉ thị này sẽ không được bắt đầu cho đến khi đơn vị hiện tại được đánh dấu là bắt đầu nếu chúng được kích hoạt cùng một lúc.` |
| After=           | Các đơn vị được liệt kê trong chỉ thị này sẽ được bắt đầu trước khi bắt đầu các đơn vị hiện tại.`                                       |

**2. [Install] Section Directives**
- Phần này là tùy chọn và được sử dụng để xác định hành vi hoặc một đơn vị nếu nó được kích hoạt hoặc vô hiệu hóa. Cho phép một đơn vị đánh dấu nó sẽ được tự động bắt đầu lúc khởi động.
- Bởi vì điều này, chỉ có một số ít các đơn vị có thể được kích hoạt sẽ có phần này. Các chỉ thị mô tả những gì sẽ xảy ra khi các đơn vị được.
  
| Chỉ thị           | Mô tả                                                                                                                                                                                              |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WantedBy=         | Chỉ thị này chỉ định các đơn vị mà đơn vị hiện tại là mong muốn (wanted by). Điều này có nghĩa là nếu các đơn vị được liệt kê ở đây được kích hoạt, thì đơn vị hiện tại sẽ được kích hoạt theo.`       |
| RequiredBy=       | Chỉ thị này chỉ định các đơn vị mà đơn vị hiện tại là bắt buộc (required by). Điều này có nghĩa là nếu các đơn vị được liệt kê ở đây không được kích hoạt, thì đơn vị hiện tại sẽ không thể kích hoạt.`   |
| Also=             | Chỉ thị này chỉ định các đơn vị khác mà đơn vị hiện tại cũng có thể được kích hoạt. Điều này tương đương với việc định nghĩa WantedBy= cho các đơn vị được liệt kê ở đây.`                           |
| Alias=            | Chỉ thị này cho phép đặt tên đơn vị hiện tại thành một alias (bí danh), cho phép kích hoạt đơn vị bằng cả tên gốc và tên alias.`                                                             |
**3. [Service]**
- Phần [Service] được sử dụng để cung cấp cấu hình mà chỉ áp dụng cho các dịch vụ.

| Chỉ thị             | Mô tả                                                                                                                                                                                                         |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type=               | Chỉ thị này xác định loại của dịch vụ. Các giá trị thông thường bao gồm: simple (mặc định), forking, oneshot, dbus, notify, idle, và các giá trị khác. Loại dịch vụ xác định cách systemd xử lý và quản lý dịch vụ.` |
| ExecStart=          | Chỉ thị này chỉ định chương trình hoặc tệp kịch bản được thực thi khi dịch vụ được khởi động.`                                                                                                                |
| ExecStop=           | Chỉ thị này chỉ định chương trình hoặc tệp kịch bản được thực thi khi dịch vụ được dừng.`                                                                                                                      |
| WorkingDirectory=   | Chỉ thị này chỉ định thư mục làm việc cho dịch vụ.`                                                                                                                                                          |
| User=               | Chỉ thị này chỉ định người dùng (user) được sử dụng để chạy dịch vụ.`                                                                                                                                          |
| Group=              | Chỉ thị này chỉ định nhóm (group) được sử dụng để chạy dịch vụ.`                                                                                                                                              |
| Restart=            | Chỉ thị này xác định cách systemd khởi động lại dịch vụ khi nó dừng.`                                                                                                                                           |
| RestartSec=         | Chỉ thị này xác định khoảng thời gian giữa các lần khởi động lại dịch vụ.`                                                                                                                                     |
| Environment=        | Chỉ thị này chỉ định các biến môi trường được sử dụng trong quá trình chạy dịch vụ.`                                                                                                                          |

**4. [Socket]**
- Phần [Socket] là rất phổ biến trong các cấu hình systemd vì nhiều dịch vụ thực hiện kích hoạt trên socket để cung cấp song song tốt hơn và linh hoạt. Mỗi đơn vị socket phải có một đơn vị dịch vụ phù hợp sẽ được kích hoạt khi socket nhận hoạt động.

| Chỉ thị             | Mô tả                                                                                                                                                                                               |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ListenStream=       | Chỉ thị này chỉ định cổng và giao thức mà socket lắng nghe kết nối.`                                                                                                                                  |
| ListenDatagram=     | Chỉ thị này chỉ định cổng và giao thức mà socket lắng nghe gói tin dữ liệu không kết nối (datagram).`                                                                                                |
| ListenSequentialPacket= | Chỉ thị này chỉ định cổng và giao thức mà socket lắng nghe gói tin dữ liệu tuần tự (sequential packet).`                                                                                      |
| ListenFIFO=         | Chỉ thị này chỉ định tệp FIFO mà socket lắng nghe kết nối.`                                                                                                                                          |
| ListenSpecial=      | Chỉ thị này chỉ định tên đặc biệt (special name) của socket mà socket lắng nghe kết nối.`                                                                                                           |
| Accept=             | Chỉ thị này xác định các đơn vị dịch vụ mà sẽ được kích hoạt khi có kết nối được chấp nhận trên socket.`                                                                                          |
| SocketMode=         | Chỉ thị này chỉ định quyền truy cập (permission mode) của socket. Ví dụ: 0666, 0600, v.v.`                                                                                                        |
| SocketUser=         | Chỉ thị này chỉ định người dùng (user) sở hữu socket.`                                                                                                                                               |
| SocketGroup=        | Chỉ thị này chỉ định nhóm (group) sở hữu socket.`                                                                                                                                                   |
| SocketService=      | Chỉ thị này chỉ định dịch vụ (service) được kích hoạt khi có kết nối được chấp nhận trên socket.`                                                                                                    |
| BindIPv6Only=       | Chỉ thị này xác định xem socket chỉ ràng buộc đến địa chỉ IPv6 hay không.`                                                                                                                          |
**5. [Path]**
- Phần [Path] xác định một đường dẫn hệ thống tập tin mà systemd có thể theo dõi các thay đổi

| Chỉ thị             | Mô tả                                                                                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PathExists=         | Chỉ thị này chỉ định đường dẫn tệp (file path) mà systemd sẽ kiểm tra xem có tồn tại hay không. Nếu tệp tồn tại, đơn vị được kích hoạt.`                      |
| PathExistsGlob=     | Chỉ thị này cho phép bạn sử dụng các biểu thức chính quy (glob pattern) để kiểm tra tồn tại của nhiều tệp.`                                            |
| Unit=               | Chỉ thị này chỉ định đơn vị mà systemd sẽ kích hoạt khi điều kiện đường dẫn được đáp ứng. Đơn vị này được kích hoạt theo mặc định.`                         |
| MakeDirectory=      | Chỉ thị này cho phép systemd tạo thư mục (directory) nếu nó không tồn tại. Thư mục mới được tạo trước khi đơn vị được kích hoạt.`                         |
| DirectoryNotEmpty=  | Chỉ thị này chỉ định đường dẫn thư mục (directory path) mà systemd sẽ kiểm tra xem có rỗng hay không. Nếu thư mục không rỗng, đơn vị được kích hoạt.`    |
| TriggeredBy=        | Chỉ thị này cho phép bạn chỉ định đơn vị hoặc đường dẫn mà khi thay đổi, đơn vị hiện tại sẽ được kích hoạt. Điều này giúp tạo ra mối phụ thuộc động.`        |
| WatchPaths=         | Chỉ thị này cho phép bạn theo dõi các đường dẫn tệp (file path) và kích hoạt đơn vị khi các tệp thay đổi. Điều này thích hợp để theo dõi tệp log hoặc cấu hình.` |

**6. [Mount]**
- Đơn vị gắn kết cho phép quản lý điểm gắn kết từ bên trong systemd
  
| Chỉ thị             | Mô tả                                                                                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PathExists=         | Chỉ thị này chỉ định đường dẫn tệp (file path) mà systemd sẽ kiểm tra xem có tồn tại hay không. Nếu tệp tồn tại, đơn vị được kích hoạt.`                      |
| PathExistsGlob=     | Chỉ thị này cho phép bạn sử dụng các biểu thức chính quy (glob pattern) để kiểm tra tồn tại của nhiều tệp.`                                            |
| Unit=               | Chỉ thị này chỉ định đơn vị mà systemd sẽ kích hoạt khi điều kiện đường dẫn được đáp ứng. Đơn vị này được kích hoạt theo mặc định.`                         |
| MakeDirectory=      | Chỉ thị này cho phép systemd tạo thư mục (directory) nếu nó không tồn tại. Thư mục mới được tạo trước khi đơn vị được kích hoạt.`                         |
| DirectoryNotEmpty=  | Chỉ thị này chỉ định đường dẫn thư mục (directory path) mà systemd sẽ kiểm tra xem có rỗng hay không. Nếu thư mục không rỗng, đơn vị được kích hoạt.`    |
| TriggeredBy=        | Chỉ thị này cho phép bạn chỉ định đơn vị hoặc đường dẫn mà khi thay đổi, đơn vị hiện tại sẽ được kích hoạt. Điều này giúp tạo ra mối phụ thuộc động.`        |
| WatchPaths=         | Chỉ thị này cho phép bạn theo dõi các đường dẫn tệp (file path) và kích hoạt đơn vị khi các tệp thay đổi. Điều này thích hợp để theo dõi tệp log hoặc cấu hình.` |

**6.[Swap]**
- Phần [Swap] được sử dụng để cấu hình không gian trao đổi trên hệ thống. 

| Chỉ thị             | Mô tả                                                                                                                                               |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| What=               | Chỉ thị này chỉ định thiết bị hoặc đường dẫn tệp (file path) cho phân vùng swap.`                                                                   |
| Options=            | Chỉ thị này cho phép bạn chỉ định các tùy chọn (options) khác nhau cho quá trình kích hoạt swap. Ví dụ: pri=, discard, noauto, v.v.`                  |
| Priority=           | Chỉ thị này chỉ định ưu tiên (priority) của swap. Giá trị càng thấp, ưu tiên càng cao. Giá trị mặc định là 100.`                                     |
| TimeoutSec=         | Chỉ thị này chỉ định thời gian chờ (timeout) để kích hoạt swap trước khi bỏ qua. Giá trị mặc định là 90s.`                                         |
| ExecStartPre=       | Chỉ thị này cho phép bạn chỉ định các chương trình hoặc tệp kịch bản được thực thi trước quá trình kích hoạt swap.`                                   |
| ExecStartPost=      | Chỉ thị này cho phép bạn chỉ định các chương trình hoặc tệp kịch bản được thực thi sau quá trình kích hoạt swap.`                                     |
| ExecStopPre=        | Chỉ thị này cho phép bạn chỉ định các chương trình hoặc tệp kịch bản được thực thi trước quá trình tắt swap.`                                         |
| ExecStopPost=       | Chỉ thị này cho phép bạn chỉ định các chương trình hoặc tệp kịch bản được thực thi sau quá trình tắt swap.`                                           |

#### Tài liệu tham khảo:

https://viblo.asia/p/tim-hieu-va-van-dung-systemd-de-quan-ly-he-thong-linux-phan-co-ban-WAyK8kN65xX
https://systemd.io/
https://man7.org/linux/man-pages/man1/init.1.html





