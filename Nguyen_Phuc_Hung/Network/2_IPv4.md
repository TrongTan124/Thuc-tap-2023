# Tổng quan về IPv4

- IPv4 là phiên bản IP thế hệ thứ 4, nó được sử dụng nhiều nhất hiện nay bên cạnh IPv6. Hai phiên bản IP này là yếu tố chủ chốt cho việc giao tiếp giữa các thiết bị trong mạng internet.

![](https://bkhost.vn/wp-content/uploads/2022/03/ipv4-la-gi.jpg)

- IPv4 được ra mắt vào năm 1981 trong phiên bản RFC 791 và đã được bộ quốc phòng Hoa Kỳ chuẩn hóa trong phiên bản MIL-STD-1777.

- IPv4 được ứng dụng trong các hệ thống chuyển mạch gói. Vai trò của nó là định hướng dữ liệu truyền đi. Khi truyền đi các gói tin, giao thức này chỉ đảm bảo phần truyền tải mà không để ý đến thứ tự truyền gói tin hoặc vấn đề gói tin có đến đích hay không, có lặp lại ở máy đích hay không. Vấn đề này sẽ được giải quyết ở tầng cao hơn của hệ thống TCP/IP. Một điều mà IPv4 đảm bảo được đó là tính toàn vẹn dữ liệu bằng cách sử dụng kết quả của việc chạy thuật toán Checksum để kiểm tra.

### 1. Cấu trúc của IPv4

- IPv4, 32 bit, chia thành 4 octet (mỗi octet có 8 bit, tương đương 1 byte, các byte tách nhau bằng dấu .), bao gồm 3 thành phần chính:


![](https://github.com/TrongTan124/Thuc-tap-VNPT/raw/main/MinhNN/CCNA/images/example1-network2.png)

  - Bit nhận dạng lớp (classbit)
  - Địa chỉ của mạng (NetID)
  - Địa chỉ của máy chủ (Host ID)

**Note:** Việc đặt địa chỉ IP phải tuân theo các quy tắc sau:

- Không được đặt những bit ở phần network bằng 0 cùng một lúc. Khi đặt tất cả những bit ở phần network bằng không thì địa chỉ IP sẽ có 3 số đầu là 0.0.0. Đây là một địa chỉ sai.
- Nếu đặt tất cả các bit ở phần host bằng 0 thì số cuối cùng của địa chỉ IP sẽ bằng 0. Khi đó địa chỉ đó là một địa chỉ mạng, không thể dùng làm host. Ví dụ: 191.168.10.0 là một địa chỉ mạng.
- Nếu đặt tất cả các bit ở phần host là 1 thì số cuối cùng của địa chỉ IP là 255. Khi đó địa chỉ này sẽ là một địa chỉ broadcast của mạng đó. Ví dụ: 192.168.10.255 là một địa chỉ broadcast.

### 2. Phân lớp địa chỉ IPv4

![](https://github.com/TrongTan124/Thuc-tap-VNPT/raw/main/MinhNN/CCNA/images/example2-network2.png)


![](https://github.com/TrongTan124/Thuc-tap-VNPT/raw/main/MinhNN/CCNA/images/example3-network.png)

#### 2.1. Lớp A

![](https://bkhost.vn/wp-content/uploads/2022/03/dia-chi-lop-a.jpg) 
- Địa chỉ lớp A có phần mạng là 8 bit đầu và phần host là 24 bit sau. Bit đầu tiên của phần mạng luôn là 0.

- Lớp A sẽ có các địa chỉ mạng từ 1.0.0.0 đến 126.0.0.0 và mỗi mạng sẽ có 224 địa chỉ host (loại trừ địa chỉ mạng và địa chỉ broadcast).
  - netid: 126 mạng
  - host id: 16.777.214 máy chủ trên 1 mạng

- Mạng loopback sẽ là 127.0.0.0.

#### 2.2. Lớp B

![](https://bkhost.vn/wp-content/uploads/2022/03/dia-chi-lop-b.jpg)
- 2 bit đầu nhận dạng lớp B = 10
- 14 Bit còn lại trong 2 octet đầu dành cho địa chỉ mạng
- 2 Octet còn lại có 16 bit dành cho địa chỉ host

  - netid: 16.382 mạng
  - host id: 65.354 máy chủ

#### 2.3. Lớp C
![](https://github.com/TrongTan124/Thuc-tap-VNPT/raw/main/MinhNN/CCNA/images/example6-network2.png)

- 3 bit đầu nhận dạng lớp C = 110
- 21 bit còn lại trong 3 octet đầu dành cho địa chỉ mạng
- Octet cuối có 8 bit dành cho địa chỉ máy chủ

  - netid: 2.097.150 mạng
  - host id: 254 máy chủ / mạng

#### 2.4. Lớp D

-    Địa chỉ: 224.0.0.0 -> 239.255.255.255

-    Dùng làm địa chỉ multicast.
 - Ví dụ: 
   -   224.0.0.5 dùng cho OSPF

    - 224.0.0.9 dùng cho RIPv2 

#### 2.5. Lớp E
- Từ 240.0.0.0 trở đi.

-    Được dùng cho mục đích dự phòng.

### 3. Địa chỉ Private và Public

-   Địa chỉ IP được phân thành hai loại: private và public.

- Private: chỉ được sử dụng trong mạng nội bộ (mạng LAN), không được định tuyến trên môi trường Internet. Có thể được sử dụng lặp đi lặp lại trong các mạng LAN khác nhau.
- Public: là địa chỉ IP sử dụng cho các gói tin đi trên môi trường Internet, được định tuyến trên môi trường Internet, không sử dụng trong mạng LAN. Địa chỉ public phải là duy nhất cho mỗi host tham gia vào Internet.
-   Dải địa chỉ private (được quy định trong RFC 1918):

    - Lớp A: 10.x.x.x

    - Lớp B: 172.16.x.x -> 172.31.x.x

    - Lớp C: 192.168.x.x

-   Kỹ thuật NAT (Network Address Translation) được sử dụng để chuyển đổi giữa IP private và IP public.

-   Ý nghĩa của địa chỉ private: được sử dụng để bảo tồn địa chỉ IP public đang dần cạn kiệt.

### 4. Chia Subnet

#### 4.1. Subnet mask và số prefix
- Subnet mask là một dải 32 bit nhị phân đi kèm với một địa chỉ IP, được các host sử dụng để xác định địa chỉ mạng của địa chỉ IP này. Để làm được điều đó, host sẽ đem địa chỉ IP thực hiện phép tính AND từng bit một của địa chỉ với subnet mask của nó, kết quả host sẽ thu được địa chỉ mạng tương ứng của địa chỉ IP.

- Ví dụ: Xét địa chỉ 192.168.1.1, với subnet mask tương ứng là 255.255.255.0
  - Lớp A : 255.0.0.0                     

  - Lớp B:  255.255.0.0
  - Lớp C: 255.255.255.0

- Số prefix: Để mô tả một địa chỉ IP, người ta dùng một đại lượng khác được gọi là số prefix. Số prefix có thể hiểu một cách đơn giản là số bit mạng trong một địa chỉ IP, được viết ngay sau địa chỉ IP, và được ngăn cách với địa chỉ này bằng một dấu “/”.

Ví du: 192.168.1.1/24, 172.16.0.0/16 hay 10.0.0.0/8, v.v…

#### 4.2. Chia Subnet VLSM
![](https://scontent.xx.fbcdn.net/v/t1.15752-9/350090288_900207957711455_6943665591303809326_n.png?_nc_cat=106&ccb=1-7&_nc_sid=aee45a&_nc_ohc=3KFML0yJro8AX-X6_PZ&_nc_oc=AQnX0LgfggkKs1eiOrfYH-On9b42tQdv3zpVyvqiBzvc3pgWrww3KVk7aJkC0ydqn1pPpW7KWNNShozOb22gBV3f&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQ8gqsN8MKqWDtTN_gS1fZgjnH3FiHLwn8q3I62lpTkDQ&oe=64991B69)

![](https://scontent.xx.fbcdn.net/v/t1.15752-9/350092823_163800946455530_4146803422053345977_n.png?stp=dst-png_p206x206&_nc_cat=111&ccb=1-7&_nc_sid=aee45a&_nc_ohc=2a9lO21rruMAX9clCeo&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQ-gisSUriPKWJ5D1-TInCrHZjCLtdY1dppKCOR_ria_Q&oe=6499121B)

<img src="https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/349680548_3107759679525786_7466595498941542241_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_ohc=KJeO_S2PmXcAX8433IO&_nc_ht=scontent.fhan2-3.fna&oh=03_AdTfI9fNiuM_V7XnCouQoO7xgQoHPjoBDzlmDqly4VdQPQ&oe=64991666" width="500" height="500">

![](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/349585288_208412111555664_7430575411844834693_n.png?_nc_cat=106&ccb=1-7&_nc_sid=ae9488&_nc_ohc=p5YKf6a1KN8AX-F_5XD&_nc_ht=scontent.fhan2-5.fna&oh=03_AdQIlaaFK3ow8EaPvvkkRMGWMYZ3s5XqzeKiBE_mI2bOCA&oe=64993DD4)

### Tài liệu tham khảo

https://bizflycloud.vn/tin-tuc/ipv4-la-gi-20210607115922143.htm
https://maychusaigon.vn/ipv4-la-gi/
https://whatismyipaddress.com/private-ip
