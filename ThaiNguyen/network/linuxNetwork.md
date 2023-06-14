## các lệnh tương tác
1. ifconfig
hiển thị IP address của 3 network: ethernet, local network, và WLAN
``` 
ifconfig [..options] [interface]
```
### command: 
- eth0: ethernet
- lo: local network
- wlan0: WLAN
###Options:
- -a: hiển thị tất cả các interface hiện có
- -s: hiển thị thông tin từ ifconfig dưới dạng danh sách ngắn
- -v: hiển thị thông tin có thêm nhiều chi tiết hơn so với -s
- [interface] up: khởi động interface chỉ định
- [interface] down: vô hiệu hóa interface chỉ định
- add addr /prefixlen: thêm một địa chỉ IP vào interface(IPv6)
- del addr /prefixlen: bỏ một địa chỉ IP vào interface(IPv6)
- [-]promisc:bật hoặc tắt chế độ promiscuous, là chế độ cho phép interface nhận tất cả các packet trên network
- mtusize N:
cho phép người dùng đặt Maximum transfer size, là size lớn nhất của 1 data packet trên network
+ Syntax như sau
```
ifconfig interface_name mtusize size
```
2. ip
dùng để quản lý địa chỉ IP và network
```
ip [options] object {command}
```
options:
- address: hiển thị địa chỉ IP
- address show [interface]: hiển thị địa chỉ IP của một interface nhất định
- link: hiển thị thông tin từ data link layer
nếu cần hiển thị thêm thông tin có thể làm như sau, thêm tên của interface nếu cần hiển thị cụ thể:
```
ip -s link (interface name)
```
- route: hiển thị thông tin từ routing table:
+ hiển thị routing table:
```
ip route show
```
+thêm route mới vào routing table
``` 
ip route add [network] via [gateway] dev [interface]
```
+ xóa route:
```
ip route delete [network] 
```
+ thay đổi route đang có:
``` 
ip route change [network] via [gateway] dev [interface]
```
- add: thêm địa chỉ IP vào interface
```
ip a add [ip_address] dev (interface)
```
- del: xóa địa chỉ IP khỏi interface
```
ip a del [ip_address] dev (interface)
```
- up: bật interface
```
ip link set (interface) up
```
- down: tắt interface
```
ip link set (interface) down 
```
- neighbour: xem MAC address của các thiết bị đang được kết nối với network
```
ip neighbour
```
3. traceroute
- hiển thị địa chỉ IP mà các packet phải đi qua để tới điểm đến
```
traceroute [options] [destination] 
```
options:
- -4: dùng IPv4
- -6: dùng IPv6
- -F: không chia nhỏ packet
- -g gate: route packet qua gate chỉ định
- -m max_hop: đặt số hop tối đa để packet có thể tới được điểm đến
- -p Port: đặt port chỉ định cho điểm đến của packet
- -q num: đặt số probe cho mỗi hop, số mặc định là 3
4. ping : kiểm tra thời gian phản hồi khi gửi packet đến một địa chỉ
```
ping [destination]
```
option :
- -c num: số packet cần gửi trước khi dừng
- -i num: đặt thời gian trước khi gửi packet
- -s size: đặt kích cỡ của packet
- -W timeout: đặt thời gian timeout khi đang đợi phản hồi
5. netstat
- dùng để hiển thị thông tin về network
```
netstat [options] 
```
options:
- -t : hiển thị tất cả TCP Port
- -u: hiển thị tất cả UDP Port
- -l: hiển thị listening port
- -s: hiển thị tất cả thông số của tất cả các port
- -r: hiển thị routing table
- -i: hiển thị thông số của interface
6. dig
```
dig [server name] [commands]
```
commands:
- +short: rút ngắn lượng thông tin, thường chỉ hiển thị mỗi địa chỉ IP
- +nocomments: bỏ comments
- +noall: xóa hết displayflag
- +trace: trace DNS path
- +stats: hiển thị thông số
7. route
- dùng khi người dùng muốn sử dụng route table
+ hiển thị route table:
```
route
```
+ hiển thị route table bản đầy đủ hơn:
```
route -n
```
+ thêm default gateway
```
route add default gw [ip]
```
+ từ chối routing đến một host hoặc network cụ thể
```
route add - host [ip] reject
```
8. host
- dùng để tìm địa chỉ IP cho hostname và tìm domain name cho IP address
```
host [website name/IP]
```
9. wget
- công cụ dùng để lấy nội dung và file từ các máy chủ khác nhau
```
wget [options] [URL]
```
options: 
- O: xác định tên file và vị trí trong thư mục để lưu file vừa tải
- P: xác định tên directory để lưu file
- r : recursive downloading, wget có thể truy cập và tải các file từ các link trong URL
- N: tải file nếu như file đó là bản mới hơn của bản được lưu trong thư mục
- c: tiếp tục tải 1 file đang trong trạng thái dừng tải
10. curl
chức năng giống wget
```
curl [options] [URL]
```
Options:
-o filename: lưu file với tên được chỉ định
-O : lưu file cùng tên với URL
-C: tiếp tục download file đang download dở
--limit-rate [value]: giới hạn băng thông xuống 1 giá trị nhất định

Nguồn tham khảo:
1. [Nguồn 1](https://www.geeksforgeeks.org/)
2. [Nguồn 2](https://mindmajix.com/linux-networking-commands-best-examples)


