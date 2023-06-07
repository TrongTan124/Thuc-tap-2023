## Định nghĩa:
+  LAN(local area network):
- một nhóm các hệ thống máy tính được kết nối với nhau trên một khu vực có diện tích nhỏ

![LAN](./images/LAN.png)

+  VLAN(Virtual LAN): là một nhóm máy tính được kết nối bằng một mạng LAN ảo, không kể khoảng cách địa lý giữa chúng

Broadcast domain là một phân đoạn mạng trong đó khi một thiết bị phát một gói, tất cả các thiết bị trên domain đó sẽ nhận được nó. Broadcast domain thường chỉ giới hạn ở các bộ chuyển mạch.

Phạm vi Vlan
- VLAN 0,4095: dành riêng cho VLAN không thể nhìn thấy hoặc sử dụng
- VLAN 1: VLAN mặc định của switch. không thể xóa hoặc chỉnh sửa nhưng có thể được sử dụng.
- VLAN 2-1001: đây là dải VLAN thông thường và có thể tạo, chỉnh sửa và xóa.
- VLAN 1002-1005: dùng cho FDDI và token ring. không thể bị xóa.
- VLAN 1006-4094: phạm vi mở rộng của VLAN

Token ring:
- là một giao thức truyền thông trong đó tất cả các thiết bị được kết nối trong một vòng. Mã thông báo(token) thường ở dạng mẫu bit đặc biệt hoặc gói tin nhỏ và được chuyển qua các thiết bị theo thứ tự được xác định trước. Nếu một thiết bị có dữ liệu đang chờ gửi và nhận được mã thông báo, thiết bị sẽ gửi những dữ liệu đó sau đó chuyển mã thông báo sang thiết bị tiếp theo. Nếu không, nó sẽ chỉ chuyển mã thông báo sang thiết bị tiếp theo.

FDDI(Fiber Distributed Data Interface):
- - là bộ tiêu chuẩn truyền dữ liệu trong mạng LAN qua cáp quang. Có thể mở rộng kết nối lên đến 200km. Nó dựa trên giao thức token ring.

Các tính năng chính:
1. VLAN tagging: là phương pháp xác định và phân biệt lưu lượng VLAN với lưu lượng mạng khác, thường bằng cách thêm thẻ VLAN vào tiêu đề khung Ethernet
2. Tư cách thành viên Vlan: chỉ định các thiết bị mạng cho các Vlan cụ thể
+ static VLANs: người quản trị mạng tạo VLAN và gán port của switch vào VLAN (còn gọi là port-based VLAN). Các cổng VLAN không thay đổi cho đến khi quản trị viên thay đổi việc gán cổng
+ Dynamic VLAN: switch tự động gán port vào một VLAN sử dụng thông tin từ người dùng như địa chỉ MAC hoặc địa chỉ IP. Khi một thiết bị được kết nối với một công tắc, switch sẽ tra cứu cơ sở dữ liệu để thiết lập tư cách thành viên Vlan. Khi chúng tôi di chuyển một thiết bị từ một port trên một switch này sang một switch khác, dynamic VLAN sẽ tự động định cấu hình tư cách thành viên của Vlan.
3. VLAN trunking: cho phép nhiều VLAN được truyền qua một liên kết vật lý duy nhất.
### Trunking 

