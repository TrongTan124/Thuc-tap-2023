## Overview
1. Giao thức định tuyến OSPF (Open Shortest Path First)
2. Giao thức EIRGP

### 1. Giao thức định tuyến OSPF

- Giao thức định tuyến OSPF là giao thức định tuyến động thuộc nhóm Link State. 
-  Mỗi router khi chạy giao thức sẽ gửi các trạng thái đường link của nó cho tất cả các router trong vùng (area). Sau một thời gian trao đổi, các router sẽ đồng nhất được bảng cơ sở dữ liệu trạng thái đường link (Link State Database – LSDB) với nhau, mỗi router đều có được bản đồ mạng của cả vùng. Từ đó mỗi router sẽ chạy giải thuật Dijkstra tính toán ra một cây đường đi ngắn nhất (Shortest Path Tree) và dựa vào cây này để xây dựng nên bảng định tuyến.


#### 1.1 Đặc điểm của OSPF

- Định tuyến theo kiểu Link State
- Chỉ số AD (Administrative Distance): 110
- Metric phụ thuộc vào BandWidth
- OSPF chạy trên nền giao thức IP, có protocol ID = 89 

<!-- AD- Administrative Distance: là chỉ số ưu tiên của một giao thức trong hệ thống mạng có từ 2 hay nhiều giao thức định tuyến được triển khai -->

#### 1.2 Cơ chế hoạt động của các router giao thức OSPF
- Router ID
- Thiết lập Neighbor
- Trao đổi LSDB (Link State Database)
- Xây dựng bảng định tuyến (sử dụng giải thuật Dijkstra)

##### 1.2.1 Router ID
- Router ID: là một giá trị dùng để định danh cho Router, khi Router tham gia vào môi trường định tuyến OSPF.
- Router ID có định dạng là 1 IP nhưng nó không phải IP 
Cách bầu Router ID: Lấy IP cao nhất trong các interface active và ưu tiên cổng loopback
- Để tạo ra Router-ID có 2 cách:
    - Router tự động tạo ra
    - Tự config

**Cách 1:** Tự động tạo
- Dựa vào interface nào có địa chỉ `IP cao nhất` thì nó lấy IP đó làm Router ID.
    - Ví dụ: Router có f0/0 là 10.0.0.1, f0/1 là 172.16.1.1, s0/0/0: 192.168.1.1 => Router ID là 192.168.1.1
- Nếu Router có loopback tồn tại và tham gia vào định tuyến thì Router-id `ưu tiên cho loopback` trước 
    - Ví dụ: lookback 0 = 4.1.1.1, lookback 1 = 4.2.2.2, f0/0=172.16.1.1, f0/1=192.168.1.1 => Router ID là 4.2.2.2

**Cách 2:** Cấu hình
- Router-id không nhất thiết là phải chọn IP có trên interface
- Vd: lookback 0 = 4.1.1.1, lookback 1 = 4.2.2.2, f0/0=172.16.1.1, f0/1=192.168.1.1
Ta có thể cấu hình để chọn Router-id = 100.100.100.100. Ip này không thuộc interface nào của router cả

##### 1.2.2 Thiết lập quan hệ láng giềng
- Router chạy OSPF sẽ gửi gói tin hello ra tất cả các cổng chạy OSPF, mặc định 10s/lần. Gói tin này được gửi đến địa chỉ multicast dành riêng cho OSPF là 224.0.0.5, đến tất cả các router chạy OSPF khác trên cùng phân đoạn mạng. Mục đích của gói tin hello là giúp cho router tìm kiếm láng giềng, thiết lập cũng như duy trì mối quan hệ này.
- Điều kiện để thiết lập quan hệ láng giềng:
    - Cùng Area-ID
    - Cùng subnet và subnet-mask
    - Cùng hello-timer và dead-timmer
    - Thoả mãn điều kiện xác thực

**Điều kiện 1: Cùng Area-ID**: 
- Cùng Area-id: Khi mạng lớn người ta chia làm nhiều vùng, vùng nào hỏng thì chỉ vùng đó chịu tác động. Mỗi một vùng sẽ đặt cho một Area-id. Vùng trung tâm có Area-id phải bằng 0. Mọi vùng khác phải có đường truyền trực tiếp về vùng 0 nó mới truyền được dữ liệu.

Các thuật ngữ liên quan đến Area-ID: 
- Backbone Area: Phải có ít nhất 1 vùng, kí hiệu: 0
- Non-backbone area: phải kết nối trực tiếp với vùng Backbone area, kí hiệu: 1-2^52 => Sẽ có 1 con router đứng giữa 2 vùng
- Backbone Router: Router nằm trong vùng backbone area
- Internal Router: là Router nằm trong vùng non-backbone area.
- Area Boder Router(ABR): Router nằm giữa ranh giới backbone area và non-backbone area.

![](https://github.com/TrongTan124/Thuc-tap-VNPT/blob/main/MinhNN/CCNA/images/07_network-example1.png?raw=true)

**Điều kiện 2: Cùng Subnet và Subnet-Mask**: 


**Điều kiện 3: Cùng Hello Timer và Dead Timer:**
- `Hello Timer` là khoảng thời gian định kỳ router gửi các gói tin hello ra các cổng chạy OSPF
- `Dead Timer` là khoảng thời gian mà láng giềng chờ hello timer gửi gói tin cho mình. Nếu hết khoảng thời gian Dead Timer mà router đó không nhận đước các gói tin hello từ láng giếng, nó sẽ tự động xoá bộ dữ liệu được học từ láng giềng này.
- Giá trị mặc định của `Hello Timer / Dead Timer` là `10s/40s`
**Điều kiện 4: Thoả mãn điều kiện xác thực:**

- Cùng là plain-text
- Cùng xác thực MD5

![](https://github.com/TrongTan124/Thuc-tap-VNPT/blob/main/MinhNN/CCNA/images/07_network-example2.png?raw=true)

- Trong hình trên, khi R3 chạy OSPF tuy nhiên k biết password thì không thể học được các thông tin định tuyến của R1, R2 mà chỉ có R1, R2 trao đổi thông tin định tuyến với nhau.

**=> Khi thoả mãn 4 điều kiện trên thì 2 con router sẽ trở thành láng giềng của nhau**

##### 1.2.3 Tìm đường đi tối ưu
- B1: thiết lập được neighbor của nhau. Sau đó liệt kê các neighbor vào trong neighbor của mình. Lúc này, mối quan hệ giưa các neighbor gọi là 2-way

- B2: Bắt đầu gửi thông tin trạng thái đường link để dựng lên 1 bảng database(bảng topology).

- B3: từ bảng topology nó bắt đầu dùng thuật toán Dijkstra để tìm ra đường đi tối ưu để đưa ra bảng định tuyến.

- B4: bảng LSDB chứa các LSA. Để có LSA thì nó phải trải qua các giai đoạn sau :

> Sau khi ở trạng thái 2-Way thì các con router sẽ gửi thông tin cho nhau để hình thành 1 bảng databse gọi là `Link State Database`.

*Note: Các router sẽ không trao đổi với nhau cả một bảng LSDB mà sẽ trao đổi với nhau từng đơn vị thông tin gọi là LSA (Link State Advertisement). Các đơn vị thông tin này lại được chứa trong các gói tin cụ thể gọi là LSU (Link State Update) mà các router thực sự trao đổi với nhau.*

**Giai đoạn 1:** Router sẽ gửi thông tin trạng thái đường link của nó qua láng giềng, gọi là ` LSA (Link State Advertisement)`

**Giai đoạn 2:** Trước khi gửi `LSA`, nó sẽ gửi 1 bản tin `DBD (Database Description)` để mô tả thông tin nó có được cho router neighbor

**Giai đoạn 3:** Khi neighbor nhận được DBD, nếu nó thấy thông tin nào trong DBD mà nó không có thì nó sẽ gửi `LSR (Link state request) ` để xin thông tin thiếu. 

**Giai đoạn 4:** Khi router nhận được `request LSR` thì nó phải trả những thông tin thiếu cho router bằng `LSA` nằm bên trong `LSU (Link State Update)`.

**Giai đoạn 5:** Khi router nhận được `LSU` thì nó sẽ bỏ phần `LSU` đi và lấy phần `LSA`. Khi nhận xong nó sẽ gửi lại `LSACK (Link state acknowledgement)` để xác nhận là đã nhận.

> Sau khi có LSDB thì router có thể tự chọn được đường đi tốt nhất dựa vào thuật toán Dijkstra

### 1.3 Môi trường mạng
- Tùy thuộc vào mỗi 1 môi trương mạng thì nó có 1 cách trao đổi khác nhau để nó tìm được đường đi tốt nhất.

- Trong môi trường mạng có 2 môi trường chính:

    - a. môi trường point to point
        - là môi trường mà 2 router kết nối với nhau bằng cổng serial(WAN).
        - Khi ở môi trường này thì các router gửi LSDB trực tiếp qua nhau thì từ mối quan hệ 2-way chuyển sang mối quan hệ FULL (nếu không quan hệ trực tiếp với nhau thì ko cần chuyển quan hệ 2-way)
    - b. môi trường broadcast multi access
        - các router kết nối với nhau = interface LAN.
        - Trước khi trao đổi thông tin thì các router sẽ bầu chọn ra 1 router đóng vai trò làm chủ đạo gọi là `DR(designated router)` có nhiệm vụ tiếp nhận các thông tin trao đổi và gửi qua cho các router khác.
        - `BDA(backup designated router)` là router dự phòng cho DR.
        - `DA other`: Những router còn lại. Những router không nói chuyện trực tiếp với nhau (vẫn giữ trạng thái 2-way) mà phải thông qua DR. Đồng thời DR gửi thông tin copy cho BDA để backup. Theo mặc định, DR Other sẽ gử thông tin về DR bằng địa chỉ 224.0.0.6. DR sẽ gửi LSDB cho DR Other là 224.0.0.5.
        
        ![](https://github.com/TrongTan124/Thuc-tap-VNPT/blob/main/MinhNN/CCNA/images/07_network-example3.png?raw=true)

        - Cách bầu DR, BDR:

            - priority: chỉ số ưu tiên của cổng. Có giá trị từ 0 – 255(default=1)

                - Router có priority cao nhất làm DR, cao thứ 2 làm BDR, còn lại DA other.

                - Khi đặt priority = 0 cho 1 
                interface router thì router đó không bao giờ được làm DR,BDR.

            - Router-id: Khi xét quá trình chọn DR thì router-id sẽ không xét loopback

                - Riêng DR và BDR nói chuyện với nhau = 224.0.0.6 còn lại nói chuyện với nhau = 224.0.0.5

                - Trong OSPF có 1 quy luật Non-preemptive: nghĩa là không bầu chọn lại.Khi DR chết BDR thay nhưng sau đó DR sống lại thì nó sẽ ko được bầu chọn lại làm DR lại như cũ.
### 1.4. Tính toán xây dựng bảng định tuyến

 - Trong OSPF không còn gọi là Metrics, thay vào đó gọi là Cost (Cost trên interface).

 - Cost được tính khi đi vào 1 cổng và đi ra không tính.

 - Metric = cost = 10^8/Bandwidth (đơn vị bps). 1 Mbps = 10^6 bps (you are converting between megabit/second and bit/second)
 

    - vd:Ethernet (BW = 10Mbps) → cost = 10.

    - Fast Ethernet (BW = 100Mbps) → cost = 1.

    - Serial (BW = 1.544Mbps) → cost = 64 (bỏ phần thập phân trong phép chia).

 - Dựa vào đó xây dựng bảng định tuyến nó dùng giải thuật Dijkstra để đưa ra đường đi tốt nhất


### 1.5. Những trạng thái của OSPF

- Down: Tại trạng thái này, trên giao diện sẽ không nhận bất kỳ gói tin HELLO nào nếu thiết bị ở trạng thái ngừng hoạt động (quá trình OSPF chưa bắt đầu).
- Init: Thiết bị của bạn ở trạng thái Init sẽ đồng nghĩa với việc thiết bị đã nhận được gói HELLO từ một bộ định tuyến khác.
- 2WAY: Nếu thiết bị của bạn trong trạng thái này thì cả hai bộ định tuyến đều đã nhận được gói tin HELLO từ bộ định tuyến khác và giữa những bộ định tuyến này đã được hình thành liên kết.
- Exstart: Cả hai bộ định tuyến sẽ chuyển sang trạng thái khởi động khi quá trình trao đổi giữa chúng bắt đầu. Cả chủ và khách tại trạng thái này sẽ được chọn dựa trên ID của bộ định tuyến.
- Exchange: Cả hai bộ định tuyến trong trạng thái trao đổi sẽ gửi danh sách các LSA có chứa mô tả cơ sở dữ liệu cho nhau.
- Loading: LSR, LSU và LSA tại trạng thái tải sẽ tiến hành trao đổi cho nhau.
- Full: Sau khi LSA hoàn tất việc trao đổi, các bộ định tuyến sẽ ngay lập tức chuyển sang trạng thái đầy đủ này.

### 1.6. Định dạng tin nhắn OSPF
![](https://github.com/fptcloud/Thuc-tap-2023/raw/main/PhucDH/Network/images/ospf-format-messes.png)

- Version: Đây là trường 8 bit chỉ định phiên bản giao thức OSPF.

- Type: Đây là trường 8 bit. Nó chỉ định loại gói OSPF.

- Message: Nó là một trường 16 bit xác định tổng độ dài của thông báo, bao gồm cả header. Do đó, tổng độ dài bằng tổng độ dài của thông điệp và Header.

- Source IP address: Nó xác định địa chỉ mà các gói được gửi đi. Nó là một địa chỉ IP định tuyến gửi.

- Area identification: Nó xác định khu vực mà quá trình định tuyến diễn ra.

- Checksum: Nó được sử dụng để sửa lỗi và phát hiện lỗi.

- Authentication type: Có hai loại xác thực, tức là 0 và 1. Ở đây, 0 có nghĩa là không có nghĩa là không có xác thực nào khả dụng và 1 có nghĩa là chỉ định xác thực dựa trên mật khẩu.

- Authentication: Nó là một trường 32 bit chứa giá trị thực của dữ liệu xác thực.

### 1.7. Các loại gói tin OSPF
Có năm loại gói tin khác nhau trong OSPF:

1. Hello:

    Gói Hello được sử dụng để tạo mối quan hệ láng giềng và kiểm tra khả năng tiếp cận của neighbor. Do đó, gói Hello được sử dụng khi kết nối giữa các bộ định tuyến cần được thiết lập.

2. Database Description:

    Sau khi thiết lập kết nối, nếu router láng giềng đang giao tiếp với hệ thống lần đầu tiên, nó sẽ gửi thông tin cơ sở dữ liệu về cấu trúc liên kết mạng đến hệ thống để hệ thống có thể cập nhật hoặc sửa đổi cho phù hợp.

3. Link state request:

    Link state request được gửi bởi bộ định tuyến để lấy thông tin của một tuyến được chỉ định. Giả sử có hai bộ định tuyến, tức là bộ định tuyến 1 và bộ định tuyến 2, và bộ định tuyến 1 muốn biết thông tin về bộ định tuyến 2, vì vậy bộ định tuyến 1 gửi yêu cầu trạng thái liên kết đến bộ định tuyến 2. Khi bộ định tuyến 2 nhận được yêu cầu trạng thái liên kết, thì nó gửi thông tin trạng thái liên kết đến bộ định tuyến 1.

4. Link-state update

    Link state update được bộ định tuyến sử dụng để quảng cáo trạng thái của các liên kết của nó. Nếu bất kỳ bộ định tuyến nào muốn phát trạng thái của các liên kết của nó, nó sẽ sử dụng bản cập nhật trạng thái liên kết.

5. Link state Acknowledgment

    Xác nhận trạng thái liên kết làm cho việc định tuyến đáng tin cậy hơn bằng cách buộc mỗi bộ định tuyến gửi xác nhận trên mỗi bản cập nhật trạng thái liên kết. Ví dụ: bộ định tuyến A gửi bản cập nhật trạng thái liên kết tới bộ định tuyến B và bộ định tuyến C, sau đó đổi lại, bộ định tuyến B và C gửi xác nhận trạng thái liên kết đến bộ định tuyến A, để bộ định tuyến A biết rằng cả hai bộ định tuyến đã nhận được bản cập nhật trạng thái liên kết.



### 2. Giao thức EIRGP

#### 2.1.  Giao thức định tuyến EIGRP (Enhanced Interior Gateway Routing Protocol)

- Là giao thức định tuyến do Cisco phát triển, chỉ chạy trên các sản phẩm của Cisco. 

- Là giao thức dạng Advanced Distance Vector, sử dụng thuật toán DUAL.

- EIGRP chỉ gửi toàn bộ bảng định tuyến cho láng giềng lần đầu, và các lần sau chỉ gửi bản cập nhật khi có sự thay đổi, giúp cho việc tiết kiệm tài nguyên mạng.

- Việc sử dụng bảng Topology và thuật toán DUAL làm cho EIGRP có tốc độ hội tụ rất nhanh.

- EIGRP sử dụng công tính thức metric phức tạp, dựa trên nhiều thông số: Bandwidth, Delay, Load, Reliability

- Chỉ số AD của EIGRP là 90 cho các internal router và 170 cho external router

- EIGRP chạy trực tiếp trên nền IP và có số protocol-id là 88

#### 2.2. Thiết lập quan hệ láng giềng

- Điều kiện thiết lập quan hệ láng giềng:
    - Giá trị AS (Autonomous System) được cấu hình trên router là giống nhau
    - Cùng subnet
    - Thoả mãn các điều kiện xác thực
    - Cùng bộ tham số K

- Cách hoạt động:
    - Khi bật EIGRP lên một cổng, thì router sẽ tự động gửi các gói tin ra khỏi cổng để thiết lập quan hệ neighbor với router được kết nối trực tiếp với nó. Các gói tin này được gửi đến địa chỉ multicast dành riêng cho EIGRP là 224.0.0.10 với giá trị hello-timer (khoảng thời gian định kỳ gửi gói tin hello) là 5s.
    - Để thiết lập được quan hệ láng giềng thì router phải thoả mãn các điều kiện được nhắc tới ở trên.


##### Điều kiện 1: Giá trị AS - Autonomous System
- AS ở đây chỉ được coi là 1 routing domain, các router khi chạy định tuyến với nhau, cùng 1 sự quản trị sẽ được ghép chung 1 domain. Mỗi domain có 1 giá trị AS riêng 
- AS được dùng trong giao thức định tuyến EIGRP khác với giao thức định tuyến ngoài (Ví dụ: BGP)

![](https://github.com/TrongTan124/Thuc-tap-VNPT/blob/main/MinhNN/CCNA/images/08_network-example1.png?raw=true)


- Ở hình trên, Có 2 AS 100 và 200 chạy định tuyến ngoài BGP với nhau. Bên trong AS 100 chạy giao thức định tuyến EIGRP và chia thành 2 process-domain là 100 và 200. Router biên đứng ở giữa process-domain 100 và 200 sẽ redistribute thông tin giữa 2 domain để các con router trên 2 domain này thấy các thông tin về các subnet của nhau.


##### Điều kiện 2: Cùng Subnet

- Để 2 router thiết lập được quan hệ láng giềng, hai router phải có cùng subnet.

##### Điều kiện 3: Thoả mãn các điều kiện xác thức

- Trên các router phải có password giống nhau mới có thể trao đổi thông tin định tuyến với nhau.

##### Điều kiện 4: Cùng bộ tham số K

EIGRP sử dụng công thức tính metric rất phức tạp: 

 - Metric = f(Bandwidth, Delay, Reliability, Load), các thông số K1, K2, K3, K4, K5 được cấu hình trên các router phải khớp với nhau.



#### 2.3. Bảng Topology, FD, AD, Successor và Feasible Successor

- Sau khi thiết lập quan hệ láng giềng, các router láng giềng của nhau sẽ lập tức gửi toàn bộ các route EIGRP trong bảng định tuyến của chúng.
- Chúng chỉ gửi bảng định tuyến lần đầu tiên, các lần sau sẽ gửi các bản cập nhật nếu có bất kỳ thay đổi gì.
- Khi router nhận được nhiều route từ nhiều láng giềng khác nhau, nó sẽ chọn cái tốt nhất để đưa vào sử dụng, các route khác nó sẽ đưa vào một "kho chứa" để dùng cho mục đích dự phòng đường đi. Kho chứa này được gọi là bảng "Topology". Khi đó, bảng Topology trên một router chạy EIGRP là bảng lưu toàn bộ route có thể có từ nó đến mọi đích đến trong mạng, và bảng định tuyến sẽ là bảng lấy và sử dụng route tốt nhất từ bảng Topology này.

![](https://github.com/TrongTan124/Thuc-tap-VNPT/blob/main/MinhNN/CCNA/images/08_network-example2.png?raw=true)

- Giả sử sơ đồ trên chạy định tuyến EIGRP, ta xem xét các đường đi từ router R đến mạng 4.0.0.0/8 của R4. Khi đó có tổng cộng 3 đường

    - Đường số 1: metric từ router đang xét đến mạng 4.0.0.0/8 là 1000, metric từ láng giềng trên đường này (R1) đến 4.0.0.0/8 là 900. 
    - Đường số 2: metric từ router đang xét đến mạng 4.0.0.0/8 là 2000, metric từ láng giềng trên đường này (R2) đến 4.0.0.0/8 là 1200.
    - Đường số 3: metric từ router đang xét đén mạng 4.0.0.0/8 là 3000, từ router láng giềng trên đường này (R3) đến 4.0.0.0/8 là 800.

- Khi đó ta có các khái niệm:
    - Với mỗi đường đi, giá trị metric từ router đang xét đến mạng đích được gọi là FD - Feasible Distance
    - Cũng với đường ấy, giá trị metric từ router láng giềng (next hop) đi đến cùng mạng đích được gọi là AD - Advertised Distance hay là RD - Reported Distance. Khái niệm AD ở đây khác với AD - Administrative Distance được dùng trong việc so sánh độ ưu tiên giữa các giao thức định tuyến.

- Như vậy ta có các giá trị AD, FD từ hình trên như sau:
    - Đường số 1: FD1 = 1000, AD1 = 900
    - Đường số 2: FD2 = 2000, AD2 = 1200
    - Đường số 3: FD3 = 3000, AD3 = 800

- `Sucessor`: Trong tất cả các đường đi đến mạng đích được lưu ở trong bảng Topology, đường nào có FD nhỏ nhất, đường đó sẽ được bầu làm `Successor`, router láng giềng trên đường này được gọi là successor router (hoặc successor). Đường successor sẽ được đưa vào bảng định tuyến để sử dụng làm được đi chính thức đến đích
- `Feasible Successor`: Trong tất cả các đường còn lại có FD > FD của Successor, đường nào có AD < FD của successor, đường đó sẽ được chọn làm `Feasible Successor` và được dùng để làm backup cho `Successor`

- Trong 3 đường trên, đường 1 được bầu làm `Successor` và đường 3 được bầu làm `Feasible Successor`. Khi đường số 1 down, đường số 3 sẽ lập tức được dùng để thay thế.

- Lý do chọn đường `Feasible Successor` mà thoả mãn điều kiện AD < FD của successor là để chống loop. Trong một mạng chạy giao thức Distance - Vector, nếu metric từ điểm A đến một mạng nào đấy < metric đi từ điểm B đến mạng ấy thì không bao giờ trên hành trình từ điểm A đi đến mạng nêu trên lại đi qua mạng B. Chính vì thế nếu AD của Feasible Successor < FD của Successor thì không bao giờ dữ liệu đi theo Feasible Successor lại đi vòng trở lại router Successor.

- Trong trường hợp không có đường nào được bầu làm `Feasible Successor`. `Successor` vẫn được đưa vào bảng định tuyến để làm đường đi chính thức đến mạng chính nhưng nó sẽ không có đường backup. Trong trước hợp này khi `Successor` bị down, router chạy EIGRP sẽ thực hiện một kỹ thuật gọi là Query: nó sẽ phát các gói tin truy vấn đến các láng giềng, hoạt động truy vấn sẽ được tiếp tục nó khi tìm thấy đường đi đến đích hoặc không còn đường đi nào có thể về đích được nữa. 

### Cân bằng tải trên những đường không đều nhau (Unequal Cost Load - Balancing)


![](https://github.com/TrongTan124/Thuc-tap-VNPT/blob/main/MinhNN/CCNA/images/08_network-example3.png?raw=true)

| Network  |  Neighbor |  FD |  AD |
|---|---|---|---|
| 172.16.0.0  | B  |  30 |  10 |
|   |  C |  20 | 10  |
|   |  D | 45  | 25  |

- Khi này router gốc sẽ chọn router C để route đến network 172.16.0.0 bởi vì nó có FD min.
- Với variance 2. Router gốc sẽ chọn cả router B để đi đến network 172.16.0.0 (20 + 10 = 30 < (2 * FDmin) = 40)
- Với variance 3. Ta sẽ có cả 3 đường.

#### Xác thực MD5 với EIGRP

[Video](https://www.youtube.com/watch?v=JpsV9LVFUAw&list=PLBOZzuSFDzSL_5CvfuNo7EhFQR1z6hhpo&index=71)

[Docs](https://vnnet.edu.vn/giao-thuc-dinh-tuyen-eigrp-enhanced-interior-gateway-routing-protocol/)


#### Tài liệu tham khảo:

[OSPF Security Zone](https://securityzone.vn/t/bai-14-tim-hieu-giao-thuc-dinh-tuyen-ospf.101/)

[Link State OSPF](https://www.daihockhonggiay.com/blogs/post/link-state-ospf)

[OSPF Hosting Viet](https://hostingviet.vn/giao-thuc-ospf)

[Tài liệu về subnet mask cơ bản 1](https://hocmangcoban.blogspot.com/2014/04/network-subnet-subnet-mask-broadcast.html)

[Tài liệu về subnet mask cơ bản 2](https://vietnix.vn/subnet-mask-la-gi/)
