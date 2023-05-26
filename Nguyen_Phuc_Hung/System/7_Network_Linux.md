# Giới thiệu về mạng trong Linux

Mạng trong hệ thống Linux đóng vai trò quan trọng trong việc kết nối các thiết bị và cho phép truyền thông dữ liệu giữa chúng. Mạng là một hệ thống gồm các thiết bị, giao thức và dịch vụ nhằm tạo ra sự liên kết và giao tiếp thông tin giữa các máy tính và thiết bị khác nhau.

### Mạng trong Linux có nhiều vai trò quan trọng, bao gồm:

1. Kết nối máy tính: Mạng cho phép các máy tính trong hệ thống Linux kết nối với nhau thông qua giao thức và cơ chế truyền thông.
2. Chia sẻ tài nguyên: Mạng trong Linux cho phép chia sẻ tài nguyên như máy in, ổ đĩa, thư mục chia sẻ và dịch vụ khác giữa các máy tính trong mạng.
3. Truy cập mạng và internet: Mạng trong Linux cung cấp khả năng truy cập vào mạng nội bộ và internet, cho phép truyền thông dữ liệu và truy cập các dịch vụ và tài nguyên trên mạng.

# Kiến trúc mạng trong Linux

| Khái niệm             | Mô tả                                                                                                                                               |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Giao diện mạng       | Là phần cứng hoặc phần mềm kết nối máy tính với mạng. Giao diện mạng có thể là card mạng vật lý (ethernet, Wi-Fi, v.v.) hoặc giao diện mạng ảo.         |
| Giao diện mạng vật lý | Đại diện cho card mạng được gắn vào máy tính, như card ethernet hoặc card Wi-Fi.                                                                    |
| Giao diện mạng ảo    | Được tạo ra để mô phỏng giao diện mạng vật lý, thường được sử dụng trong các môi trường ảo hóa.                                                       |
| IP (Internet Protocol) | Là giao thức truyền thông dữ liệu trong mạng Internet. IP định danh và địa chỉ các thiết bị trong mạng và quản lý việc chuyển tiếp dữ liệu giữa chúng. |
| Routing (Định tuyến) | Là quá trình chọn lựa đường đi tối ưu cho gói tin từ nguồn đến đích trong mạng. Routing có vai trò quan trọng trong việc kết nối các mạng con và định tuyến dữ liệu giữa chúng. |
| Tường lửa (Firewall) | Là hệ thống kiểm soát truy cập và bảo vệ mạng bằng cách lọc các gói tin dựa trên các quy tắc được cấu hình trước.                                      |

| Khái niệm                  | Mô tả                                                                                                                                                               |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DNS (Domain Name System)  | Là hệ thống giúp chuyển đổi tên miền (domain name) thành địa chỉ IP và ngược lại. DNS cho phép dễ dàng truy cập và giao tiếp qua tên miền thay vì phải ghi nhớ địa chỉ IP. |
| DHCP (Dynamic Host Configuration Protocol) | Là giao thức tự động cấu hình địa chỉ IP, subnet mask, gateway và các thông tin mạng khác cho các thiết bị trong mạng. DHCP giúp đơn giản hóa quá trình cấu hình mạng và tự động phân phối địa chỉ IP cho các thiết bị mới kết nối vào mạng. |
| NAT (Network Address Translation) | Là kỹ thuật cho phép chuyển đổi địa chỉ IP trong gói tin khi truyền qua các thiết bị mạng, giúp tiết kiệm địa chỉ IP công cộng và bảo mật mạng. |
| VLAN (Virtual Local Area Network) | Là phương pháp tạo ra các mạng ảo trong mạng vật lý. VLAN cho phép chia mạng thành các phân đoạn nhỏ hơn, giúp tăng tính bảo mật và quản lý mạng hiệu quả hơn. |

# Quản lý giao diện mạng trong Linux

1. Ifconfig

ifconfig là viết tắt của interface configurator tức là trình cấu hình giao diện mạng. Đây là một trong những lệnh cơ bản nhất được sử dụng trong việc kiểm tra mạng. 

Ta sẽ thu được các thông tin cơ bản về cấu hình mạng khi sử dụng ifconfig như: địa chỉ ip, địa chỉ mac, MTU (Maxium Transmission Unit - là kích thước gói dữ liệu lớn nhất, được đo bằng byte, có thể truyền tải qua một mạng lưới). Lệnh này thường được sử dụng để đặt hoặc hiển thị địa chỉ IP và netmask của giao diện mạng. Nó cũng cung cấp các lệnh để bật hoặc tắt một giao diện mạng.

**Các câu lệnh hay dùng**
- `ifconfig -a` - Liệt kê tất cả các inteface hiện đang có, kể cả các interface không sử dụng.

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/348378829_2609892355834231_3610153947725405629_n.png?stp=dst-png_s350x350&_nc_cat=100&ccb=1-7&_nc_sid=aee45a&_nc_ohc=ejedovI_GBwAX-j8JRq&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRov4ricofv9xocZAd95qDhnftNUC-FGdN9UcSUt0JKpA&oe=64965FD4)

- `ifconfig <interface>` - Thông tin chi tiết của một interface cụ thể.

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/349032280_169862409383386_6981586810560305988_n.png?stp=dst-png_s843x403&_nc_cat=103&ccb=1-7&_nc_sid=aee45a&_nc_ohc=ZsqPXB5GiI4AX-C2_aS&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdTSbYf22sJ20gF4PvcAEV3QSQB77ZrpKCXVh6EUrXnggg&oe=64964AB6)

- `ifup <interface>` hay `ifdown <interface>` - Để bật hay tắt một interface.

**2. IP**
ip như là một phiên bản cập nhật và mới nhất của lệnh ifconfig. Lệnh ip tương tự như ifconfig, nhưng mạnh mẽ hơn rất nhiều. 

- `ip a` - Lệnh này cung cấp thông tin chi tiết của tất cả các mạng như ifconfig.

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/349295004_183503590971945_3757597359617091393_n.png?stp=dst-png_p206x206&_nc_cat=109&ccb=1-7&_nc_sid=aee45a&_nc_ohc=2IX19PTM9uUAX8EkZOY&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdR_DTxrVU9D8k3Qsj9nfAceUfg-evMsZWFzBTJV_1kJpA&oe=649657DE)
- `ip link` - Cấu hình, thêm và xóa các interface. Sử dụng `ip link show` để hiển thị tất cả các interface trên hệ thống.

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/346150977_247911884557436_8389278809770330972_n.png?_nc_cat=101&ccb=1-7&_nc_sid=aee45a&_nc_ohc=WhnA2PpryZoAX8kD7r1&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQkFIOBYHIgZaTNmiZHkS-qMVEGiJR9rqaoElTrzUkEWw&oe=64964B59)
- `ip address` - Hiển thị địa chỉ ip, gắn địa chỉ ip mới hoặc xóa địa chỉ ip chỉ cũ.

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/346164149_3351878721741997_1257281868554523120_n.png?stp=dst-png_p206x206&_nc_cat=103&ccb=1-7&_nc_sid=aee45a&_nc_ohc=4fyBsL7AXjAAX_RYZv4&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdSNZbjNjwPbZdovZqo-C3ormYaY1S89xh73lcJf8RdW9g&oe=64964EC4)
- `ip route` - Được sử dụng để Cấu hình quản lý bảng định tuyến.

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/349039197_1629082350908378_7109849201836240558_n.png?_nc_cat=100&ccb=1-7&_nc_sid=aee45a&_nc_ohc=CyUe01Zm1nsAX_UfR2F&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdR4P4m5ITM_ObHdjbKWl1Uo0LHSjyb8q699Tvid0PcWDw&oe=64965F21)

**3. Hostname**
- Lệnh hostname trong Linux được sử dụng để xem hoặc thay đổi tên hostname hoặc system’s domain. Nó cũng có thể được dùng kiểm tra địa chỉ IP của máy tính.

- Một số cú pháp lệnh hostname:

`hostname` - Hiển thị hostname

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/346151000_263879916212399_4430877610223846293_n.png?_nc_cat=103&ccb=1-7&_nc_sid=aee45a&_nc_ohc=xwbASAjAVJwAX8nDfl6&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQ-4sianAe2hf6MVT8imN5YTugdkJWbmGQUfmvPkFDBPA&oe=649647F4)

`hostname --all-ip-addresses` - Hiển thị tất cả các địa chỉ IP

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/348925219_293530773018015_5352291239697458507_n.png?_nc_cat=105&ccb=1-7&_nc_sid=aee45a&_nc_ohc=P64gexYlrsEAX_sVaAm&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdTRl4IVln7EeuHSh5_v3ydQzSHmmD2AinmqJxhmf8iwow&oe=64965892)

`sudo hostname <new hostname>` - Thay đổi hostname. Tuy nhiên thay đổi bằng hostname chỉ tạm thời. Sau khi reboot, hostname sẽ bị đưa trở về như cũ.

**4. Ping**

- Về cơ bản, ping kiểm tra kết nối giữa 2 nút trong 1 mạng. Nó sẽ gửi các gói tin echo ICMP (Internet Control Message Protocol) và chờ đợi phản hồi. Khi những gói tin echo này được gửi đến 1 nút mạng, nút mạng đó phản hồi lại các gói tin này nếu nó đang hoạt động và đang kết nối.

- Kết quả ping giữa 2 nút mạng sẽ cho ta những thông tin hữu ích như:

+Tình trạng của nút đích: nó có kết nối được tới được không
+Thời gian một vòng di chuyển giữa 2 nút: Host–Computer-Host
+Phần trăm lượng packet bị mất trong quá trình truyền

- Một số cú pháp lệnh ping:

`ping <destination>` - Lệnh ping gửi gói tin echo ICMP để kiểm tra kết nối mạng, destination có thể là tên miền hoặc địa chỉ ip trực tiếp
`ping -c <number> <destination>` - giới hạn số lượng gói tin bằng cách thêm " -c " vào lệnh ping.

**5. Traceroute**

- Nếu như sử dụng ping hiển thị cho bạn thấy các gói tin bị mất mát trong kết nối thì traceroute cho thấy đường đi được sử dụng, trình tự các cổng mà các gói tin đi qua để có thể đến được đích. traceroute chính là một trong những lệnh hữu ích nhất trong khắc phục sự cố mạng qua những thông tin mà lệnh nàu cung cấp gồm:

+Cung cấp tên và xác định mọi thiết bị trên đường dẫn.
+Theo dõi lộ trình để đến đích của gói tin.
+Xác định và chỉ ra vị trí các sự cố trong kết nối mạng, độ trễ trong kết nối mạng đến từ đâu.

| Tùy chọn | Mô tả                                     | Ví dụ                  |
|----------|------------------------------------------|------------------------|
| -I       | Sử dụng gói tin ICMP                      | `traceroute -I google.com` |
| -U       | Sử dụng gói tin UDP                       | `traceroute -U facebook.com` |
| -p       | Thiết lập số cổng UDP                     | `traceroute -p 1234 example.com` |
| -m       | Giới hạn số lượng hop                     | `traceroute -m 15 yahoo.com` |

**6. nslookup**

- nslookup là lệnh được sử dụng để thực hiện các tra cứu liên quan đến DNS. nslookup có thể cho chúng ta biết các thông tin quan trọng như MX records và địa chỉ IP liên kết với tên miền.

| Tùy chọn         | Mô tả                                                 | Ví dụ                        |
|------------------|------------------------------------------------------|-----------------------------|
| `-query=TYPE`    | Xác định loại truy vấn (A, AAAA, CNAME, MX, v.v.)       | `nslookup -query=MX google.com`   |
| `-debug`         | Bật chế độ gỡ lỗi để xem thông tin chi tiết           | `nslookup -debug google.com`      |
| `-type=TYPE`     | Thiết lập loại truy vấn                                | `nslookup -type=PTR 8.8.8.8`      |
| `-timeout=N`     | Thiết lập thời gian chờ (giây)                        | `nslookup -timeout=5 google.com`  |
| `-port=PORT`     | Thiết lập cổng sử dụng                                | `nslookup -port=5353 google.com`  |
| `-server=IP`     | Thiết lập máy chủ DNS để truy vấn                      | `nslookup -server=8.8.8.8 google.com` |
| `-all`           | Hiển thị tất cả các thông tin của một tên miền         | `nslookup -all google.com`         |
| `-vc`            | Sử dụng kết nối TCP cho truy vấn                       | `nslookup -vc google.com`          |
| `-d2`            | Hiển thị thông tin gỡ lỗi cấp độ 2                     | `nslookup -d2 google.com`          |

# Cấu hình IP tĩnh cho máy ảo Centos 7
B1: Sử dụng vi để chỉnh sửa file `/etc/sysconfig/network-scripts/ifcfg-ens33`

```sh
/etc/sysconfig/network-scripts/ifcfg-ens33
```



![](https://scontent.xx.fbcdn.net/v/t1.15752-9/349131313_718436633391907_794840876381253378_n.png?_nc_cat=103&ccb=1-7&_nc_sid=aee45a&_nc_ohc=Ntp42RooJGIAX9avOU-&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRI8J3qt0225Z__FBa-6dldwEEbJ8Ch4XIKo_U5oIKs9w&oe=6496AFEB)

 
B2: Cấu hình file

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/346168099_278032504654894_6677328590535194845_n.png?stp=dst-png_p235x165&_nc_cat=105&ccb=1-7&_nc_sid=aee45a&_nc_ohc=T1HmspFZeLkAX8oW8-x&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdTDu3AgXaBdzxFY1sY-8tKKrjhBjnftrM1a20enm1X3lA&oe=6496B3B8)
 
B3: Restart network service
![](https://scontent.xx.fbcdn.net/v/t1.15752-9/349073244_178827398464952_5130170281218097449_n.png?_nc_cat=105&ccb=1-7&_nc_sid=aee45a&_nc_ohc=Qc2RDoEACRYAX-3PcMV&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdTl4Nim8qKxdmi5H1FyCd6oVA8jMtAdy8-EpK4ziuLQ_g&oe=6496A29A)

B4: Kiểm tra xem mạng đã thông chưa, dùng ping

```sh
ping 8.8.8.8
```
![](https://scontent.xx.fbcdn.net/v/t1.15752-9/349037977_769738248132981_5639522987305232310_n.png?_nc_cat=101&ccb=1-7&_nc_sid=aee45a&_nc_ohc=xVxiqXENpuIAX8ILMZZ&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdSZNMos81KtQerIl-1IHkANv7_hzk9WrW0wQZjl91Fcbg&oe=6496B109)

 
