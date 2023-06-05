# Software Define Network

## 1. Tổng quan về Mạng định nghĩa mềm SDN 

### 1.1. Nhu cầu và nguyên nhân ra đời
- Mạng định nghĩa bằng phần mềm (SDN) là một công nghệ mới giúp nâng cao hiệu quả và giảm chi phí cho việc vận hành và quản trị hệ thống mạng cho các tổ chức doanh nghiệp.

- Đối với một kiến trúc mạng truyền thống, mặt phẳng dữ liệu và mặt phẳng điều khiển đều cùng nằm trên một thiết bị vật lý và mỗi thiết bị độc lập về mặt chức năng với nhau,các chính sách chuyển tiếp lưu lượng hoạt động trên trên mỗi thiết bị riêng và không có giao diện có khả năng hiển thị toàn bộ mạng.

![](https://cdn.ttgtmedia.com/visuals/searchDataCenter/operations_bestpractices/datacenter_article_019.jpg)

- Khi số lượng thiết bị trên mạng lưới càng nhiều, thì càng gây nên sự phức tạp trong mạng và làm khó khăn cho người quản trị mạng trong quá trình vận hành và điều khiển.Cùng với các thay đổi về mô hình mạng, sự gia tăng của các dịch vụ đám mây và nhu cầu phát triển của các nhà khai thác băng thông dịch vụ đưa ra một yêu cầu cần phải phát triển một giải pháp mới.

- Các nhà nghiên cứu đã phát triển một kiến trúc mạng mà ở đó nhiệm vụ điều khiển mạng được xử lý bởi các bộ điều khiển và các bộ điều khiển đó có thể tác động tới phần cứng, bộ nhớ và các chức năng của các thiết bị định tuyến (router), chuyển mạch (switch) để đạt được mục đích của người sử dụng. Do đó, mạng lưới trở nên linh hoạt hơn, hiệu suất sử dụng cao hơn và dễ quản lý hơn.
- ![](https://wiki.onosproject.org/download/attachments/2130846/dataplane.png?version=1&modificationDate=1417567449342&api=v2)


### 1.1.2. Khái niệm về mạng SDN

- Kiến trúc này phân tách chức năng điều khiển mạng (Control Plane) và chức năng vận chuyển dữ liệu (Forwarding Plane/Data Plane), điều này cho phép việc điều khiển mạng có thể lập trình được dễ dàng và hạ tầng mạng vật lý độc lập với các ứng dụng và dịch vụ mạng

![](https://scontent.fhan14-3.fna.fbcdn.net/v/t1.15752-9/350784296_1002195267860741_370288017637991112_n.png?_nc_cat=103&ccb=1-7&_nc_sid=ae9488&_nc_ohc=_yfCSLU6cREAX8MyDJl&_nc_ht=scontent.fhan14-3.fna&oh=03_AdTF6F7_yNpg-qd809diwxJ4GaWv_5N2lEWQXzVbiijvsg&oe=64A3A136)
- Data plane: Hành động di chuyển các bit cấu thành gói từ một cổng đến sang một cổng đi là trách nhiệm của data plane. Đây còn được gọi là forwarding plane. Ví dụ, trong các bộ chuyển mạch Ethernet, các gói đến từ một cổng được chuyển tiếp qua một hoặc nhiều cổng còn lại.
- •	Control plane: Sử dụng ví dụ trước đó, để chuyển tiếp gói đến cổng gửi chính xác, data plane có thể cần thêm thông tin. Trong trường hợp chuyển mạch Ethernet, cổng đi được xác định bằng cách sử dụng địa chỉ MAC đích được học bởi Switch. Hành động học hỏi và xây dựng thông tin nhận thức về mạng này là trách nhiệm của control plane.
- •	Management plane: Trong khi các mạng thực hiện công việc xử lý và chuyển tiếp lưu lượng dữ liệu, vấn đề quan trọng là phải theo dõi trạng thái của chúng và cấu hình chúng cho phù hợp với nhu cầu của bạn. Khả năng quản lý và điều khiển thiết bị mạng này là trách nhiệm của management plane.

## 2. Sự khác biệt giữa SDN với mạng truyền thống
Để hiểu rõ sự khác biệt giữa SDN và mạng truyền thống, chúng ta sẽ xem xét trên 2 khía cạnh: kiến trúc và tính năng của chúng.

### 1.2.1. Về kiến trúc
- Với hệ thống mạng truyền thống, các thiết bị mạng lớp 2 và lớp 3 phải đảm nhận nhiều chức năng để đảm bảo hoạt động (VLAN, Spanning tree, Quality of Service, Security…) 
- Đa số các thiết bị mạng và các giao thức này hoạt động độc lập với nhau vì mỗi nhà sản xuất thiết bị cung cấp các giải pháp mạng khác nhau
=> Điều này tạo ra sự phân mảnh đối với toàn bộ hệ thống mạng đồng thời làm giảm hiệu năng hoạt động.

![](https://packetlife.net/media/blog/attachments/680/SDN_controller.png)

- Đối với mạng điều khiển bằng phần mềm SDN, việc điều khiển được tập trung tại lớp Controller Layer, các thiết bị mạng chỉ có nhiệm vụ chuyển tiếp gói tin do đó sự khác biệt giữa các nhà sản xuất sẽ không ảnh hưởng tới toàn hệ thống mạng (giống như TCP/IP)
- Về phía người quản trị mạng, họ không cần trực tiếp làm việc tại các thiết bị mạng để cấu hình, tích hợp vào hệ thống mà chỉ cần thông qua các API đã được cung cấp cùng với kiến thức cơ bản về TCP/IP đều có thể xây dựng ứng dụng cho toàn hệ thống mạng.

### 1.2.2. Về tính năng
- Sự khác biệt căn bản nhất giữa SDN và mạng truyền thống là SDN dựa trên phần mềm trong khi mạng truyền thống thường dựa trên phần cứng. Do dựa trên phần mềm, SDN linh hoạt hơn, cho phép người dùng kiểm soát tốt hơn và dễ dàng quản lý tài nguyên hầu như trên chỉ trên mặt phẳng điều khiển.
- Bộ điều khiển SDN sử dụng giao diện giao tiếp với các API. Với giao diện này, các nhà phát triển ứng dụng có thể lập trình trực tiếp mạng, trái ngược với việc sử dụng các giao thức được yêu cầu bởi mạng truyền thống.
- SDN cho phép người dùng sử dụng phần mềm để cung cấp các thiết bị mới thay vì sử dụng cơ sở hạ tầng vật lý, do đó, quản trị viên có thể định tuyến đường truyền, lưu lượng cũng như chủ động lập lịch cho các dịch vụ mạng

## 1.3.	Tìm hiểu kiến trúc của SDN

![](https://www.researchgate.net/publication/329735894/figure/fig1/AS:705069599182852@1545113100857/SDN-Controller-In-this-there-are-four-bounds-in-this-SDN-and-they-are1-Northbound-API.ppm)

- SDN được chia làm ba lớp: lớp ứng dụng (Application Layer), lớp điều khiển (Control Layer) và lớp thiết bị hạ tầng (Infrastructure Layer). Các lớp sẽ liên kết với nhau thông qua giao thức hoặc các API.

- Lớp ứng dụng SDN là các chương trình giao tiếp với bộ điều khiển SDN thông qua các giao diện lập trình ứng dụng API, cho phép lớp ứng dụng lập trình (cấu hình) mạng (ví dụ như điều chỉnh các tham số trễ, băng thông, định tuyến, …) qua lớp điều khiển để tối ưu hoạt động của mạng lưới theo một yêu cầu cụ thể của người quản trị. Ngoài ra, các ứng dụng sẽ đưa ra mô hình trực quan về mạng lưới bằng cách thu thập thông tin từ bộ điều khiển cho các mục đích ra quyết định. Các ứng dụng này có thể bao gồm quản lý mạng, phân tích hoặc các ứng dụng kinh doanh được sử dụng để chạy các trung tâm dữ liệu lớn. Ví dụ: Một ứng dụng phân tích có thể được xây dựng để nhận ra hoạt động mạng đáng ngờ vì mục đích bảo mật.

- Lớp thiết bị hạ tầng (Infrastructure Layer) bao gồm các thiết bị mạng (thiết bị vật lý hoặc ảo hóa) thực hiện việc chuyển tiếp gói tin dưới sự điều khiển của Lớp điểu khiển. Một thiết bị mạng có thể hoạt động theo sự điều khiển của nhiều controller khác nhau, điều này giúp tăng cường khả năng ảo hóa của mạng.

- Lớp điều khiển là trung tâm của kiến trúc mạng SDN. Nó cung cấp cho người quản trị tổng quát về toàn mạng, quyết định triển khai các chính sách và điều khiển toàn bộ các thiết bị trong hạ tầng mạng. Nó cung cấp một giao diện Northbound API cho việc giao tiếp với lớp ứng dụng. Thực hiện các chính sách quyết định liên quan tới định tuyến, chuyển tiếp, redirect, cân bằng tải, hoặc tương tự.
  - Bên trong SDN controller chưa các module giúp quản lý topo mạng, quản lý trạng thái, quản lý các thiết bị, quản lý các cảnh báo, tính toán đường đi ngắn nhất và cung cấp các kỹ thuật bảo mật.
  - SDN controller sử dụng giao điện Southbound để giao tiếp với các thiết bị lớp hạ tầng. Các giao thức phổ biến là Openflow, OVSDB, ForCES, OF-Config... Thông qua các giao thức này SDN controller có thể cấu hình và thu thập các thông tin trạng thái trên thiết bị.

## Tài liệu tham khảo:
[1]- https://vietnix.vn/sdn-la-gi/
[2]- https://iopscience.iop.org/article/10.1088/1757-899X/121/1/012003/pdf#:~:text=The%20list%20of%20SDN%20challenges,errors%20and%20increase%20network%20availability.

