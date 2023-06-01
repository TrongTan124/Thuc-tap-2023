## Định nghĩa
Mô hình OSI vạch ra các giao thức chuẩn cho máy tính để thiết lập giao tiếp qua mạng.
## Ưu điểm khi sử dụng mô hình OSI
1. Troubleshooting :Mặc dù internet ngày nay không tuân thủ nghiêm ngặt mô hình OSI, nhưng mô hình OSI rất hữu ích để khắc phục sự cố mạng. Mô hình OSI là mô hình phân tầng được tạo thành từ các lớp độc lập, nghĩa là những thay đổi trong một tầng không ảnh hưởng đến các tầng khác. Nó giúp phân tích vấn đề và cô lập các vấn đề trong mạng do được chia thành nhiều lớp độc lập. 
2. Khả năng tương tác: bằng cách cung cấp các giao diện và giao thức chuẩn cho từng lớp, mô hình OSI đảm bảo rằng các thiết bị mạng từ các nhà cung cấp khác nhau có thể hoạt động liền mạch với nhau.
3. Khả năng mở rộng: mỗi lớp hoạt động dựa trên thông tin nhận được từ lớp bên trên, nhưng mỗi lớp xử lý thông tin đó theo cách độc lập với các lớp trước đó. Điều này cho phép thêm các lớp, công nghệ hoặc giao thức bổ sung nếu cần vào một lớp mà không ảnh hưởng đến chức năng của các lớp khác.

### OSI model:

![OSI](./images/Osi_model.png)
 
 OSI được chia ra làm 7 lớp: 
 7. Application layer:
- trực tiếp tương tác với dữ liệu từ người dùng
- bao gồm các protocol và dữ liệu được dùng bởi phần mềm mà người dùng sử dụng như email hay trình duyệt web
6. Presentation layer:
- phụ trách xử lý dữ liệu bằng việc dịch, giải nén hoặc nén, và mã hóa dữ liệu
5. Session layer:
- phụ trách việc thiết lập, duy trì và hủy bỏ các session(phiên liên lạc) giữa các máy
4. Transport: 
- transport layer quản lý việc trao đổi dữ liệu giữa 2 thiết bị
- cung cấp phân đoạn dữ liệu thành các gói và cung cấp kiểm soát luồng và lỗi để đảm bảo truyền dữ liệu thích hợp
- thêm số cổng nguồn và đích vào các gói dữ liệu trước khi chuyển tiếp đến lớp network
- thực hiện việc tập hợp lại các gói dữ liệu (đối với TCP) theo số thứ tự của chúng.
3. Network: 
- chịu trách nhiệm quản lý việc trao đổi thông tin giữa các network khác nhau
- sử dụng router để kết nối các network:
	+ router kết nối với ISP(internet service provider)
	+ router có thể chọn lựa quãng đường thuận tiện nhất để gửi dữ liệu dưới dạng packets
	+ lưu thông tin về địa chỉ IP và routing information bằng routing table
2. Data link: chịu trách nhiệm trong việc điều khiển luồng và phát hiện lỗi (error-detection)
1. Physical layer: bao gồm tất cả các hardware để vận hành network ví dụ như cable, router,...

TCP/IP






