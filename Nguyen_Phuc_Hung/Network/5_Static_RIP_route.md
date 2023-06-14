# Định tuyến
- Trong thế giới kỹ thuật mạng, định tuyến đóng một vai trò cực kỳ quan trọng trong việc truyền tải thông tin giữa các mạng và thiết bị. Trong bài viết này, chúng ta sẽ khám phá hai loại định tuyến quan trọng: định tuyến tĩnh và định tuyến động. Chúng ta sẽ tìm hiểu sự khác biệt giữa chúng, ưu điểm của từng loại và các trường hợp sử dụng phù hợp.
- Định tuyến là quá trình xác định và chọn đường đi tối ưu cho việc truyền tải dữ liệu hoặc gói tin trong mạng. Nó là một phần quan trọng của quá trình truyền thông trong hệ thống mạng và có vai trò quan trọng trong đảm bảo kết nối hiệu quả giữa các thiết bị và mạng.

![](https://maychuvatly.com/wp-content/uploads/2020/11/Dinh-tuyen-800x261.png)

## Định tuyến tĩnh (static route)

## Khái niệm

- Định tuyến tĩnh là quá trình router thực hiện chuyển gói dữ liệu tới địa chỉ mạng đích dựa vào địa chỉ IP đích của gói dữ liệu. Để chuyển được gói dữ liệu đến đúng đích thì router phải học thông tin về đường đi tới các mạng khác. Thông tin về đường đi tới các mạng khác sẽ được người quản trị cấu hình cho router. Khi cấu trúc mạng thay đổi, người quản trị mạng phải tự thay đổi bảng định tuyến của router.

- Kỹ thuật định tuyến tĩnh đơn giản, dễ thực hiện, ít hao tốn tài nguyên mạng và CPU xử lý trên router (do không phải trao đổi thông tin định tuyến và không phải tính toán định tuyến). Tuy nhiên kỹ thuật này không hội tụ với các thay đổi diễn ra trên mạng và không thích hợp với những mạng có quy mô lớn (khi đó số lượng route quá lớn, không thể khai báo bằng tay được).

## Ưu và nhược điểm

- Ưu điểm:

 +Sử dụng ít bandwidth hơn định tuyến động.

 +Không tiêu tốn tài nguyên để tính toán và phân tích gói tin định tuyến.

- Nhược điểm:

 +Không có khả năng tự động cập nhật đường đi.

 +Phải cấu hình thủ công khi mạng có sự thay đổi.

 +Phù hợp với mạng nhỏ, rất khó triển khai trên mạng lớn.

 +Một số tình huống bắt buộc dùng định tuyến tĩnh:

 +Đường truyền có băng thông thấp

 +Người quản trị mạng cần kiểm soát các kết nối.

## Cấu hình

```sh
ip route destination_subnet subnetmask{IP_next_hop|output_interface} [AD]
```
Trong đó:

|              | Ghi chú                                    |
|----------------------|--------------------------------------------|
| destination_subnet   | Mạng đích đến                              |
| subnetmask           | Subnet - mask của mạng đích                 |
| IP_next_hop          | Địa chỉ IP của trạm kế tiếp trên đường đi    |
| output_interface     | Cổng ra trên router                        |
| AD                   | Chỉ số AD của route khai báo                |

## Ví dụ

![](https://vnpro.vn/upload/user/images/Th%C6%B0%20Vi%E1%BB%87n/S%C6%A1-%C4%91%E1%BB%93-v%C3%AD-d%E1%BB%A5.jpg)

- Hình trên là hai router, R1 sử dụng cổng f0/0 đấu xuống mạng LAN có subnet 192.168.1.0/24. Tương tự, R2 sử dụng cổng f0/0 đấu xuống PC có subnet 192.168.2.0/24. Subnet sử dụng cho kết nối leased-line nối giữa hai router là 192.168.3.0/24. Đầu tiên, chúng ta phải cấu hình đặt địa chỉ IP cho các cổng của router, cũng như IP và Default-gateway cho các PC. Default-gateway hiểu đơn giản là IP của cổng của router gần nhất mà PC đó kết nối trực tiếp đến.

- R1 muốn đi đến mạng 192.168.2.0/24 thì phải đi ra khỏi cổng f1/0. Để thể hiện điều đó vào bảng định tuyến phải thực hiện cấu hình:

> R1 (config) # ip route 192.168.2.0 255.255.255.0 f1/0

hoặc

> R1 (config) # ip route 192.168.2.0 255.255.255.0 192.168.3.2

- R2 muốn đi đến mạng 192.168.1.0/24 thì phải đi ra khỏi cổng f1/0:

> R2 (config) # ip route 192.168.1.0 255.255.255.0 f1/0

hoặc

> R2 (config) # ip route 192.168.1.0 255.255.255.0 192.168.3.1

- Sau khi đã cấu hình xong các route cho các mạng 192.168.1.0/24 và 192.168.2.0/24, kiểm tra bảng định tuyến trên mỗi router: Bảng định tuyến của R1:

> R1#show ip route
C 192.168.1.0/24 is directly connected, FastEthernet0/0
S 192.168.2.0/24 [1/0] via 192.168.3.2
C 192.168.3.0/24 is directly connected, FastEthernet1/0

- Bảng định tuyến của R2:

> R2#show ip route
S 192.168.1.0/24 [1/0] via 192.168.3.1
C 192.168.2.0/24 is directly connected, FastEthernet0/0
C 192.168.3.0/24 is directly connected, FastEthernet1/0

Kí tự “S” ở đầu dòng thể hiện rằng các thông tin định tuyến này được học vào bảng định tuyến thông qua định tuyến tĩnh và các dòng mô tả các mạng kết nối trực tiếp được ký hiệu bởi kí tự “C” – connected – kết nối trực tiếp.



## Định tuyến động

### Khái niệm

- Định tuyến động là phương pháp định tuyến mà ở đó router sẽ tự động chia sẻ thông tin định tuyến (toàn bộ bảng định tuyến, hoặc một route trong bảng định tuyến) của mình cho các router hàng xóm (neighbor), qua đó router sẽ có thể tự động xác định đường đi tốt nhất tới một mạng đích.

### Phân loại: EGP và IGP 

#### EGP

- Giao thức định tuyến ngoài ( EGP - Exterior Gateway Protocol ) tiêu biểu là giao thức BGP ( Border Gateway Protocol ) là loại giao thức được dùng để chạy giữa các Router thuộc AS - Anonymous System ( vùng tự trị ) khác nhau , phục vụ cho việc trao đổi thông tin định tuyến .

- Giao thức định tuyến trong ( IGP - Interior Gateway Protocol ) gồm các giao thức RIP , OSPF , EIGRP . IGP là loại giao thức chạy giữa các Router nằm bên trong 1 AS . 

#### IGP
- Distance Vector (RIP)
- Hybrid Routing (EIGRP)
- Link-State (OSPF)

**1. Distance Vector (RIP)**

*a. Khái niệm*
- Routing Information Protocol (RIP) là giao thức định tuyến vector khoảng cách. Mỗi router sẽ gửi toàn bộ bảng định tuyến của nó cho router láng giềng theo định kỳ 30s/lần. Thông tin này lại tiếp tục được láng giềng lan truyền tiếp cho các láng giềng khác và cứ thế lan truyền ra mọi router trên toàn mạng. RIP chỉ sử dụng metric là hop-count để tính ra tuyến đường tốt nhất tới mạng đích. Vì sử dụng tiêu chí định tuyến là hop-count và bị giới hạn ở số hop là 15 nên giao thức này chỉ được sử dụng trong các mạng nhỏ dưới 15 hop (15 router). RIP có 2 phiên bản là RIP version 1 (RIPv1) và RIP version 2 (RIPv2).
- Các bản tin RIP được gửi đến địa chỉ IP định sẵn (multicast address) 224.0.0.9 hoặc địa chỉ broadcast 255.255.255.255 để đảm bảo rằng các router trong miền RIP nhận được thông tin.

*b. Ví dụ*

Cấu hình định tuyến tĩnh
![](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/350375573_780000983505937_214357928522389806_n.png?_nc_cat=109&ccb=1-7&_nc_sid=ae9488&_nc_ohc=0sIcSb1RypkAX_5XlhJ&_nc_oc=AQn8KW3yOc8JK9TvSZd9jaVUhQlfVD1ThIy2yWiQT7spFG49CL1cs9M-MFYXBTizQ3k&_nc_ht=scontent.fhan2-5.fna&oh=03_AdR15wavZcXemgMOvvYKYXNs1aqkPvojbbNp8UpFd3xfFA&oe=649D28BD)
=> cân bằng tải 50 50 cho 2 router
Nhược điểm: ví dụ 1 đoạn mạng hỏng, 50% bị mất hết

**Cấu hình RIP => có gửi phản hồi lại**
![](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/350239245_1478202716258412_8523284028201460734_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_ohc=Sz2kFcsRlScAX9faofM&_nc_ht=scontent.fhan2-3.fna&oh=03_AdS5h9M2XkQfO0NB9WDvKIFmiEiNC_lMeMql-NpKXt2Rlw&oe=649D1C74)

**Tính metrics**
![](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/350297122_190934467236890_3285874552135082726_n.png?_nc_cat=107&ccb=1-7&_nc_sid=ae9488&_nc_ohc=-PNp9nsyimwAX8QFDkD&_nc_ht=scontent.fhan2-5.fna&oh=03_AdToWcM5y9QNGoB2l9oUrMcJXJavoQ4wouBI209tGF--lg&oe=649D1C17)
![](https://scontent.fhan2-4.fna.fbcdn.net/v/t1.15752-9/349314046_1318731312071158_1399180318381463680_n.png?_nc_cat=110&ccb=1-7&_nc_sid=ae9488&_nc_ohc=g3Hb6rIg9RgAX_gkFXT&_nc_ht=scontent.fhan2-4.fna&oh=03_AdS3qOMiZuglH2y5IqIh6c42yNKXA7UCxlEigErLFMh6Aw&oe=649D2B3B)

=> không tói ưu đường đi, phì hợp cho hệ thống ít router

**Metrics 16:**
![](https://scontent.fhan2-4.fna.fbcdn.net/v/t1.15752-9/350375664_249542827667912_1580103675101430507_n.png?_nc_cat=110&ccb=1-7&_nc_sid=ae9488&_nc_ohc=218unuIjzmcAX-7MeZq&_nc_ht=scontent.fhan2-4.fna&oh=03_AdT1eJ6MwgGqVLNlshZdQXaT0lJvZ4CaM5hcXBSnR7zOwA&oe=649CF6FE)

![](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/350383163_834646801602782_387309679404082188_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_ohc=TBBca8EQQ60AX8C3_wr&_nc_ht=scontent.fhan2-3.fna&oh=03_AdTbvc_mrZkZpZzkFOV7MDtfobzr2kd7UvWH9gb7XF0Jug&oe=649D1C28)

![](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/350374692_531808478976857_728203120339016927_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=K0bx7aKtP4gAX_qW6LV&_nc_ht=scontent.fhan2-5.fna&oh=03_AdS2XAtj-VGS-GTZy_x78UVFraWLcZNvWmI6SvjU_pgqoQ&oe=649D0199)

=> không bao giờ chọn đường có metrics là 16 

*Ví dụ:*
Router Core không học từ DS2 vì AD của mạng 172.16.0.0/16 từ DS2=120>0 từ chính Core (mạng kết nối trực tiếp thì AD=0)
![](https://scontent.fhan2-4.fna.fbcdn.net/v/t1.15752-9/350380346_3105002066473688_5581318517432863882_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_ohc=hAhmtISWJGAAX9lHVpR&_nc_ht=scontent.fhan2-4.fna&oh=03_AdSOI-IeoUbOQLv-dPoL5bvZU9duADxGrRgsOIhSpGQRnQ&oe=649D263A)
- Nhưng khi mạng 172.16.0.0/16 bị mất kết nối với Core => Router Core học lại từ DS2 => Metrics vô hạn => Router Core sẽ gửi một thông báo cập nhật với metric 16 (không khả dụng) cho mạng này => Khi các router khác nhận được thông báo cập nhật này, nó sẽ áp đặt holddown timer (thường là 180 giây). Trong khoảng thời gian này, các router sẽ không chấp nhận bất kỳ thông báo cập nhật mới nào liên quan đến mạng 172.16.0.0/16. Điều này giúp đảm bảo rằng các router không xây dựng lại đường đi sai lệch trong quá trình cập nhật và chờ đợi thông tin định tuyến ổn định trước khi cập nhật lại.

![](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/350045918_995200904969929_1789940944085656716_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_ohc=XtVn19JQfrIAX-wqns2&_nc_ht=scontent.fhan2-3.fna&oh=03_AdTQATHYqNlrekAK534eQEZ4tD0Y1MKagZIEm1HFlYcKLw&oe=649D0115)

- Khi có gói tin được chuyển đến, auto bị hủy vì có metrics là 16
![](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/350091151_219878047474769_3984975842411867705_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_ohc=p_J4uc-kgTAAX-8mx4E&_nc_ht=scontent.fhan2-3.fna&oh=03_AdQODTLS6MJWJe2ubxmxGRWM-LKCFr1ZNjVk-SaymaXbyQ&oe=649D2724)

**Cách thức RIP trao đổi thông tin**
![](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/350385835_1234506874101615_1670048908091072155_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=tGeYkDoSDxYAX-q2xI5&_nc_ht=scontent.fhan2-5.fna&oh=03_AdSH42xL10VaFLOFj6ro8nZ-MoP8nTJ5PkoTKJzmhiHHpg&oe=649D2D2A)

=> nếu mạng 10.0.0.0/8 hỏng => bị loop => **Split Horizon**
![](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/350167389_778123957235056_5690448647117526613_n.png?_nc_cat=109&ccb=1-7&_nc_sid=ae9488&_nc_ohc=wYkP0g4DpDgAX-ClQgY&_nc_ht=scontent.fhan2-5.fna&oh=03_AdQfUSAVGH3K64MdwnHyrAeEEs5q4CiEF2LEFHjU-G5_Pw&oe=649D1A59)

**Các thời gian cần lưu ý trong RIP:**
![](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/350385861_626874119352030_3714166165255444737_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_ohc=3KaEnHwsGFUAX-PY-mU&_nc_ht=scontent.fhan2-3.fna&oh=03_AdS5vhW_Os3o2YoKPIyeFeOI3lY7nQBTh1gKVt_8lRCiIQ&oe=649D2D22)

- Holddown-timer

    Thời gian downtime cho mỗi route có định kì là 180s bắt đầu sau khi route đó mất đi. Router sẻ tiến hành quảng bá với láng giềng là route này không đến được nữa. Trong thời gian Holdtime này thì Router sẻ không nhận bất kì quảng báo nào từ route này trừ khi được neighbor cập nhật route này cho nó đầu tiên. Không chỉnh sửa bảng định tuyến cho đến khi hết thời gian timer này.

- Update timer

    Khoảng thời gian định kì mà Router chạy RIP gửi bản tin cập nhật định tuyến đến neighbor của nó trong topology. Timer mặc định là 30s.

- Invalid timer

    Khi Router nhận được bản tin cập nhật update về một subnet nào đó, sau khoảng thời gian invalid timer mà vẫn không nhận được bản cập nhật kế tiếp (theo định kì 30s/lần). Router sẻ xem route này invalid nhưng chưa vội xóa route này ra khỏi bản định tuyến mà sẻ tiến hành đưa route này vào Holddown timer. Giá trị mặc định của invalid timer là 180s

- Flush timer

    Khi Router nhận được bản tin cập nhật update về một subnet nào đó. Sau khoảng thời gian flush timer mà vẫn không nhận được bản cập nhật kế tiếp về subnet này nó sẻ xóa hoàn toàn route này ra khỏi routing table. Giá trị mặc định của flush timer là 240s

- Thời gian timer của RIP được hiểu là khi một Route bị mất thì sau 30s cập nhật Update timer nếu không tái xuất hiện thì sau 180s sẻ được đưa vào Invalid timer. Sau 60s nữa thì nó sẻ bị xóa hoàn toàn khỏi bảng định tuyến.


*Giả sử R1 biết đường mới đến 172.16.0.0/18, nó vẫn phải đợi 240s để được cập nhất*

**RIPv1, RIPv2**
- RIPv1: 
  - RIPv1 không hỗ trợ subnetting. Nó chỉ có thể nhận diện các mạng nguyên (classful networks)
  - RIPv1 sử dụng broadcasting để truyền thông tin định tuyến. Điều này gây ra một vấn đề với mạng lớn vì các router phải tiêu tốn nhiều băng thông để xử lý các gói tin định tuyến.

- RIPv2:
  - RIPv2 hỗ trợ subnetting và có thể định tuyến giữa các mạng con (subnets) trong cùng một lớp mạng.
  - RIPv2 sử dụng multicasting (specifically, IP multicast address 224.0.0.9) để truyền thông tin định tuyến. Điều này giúp giảm lưu lượng mạng và tăng hiệu suất mạng.
  
![](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/349142239_482619754030743_2814931735663262172_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_ohc=-YyXybQ-Z2MAX9T_r3X&_nc_ht=scontent.fhan2-3.fna&oh=03_AdQcgPfrQPKqV2HbzDDobZ_V7s1a6qOI57iOcyxX1zTaZA&oe=649D28DF)

**Cấu hình**
![](https://scontent.fhan2-4.fna.fbcdn.net/v/t1.15752-9/350702047_1507346046466238_6811663802413505060_n.png?_nc_cat=110&ccb=1-7&_nc_sid=ae9488&_nc_ohc=-a-IGxqBhgUAX9UOr41&_nc_ht=scontent.fhan2-4.fna&oh=03_AdTvkkuKfdXiGUGO2-Nnkanx_mp_xTqGMHOZAkGhK2iXyQ&oe=649D29C6)




**Tài liệu tham khảo:**
https://vnpro.vn/thu-vien/dinh-tuyen-dong-la-gi-cau-hinh-dinh-tuyen-dong-rip-nhu-the-nao-2349.html
https://viblo.asia/p/tim-hieu-giao-thuc-rip-DbmemoWPvAg
https://bizflycloud.vn/tin-tuc/phan-loai-cac-giao-thuc-dinh-tuyen-dong-20210319172328825.htm

