# Mô hình OSI là gì ?
**1. Khái quát về mô hình OSI**

   **Mô hình OSI là gì?**
- OSI là mô hình tham chiếu kết nối hệ thống mở. Mô hình này được tạo nên nhờ vào nguyên lý phân tầng, giải thích về kỹ thuật kết nối giữa các máy tính và thiết lập giao thức mạng giữa các máy tính đó. Mô hình OSI còn được gọi là mô hình bảy tầng.
![](https://www.bkns.vn/wp-content/uploads/2022/09/osi-la-mo-hinh-tham-chieu-ket-noi-he-thong-mo.png.webp)

- Mô hình OSI chia giao tiếp mạng thành 7 tầng. Từ tầng 1 đến tầng 4 là là những lớp thuộc cấp thấp, nó thực hiện nhiệm vụ di chuyển dữ liệu. Từ tầng 5 đến tầng 7 là lớp thuộc cấp cao, thực hiện nhiệm vụ đặc thù và chuyển tiếp dữ liệu. Cụ thể:

| Lớp       | Chức năng                                                                                                                                                  |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Vật lý    | Đảm bảo truyền/nhận các chuỗi bit qua các phương tiện vật lý. (Xây dựng đường truyền vật lý cho các host)                                                    |
| Liên kết dữ liệu | Tạo/Gỡ bỏ khung thông tin (Frames), kiểm soát luồng và kiểm soát lỗi (Xác định cách dữ liệu được định dạng để truyền và kiểm soát truy cập vào mạng. Cung cấp phát hiện lỗi) (Điều khiển truy cập vào đường truyền vật lý) |
| Mạng      | Chọn đường và đảm bảo trao đổi thông tin trong mạng với công nghệ chuyển mạch thích hợp (Định tuyến gói dữ liệu, Chọn đường đi tốt nhất để gửi dữ liệu, Cung cấp địa chỉ logic và lựa chọn đường đi)               |
| Vận chuyển | Vận chuyển thông tin giữa các máy chủ (Kết nối từ đầu đến cuối). Kiểm soát lỗi và luồng dữ liệu (Xử lý các vấn đề vận chuyển giữa các máy chủ, Đảm bảo độ tin cậy trong vận chuyển dữ liệu, Thiết lập, duy trì và kết thúc mạch ảo, Cung cấp tính tin cậy qua việc phát hiện và khôi phục dữ liệu, Kiểm soát luồng) |
| Phiên     | Quản lý phiên truyền thông giữa các ứng dụng (Giao tiếp giữa các máy chủ: Thiết lập, quản lý và kết thúc phiên truyền thông giữa các ứng dụng)                                  |
| Trình bày | Chuyển đổi cú pháp dữ liệu để đảm bảo dữ liệu có thể đọc được bởi hệ thống nhận, Định dạng dữ liệu, Cấu trúc dữ liệu, đàm phán cú pháp truyền dữ liệu cho lớp ứng dụng, cung cấp mã hóa)                                      |
| Ứng dụng  | Cung cấp dịch vụ mạng cho các quy trình ứng dụng (như thư điện tử, truyền tệp và mô phỏng terminal), Cung cấp xác thực người dùng)                                  |

Những ưu điểm của OSI đó là:

- OSI phân thành nhiều tầng nhỏ và đơn giản hơn.
- OSI chuẩn hóa các thành phần mạng để phát triển dễ dàng hơn.
- OSI chuẩn hóa giao diện giữa các tầng.
- Dữ liệu được truyền nhanh chóng và dễ dàng hơn.

![](https://www.bkns.vn/wp-content/uploads/2022/09/osi-chia-giao-tiep-mang-thanh-7-tang.jpg.webp)

**2. Data Encapsulation, De-Encapsulation**
![](https://github.com/TrongTan124/Thuc-tap-VNPT/raw/main/MinhNN/CCNA/images/osi2.jpg)

- Đầu tiên sender sẽ gửi xuống user data dữ liệu người dùng, dữ liệu người dùng đi vào lớp Application, nó được đóng thêm một cái L7 HDR (Layer7 Header). Header là phần thông tin quản lý của 1 gói tin. Gói tin sẽ gồm 2 phần, phần dữ liệu và phần header. Đến lớp Presentation, toàn bộ nội dung của gói tin lớp 7 trở thành data của gói tin lớp 6, nội dung của gói tin lớp 7 sẽ được đóng thêm L6 HDR (Layer6 Header). Mỗi lần gói tin đi xuống 1 lớp, lại được bọc thêm 1 Header. Đến layer2, ngoài việc bọc thêm L2 HDR, nó còn kiểm tra thêm lỗi FCS. Khi đi xuống lớp Physical, toàn bộ dữ liệu sẽ được chuyển thành bits nhị phân để truyền trên đường truyền vật lý.
- Ngược lại đối với quy trình De-Encapsulation

# Mô hình TCP/IP là gì ?
**1. Giao Thức TCP/IP Là Gì?**
- TCP/IP là viết tắt của từ gì? Transmission Control Protocol/ Internet Protocol, tạm dịch là “Giao thức điều khiển truyền nhận/ Giao thức liên mạng”.

- TCP IP là gì? TCP/ IP là một bộ giao thức trao đổi thông tin, được dùng để truyền tải, kết nối các thiết bị trong mạng internet. Phương thức truyền dẫn này được sử dụng khá phổ biến trong internet hiện nay.

![](https://fptcloud.com/wp-content/uploads/2022/01/TCP-co-chuc-nang-xac-dinh-cac-ung-dung-va-tao-ra-cac-kenh-giao-tiep.png)

**2. Tìm Hiểu Về Giao Thức TCP IP** 
Giao thức TCP/IP không phải là 1 thể duy nhất, mà là sự kết hợp giữa 2 giao thức, gồm IP và TCP. Trong đó:

- IP (Internet Protocol ) – Giao thức liên mạng: Cho phép các gói tin được gửi đến đích. Tuy nhiên, giao thức này không đảm bảo các gói tin còn nguyên vẹn khi đến đích, nó có không theo thứ tự, bị trùng lặp, thậm chí là mất hoàn toàn.
- TCP (Transmission Control Protocol) – Giao thức điều khiển truyền nhận: Đóng vai trò kiểm tra và kiểm soát độ tin cậy của truyền dẫn, đảm bảo gói tin được chuyển đến đích một cách an toàn, đúng thứ tự và không xảy ra hiện tượng chậm, trễ trong đường truyền làm ảnh hưởng đến chất lượng gói tin. Trong quá trình làm việc, nếu phát hiện gói tin bị lỗi, TCP sẽ truyền đi một tín hiệu yêu cầu hệ thống gửi lại gói tin khác. Để hiểu rõ hơn về cách thức hoạt động và chức năng của TCP/IP, hãy cùng tìm hiểu chức năng của từng tầng trong mô hình này. 

![](https://github.com/TrongTan124/Thuc-tap-VNPT/raw/main/MinhNN/CCNA/images/tcp-three-way.png)

![](https://github.com/TrongTan124/Thuc-tap-VNPT/raw/main/MinhNN/CCNA/images/tcp-ip-flow-control.jpeg)
- TCP và IP kết hợp với nhau, tạo thành 1 bộ giao thức. Bộ giao thức này điều khiển truyền thông giữa tất cả các máy tính trên Internet. 


**3. Chức năng của từng tầng trong mô hình TCP/IP**
![](https://thietbimangcisco.vn/userfiles/TCP-IP-Model.png)
*3.1. Tầng 4: Tầng ứng dụng – Application*
- Tầng ứng dụng hay còn được gọi là Application. Đây là tầng trên cùng, có chức năng giao tiếp của mô hình. Cụ thể, tầng ứng dụng sẽ giao tiếp dữ liệu giữa 2 máy khác nhau. Việc giao tiếp có thể thông qua trình duyệt web, email hay một số giao thức khác như SMTP, SSH, FTP… 

- Tầng ứng dụng giao thức dữ liệu bằng hình thức Byte by Byte. Các thông tin sẽ được định tuyến với nhau, giúp gói tin đi theo một hướng đi đúng và thông tin được truyền tải thành công. 

*3.2. Tầng 3: Tầng giao vận (Transport)*
- Tầng này có vai trò xử lý vấn đề giao tiếp giữa 2 máy chủ trong cùng 1 mạng hoặc khác mạng được kết nối với nhau thông qua Router (bộ định tuyến). Ở tầng này, dữ liệu được phân thành các đoạn nhỏ, kích thước có thể không bằng nhau, nhưng bắt buộc phải nhỏ hơn 64KB.
![](https://fpttelecom.com/wp-content/uploads/2022/03/tang-3-trong-mo-hinh-tcp-ip.jpg)

- Tầng Giao vận bao gồm 2 giao thức cốt lõi, gồm: UDP và TCP. Trong đó:

| Giao thức | Đặc điểm                                      |
|----------|------------------------------------------------|
| UDP      | Không đảm bảo chất lượng gói tin                |
| TCP      | Đảm bảo độ tin cậy, kiểm soát tắc nghẽn lưu lượng |

![](https://github.com/TrongTan124/Thuc-tap-VNPT/raw/main/MinhNN/CCNA/images/tcp-header.jpg)

*3.3. Tầng 2: Tầng mạng (Network)*
- Tầng internet của TCP/IP có giao thức gần giống như mô hình OSI. Tầng 2 có chức năng chính trong việc truyền tải dữ liệu, đảm bảo các dữ liệu được truyền tải một cách logic. 

- Các dữ liệu sẽ được chia thành các phân đoạn sau đó được đóng gói. Mỗi gói sẽ có các kích thước phù hợp để việc vận chuyển dễ dàng hơn. Đồng thời, các gói thông tin khi truyền tải sẽ được thêm phần Header. Header này sẽ chứa các thông tin của tầng mạng để có thể xác định và chuyển tới tầng tiếp theo. Tầng internet thường sử dụng 3 giao thức chính, đó là: IP, ICMP và tầng ARP. 

*3.4. Tầng 1: Tầng vật lý – Physical*
- Đúng như tên gọi, tầng vật lý của giao thức TCP/IP có sự kết hợp giữa vật lý và dữ liệu mô hình OSI. Đây là tầng có trách nhiệm truyền tải các dữ liệu giữa các thiết bị khác nhau trong cùng 1 mạng internet. Khác với các tầng trên, tại tầng vật lý, các dữ liệu sẽ được đóng gói vào khung (Frame) trước khi được định tuyến và gửi tới địa chỉ đích đã được chỉ định. 

**4. Các giao thức TCP/IP phổ biến hiện nay**

**4.1. HTTP, HTTPS**
![](https://cloud.z.com/vn/wp-content/uploads/2023/03/http-vs-https.png)

- HTTP là một trong những phương thức phổ biến hiện nay. Giao thức này giúp truyền các thông tin dữ liệu giữa các website, thường là web client và web server. Việc truyền dữ liệu sẽ không được bảo mật. HTTP sẽ truyền các dữ liệu thường file ảnh hoặc tệp HTML….
- Đây là giao thức cực kỳ phổ biến. Giống với Http, Https cũng được sử dụng để truyền thông tin dữ liệu giữa 1 web client và 1 web server. Tuy nhiên, việc truyền thông tin dữ liệu sẽ được bảo mật. Đây là ưu điểm nổi bật của giao thức Http so với https. 
- HTTPS hiện đang sử dụng mô hình TCP/IP kết hợp với giao thức SSL và TLS. Vì thế, giao thức này cũng thường được sử dụng để truyền dữ liệu giữa thẻ tín dụng với dữ liệu cá nhân.

**4.2. FTP – File Transfer Protocol**
![](https://huphaco.vn/wp-content/uploads/2021/03/cach-thuc-truyen-du-lieu-cua-ftp.png)

- Đây là giao thức giúp kết nối 2 hoặc nhiều máy tính trên môi trường internet. Giao thức này hoạt động trên cổng số 20 và 21. Thông qua FTP, các máy con có thể truy cập internet để gửi dữ liệu tới máy chủ, đồng thời, lấy các dữ liệu đó. Dù ở khoảng cách xa, FTP vẫn giúp người dũng có thể dễ dàng truy cập vào máy chủ để nhận dữ liệu. 


# Giống và khác nhua giữa hai mô hình ?

| Nội dung               | Mô hình OSI                                                             | Mô hình TCP/IP                                              |
|------------------------|-------------------------------------------------------------------------|------------------------------------------------------------|
| Độ tin cậy và phổ biến | Nhiều người cho rằng đây là mô hình cũ, chỉ để tham khảo, sử dụng hạn chế | Được chuẩn hóa, được tin cậy và sử dụng phổ biến trên toàn cầu |
| Phương pháp tiếp cận   | Tiếp cận theo chiều dọc                                                   | Tiếp cận theo chiều ngang                                    |
| Sự kết hợp giữa tầng   | Mỗi tầng thực hiện nhiệm vụ riêng biệt, không có sự kết hợp               | Tầng ứng dụng kết hợp tầng trình diễn và tầng phiên             |
| Thiết kế               | Phát triển mô hình trước rồi phát triển giao thức                           | Thiết kế giao thức trước rồi phát triển mô hình                 |
| Số lớp (tầng)          | 7                                                                       | 4                                                          |
| Truyền thông           | Hỗ trợ cả kết nối định tuyến và không dây                                  | Hỗ trợ truyền thông không kết nối từ tầng mạng                 |
| Tính phụ thuộc         | Giao thức độc lập                                                        | Phụ thuộc vào giao thức                                     |
