# Software Define Network

## 1. Tổng quan về Mạng định nghĩa mềm SDN 

### 1.1. Nhu cầu và nguyên nhân ra đời
- Mạng định nghĩa bằng phần mềm (SDN) là một công nghệ mới giúp nâng cao hiệu quả và giảm chi phí cho việc vận hành và quản trị hệ thống mạng cho các tổ chức doanh nghiệp.

- Đối với một kiến trúc mạng truyền thống, mặt phẳng dữ liệu và mặt phẳng điều khiển đều cùng nằm trên một thiết bị vật lý và mỗi thiết bị độc lập về mặt chức năng với nhau,các chính sách chuyển tiếp lưu lượng hoạt động trên trên mỗi thiết bị riêng và không có giao diện có khả năng hiển thị toàn bộ mạng.

![](https://cdn.ttgtmedia.com/visuals/searchDataCenter/operations_bestpractices/datacenter_article_019.jpg)

- Khi số lượng thiết bị trên mạng lưới càng nhiều, thì càng gây nên sự phức tạp trong mạng và làm khó khăn cho người quản trị mạng trong quá trình vận hành và điều khiển.Cùng với các thay đổi về mô hình mạng, sự gia tăng của các dịch vụ đám mây và nhu cầu phát triển của các nhà khai thác băng thông dịch vụ đưa ra một yêu cầu cần phải phát triển một giải pháp mới.

- Các nhà nghiên cứu đã phát triển một kiến trúc mạng mà ở đó nhiệm vụ điều khiển mạng được xử lý bởi các bộ điều khiển và các bộ điều khiển đó có thể tác động tới phần cứng, bộ nhớ và các chức năng của các thiết bị định tuyến (router), chuyển mạch (switch) để đạt được mục đích của người sử dụng. Do đó, mạng lưới trở nên linh hoạt hơn, hiệu suất sử dụng cao hơn và dễ quản lý hơn.
- ![](https://wiki.onosproject.org/download/attachments/2130846/dataplane.png?version=1&modificationDate=1417567449342&api=v2)


### 1.2. Khái niệm về mạng SDN

- Kiến trúc này phân tách chức năng điều khiển mạng (Control Plane) và chức năng vận chuyển dữ liệu (Forwarding Plane/Data Plane), điều này cho phép việc điều khiển mạng có thể lập trình được dễ dàng và hạ tầng mạng vật lý độc lập với các ứng dụng và dịch vụ mạng

![](https://scontent.fhan14-3.fna.fbcdn.net/v/t1.15752-9/350784296_1002195267860741_370288017637991112_n.png?_nc_cat=103&ccb=1-7&_nc_sid=ae9488&_nc_ohc=_yfCSLU6cREAX8MyDJl&_nc_ht=scontent.fhan14-3.fna&oh=03_AdTF6F7_yNpg-qd809diwxJ4GaWv_5N2lEWQXzVbiijvsg&oe=64A3A136)
- Data plane: Hành động di chuyển các bit cấu thành gói từ một cổng đến sang một cổng đi là trách nhiệm của data plane. Đây còn được gọi là forwarding plane. Ví dụ, trong các bộ chuyển mạch Ethernet, các gói đến từ một cổng được chuyển tiếp qua một hoặc nhiều cổng còn lại.
- •	Control plane: Sử dụng ví dụ trước đó, để chuyển tiếp gói đến cổng gửi chính xác, data plane có thể cần thêm thông tin. Trong trường hợp chuyển mạch Ethernet, cổng đi được xác định bằng cách sử dụng địa chỉ MAC đích được học bởi Switch. Hành động học hỏi và xây dựng thông tin nhận thức về mạng này là trách nhiệm của control plane.
- •	Management plane: Trong khi các mạng thực hiện công việc xử lý và chuyển tiếp lưu lượng dữ liệu, vấn đề quan trọng là phải theo dõi trạng thái của chúng và cấu hình chúng cho phù hợp với nhu cầu của bạn. Khả năng quản lý và điều khiển thiết bị mạng này là trách nhiệm của management plane.

## 2. Sự khác biệt giữa SDN với mạng truyền thống
Để hiểu rõ sự khác biệt giữa SDN và mạng truyền thống, chúng ta sẽ xem xét trên 2 khía cạnh: kiến trúc và tính năng của chúng.

### 2.1. Về kiến trúc
- Với hệ thống mạng truyền thống, các thiết bị mạng lớp 2 và lớp 3 phải đảm nhận nhiều chức năng để đảm bảo hoạt động (VLAN, Spanning tree, Quality of Service, Security…) 
- Đa số các thiết bị mạng và các giao thức này hoạt động độc lập với nhau vì mỗi nhà sản xuất thiết bị cung cấp các giải pháp mạng khác nhau
=> Điều này tạo ra sự phân mảnh đối với toàn bộ hệ thống mạng đồng thời làm giảm hiệu năng hoạt động.

![](https://packetlife.net/media/blog/attachments/680/SDN_controller.png)

- Đối với mạng điều khiển bằng phần mềm SDN, việc điều khiển được tập trung tại lớp Controller Layer, các thiết bị mạng chỉ có nhiệm vụ chuyển tiếp gói tin do đó sự khác biệt giữa các nhà sản xuất sẽ không ảnh hưởng tới toàn hệ thống mạng (giống như TCP/IP)
- Về phía người quản trị mạng, họ không cần trực tiếp làm việc tại các thiết bị mạng để cấu hình, tích hợp vào hệ thống mà chỉ cần thông qua các API đã được cung cấp cùng với kiến thức cơ bản về TCP/IP đều có thể xây dựng ứng dụng cho toàn hệ thống mạng.

### 2.2. Về tính năng
- Sự khác biệt căn bản nhất giữa SDN và mạng truyền thống là SDN dựa trên phần mềm trong khi mạng truyền thống thường dựa trên phần cứng. Do dựa trên phần mềm, SDN linh hoạt hơn, cho phép người dùng kiểm soát tốt hơn và dễ dàng quản lý tài nguyên hầu như trên chỉ trên mặt phẳng điều khiển.
- Bộ điều khiển SDN sử dụng giao diện giao tiếp với các API. Với giao diện này, các nhà phát triển ứng dụng có thể lập trình trực tiếp mạng, trái ngược với việc sử dụng các giao thức được yêu cầu bởi mạng truyền thống.
- SDN cho phép người dùng sử dụng phần mềm để cung cấp các thiết bị mới thay vì sử dụng cơ sở hạ tầng vật lý, do đó, quản trị viên có thể định tuyến đường truyền, lưu lượng cũng như chủ động lập lịch cho các dịch vụ mạng

## 3.	Tìm hiểu kiến trúc của SDN

![](https://www.researchgate.net/publication/329735894/figure/fig1/AS:705069599182852@1545113100857/SDN-Controller-In-this-there-are-four-bounds-in-this-SDN-and-they-are1-Northbound-API.ppm)

- SDN được chia làm ba lớp: lớp ứng dụng (Application Layer), lớp điều khiển (Control Layer) và lớp thiết bị hạ tầng (Infrastructure Layer). Các lớp sẽ liên kết với nhau thông qua giao thức hoặc các API.

- Lớp ứng dụng SDN là các chương trình giao tiếp với bộ điều khiển SDN thông qua các giao diện lập trình ứng dụng API, cho phép lớp ứng dụng lập trình (cấu hình) mạng (ví dụ như điều chỉnh các tham số trễ, băng thông, định tuyến, …) qua lớp điều khiển để tối ưu hoạt động của mạng lưới theo một yêu cầu cụ thể của người quản trị. Ngoài ra, các ứng dụng sẽ đưa ra mô hình trực quan về mạng lưới bằng cách thu thập thông tin từ bộ điều khiển cho các mục đích ra quyết định. Các ứng dụng này có thể bao gồm quản lý mạng, phân tích hoặc các ứng dụng kinh doanh được sử dụng để chạy các trung tâm dữ liệu lớn. Ví dụ: Một ứng dụng phân tích có thể được xây dựng để nhận ra hoạt động mạng đáng ngờ vì mục đích bảo mật.

- Lớp thiết bị hạ tầng (Infrastructure Layer) bao gồm các thiết bị mạng (thiết bị vật lý hoặc ảo hóa) thực hiện việc chuyển tiếp gói tin dưới sự điều khiển của Lớp điểu khiển. Một thiết bị mạng có thể hoạt động theo sự điều khiển của nhiều controller khác nhau, điều này giúp tăng cường khả năng ảo hóa của mạng.

- Lớp điều khiển là trung tâm của kiến trúc mạng SDN. Nó cung cấp cho người quản trị tổng quát về toàn mạng, quyết định triển khai các chính sách và điều khiển toàn bộ các thiết bị trong hạ tầng mạng. Nó cung cấp một giao diện Northbound API cho việc giao tiếp với lớp ứng dụng. Thực hiện các chính sách quyết định liên quan tới định tuyến, chuyển tiếp, redirect, cân bằng tải, hoặc tương tự.
  - Bên trong SDN controller chưa các module giúp quản lý topo mạng, quản lý trạng thái, quản lý các thiết bị, quản lý các cảnh báo, tính toán đường đi ngắn nhất và cung cấp các kỹ thuật bảo mật.
  - SDN controller sử dụng giao điện Southbound để giao tiếp với các thiết bị lớp hạ tầng. Các giao thức phổ biến là Openflow, OVSDB, ForCES, OF-Config... Thông qua các giao thức này SDN controller có thể cấu hình và thu thập các thông tin trạng thái trên thiết bị.


## 4.Giao thức Openflow

### 4.1. Các thành phần chính trong OpenFLow switch
- Các thành phần chính của một OpenFlow switch:
![](https://github.com/hocchudong/thuctap012017/raw/master/TamNT/TimHieuSDN/images/2.0.1.png)

- Một OpenFlow Logical Switch bao gồm bảng Flow table và Group table. Switch này truyền thông qua các kênh OpenFlow channel với một controller bên ngoài.

- Controller sử dụng giao thức chuyển mạch OpenFlow để thao tác với switch. Nó có thể thêm, cập nhật và xóa các flow entry trong bảng flow table.

- Mỗi flow table chứa các flow entry, mỗi entry bao gồm Match fields (các trường thông tin để so khớp), Counter (đếm số lượng gói tin) và tập các Instructions (hướng dẫn để xử lý gói tin).
Khi một gói tin được nhận bởi switch, nó được so khớp với các flow entry trong bảng flow table theo thứ tự ưu tiên.

- Nếu gói tin khớp với một flow entry, các hướng dẫn liên kết với entry đó được thực hiện. Điều này bao gồm các action (hành động) để chuyển tiếp, sửa đổi hoặc xử lý gói tin.

- Nếu không có flow entry nào khớp, gói tin có thể được chuyển tiếp tới controller thông qua kênh OpenFlow channel, bị drop hoặc tiếp tục tới bảng flow table tiếp theo theo cấu hình của table-miss flow entry.

- Các flow entry có thể chuyển tiếp gói tin tới các Port (cổng), có thể là port vật lý hoặc port logic được định nghĩa bởi switch hoặc một port dự trữ được định nghĩa bởi OpenFlow.

- Các action gán với flow entry có thể chuyển hướng gói tin trực tiếp tới một nhóm, thực hiện xử lý bổ sung.

- Group table chứa các group entry, mỗi entry chứa một danh sách các tập action. Các action này được áp dụng cho gói tin gửi tới nhóm, cho phép thực hiện các chuyển tiếp phức tạp như flooding, multipath hoặc link aggregation.

Thông qua các bảng flow table, group table và kênh OpenFlow channel, OpenFlow cung cấp khả năng quản lý và kiểm soát linh hoạt trong mạng SDN, cho phép controller điều khiển switch và xử lý các gói tin theo các quy tắc và hướng dẫn đã được định nghĩa trước.

### 4.2. Các loại port trong OpenFLow switch

OpenFlow port là các giao diện mạng để gửi gói tin giữ quá trình xử lý OpenFlow và các thành phần trong mạng. Các switch OpenFlow kết nối một cách logi với nhau thông qua OpenFlow port, một gói tin có thể được chuyển tiếp từ một OpenFlow switch tới các OpenFlow switch khác chỉ thông qua một port OpenFlow ra trên switch đầu tiền và một cổng vào trên Switch thứ 2.

Một switch OpenFlow có thể có một số OpenFlow phục vụ cho tiến trình xử lý OpenFlow. Các OpenFlow port có thể không được định danh bởi các interface cung cấp bởi switch phần cứng, một vài interface có thể vô hiệu OpenFlow, và OpenFLow switch có thể định nghĩa thêm các OpenFlow port bổ sung.

Các gói tin OpenFlow được nhận trên một ingress port và được xử lý bởi OpenFlow pipeline (có thể chuyển tiếp gói tin ra cổng ra – output port). Ingress port là một thuộc tính của gói tin trong OpenFlow pipeline và đại diện cho port mà gói tin nhận vào từ OpenFlow switch. Ingress port có thể được sử dụng khi match các gói tin. OpenFlow pipeline có thể quyết định gửi gói tin trên cỏng ra nào sử dụng action output (định nghĩa các thức gói tin ra lại mạng)

Một OpenFLow switch phải hổ trợ 3 loại cổng OpenFLow : physical port – cổng vật lý, logical port – cổng logic và reserved port – cổng dự trữ.

#### 1.	Physical port – cổng vật lý

- Là cổng được switch định nghĩa và tương ứng với các interface vật lý trên switch. Ví dụ: trên một Ethernet switch, các cổng vật lý ánh xạ một – một tới interface Ethernet.

- Trong một số mô hình triển khai, OpenFlow switch có thể được ảo hóa thông qua switch phần cứng. Trong những trường hợp đó, một OpenFlow physical port có thể đại diện cho một phần ảo tương ứng với interface vật lý trên switch.

<a name = '2'></a>
#### 2.	Logical port – cổng logic

- Là các cổng được switch định nghĩa, không tương ứng trực tiếp với các interface vật lý của switch. Cổng logic là khác niệm mức cao mà có thể được định nghĩa trong các switch không chỉ trong OpenFLow switch ( ví dụ: link aggregation groups, tunnel và loopback interface).

- Cổng logic có thể đóng gói gói tin và có thể ánh xạ ra nhiều cổng vật lý. Quá trình xử lý thực hiện bởi cổng logic là quá trình độc lập và phải trong suốt với quá trình xử lý OpenFlow, và những cổng đó phải tương tác với tiến trình xử lý OpenFlow giống như Cổng vật lý định nghĩa ở trên.

- Sự khác biệt giữa cổng vật lý và cổng logic là: một gói tin gán với cổng logic có thể có thêm trường pipeline filed gọi là Tunnel-ID gán với nói và khi một gói tin nhận được trên cỏng logic được gửi tới controller, cả coongr logic và các cổng vật lý bên dưới đều báo cáo cho controller.

<a name = '3'></a>
#### 3.	Reserved port – cổng dự trữ

- Là các poirt được định nghĩa bởi OpenFlow switch, có thể sử dụng để chuyển tiếp gói tin tới controller, hoặc flooding hoặc chuyển tiếp theo phương thức chuyển mạch thông thường.

(updating...)

<a name = '4'></a>
#### 4.	Port changes 

- Cấu hình switch, ví dụ sử dụng giao thức cấu hình OpenFlow, có thể thêm hoặc xóa các port khỏi OpenFlow switch bất kì thời điểm nào. Switch có thể thay đổi trạng thái port dựa vào cơ chế port bên dưới, ví dụ port bị tắt. Controller hoặc cấu hình switch có thể thay đổi cấu hình port. Bất kì thay đổi nào dấn tới thay đổi trạng thái hoặc cấu hình port phải được truyền thông tới OpenFlow controller.

- Việc thêm, sửa hay xóa port không làm thay đổi nội dung trong flow table, các entry flow cụ thể tham chiếu tới các port đó không được chỉnh sửa hoặc xóa (các flow entry có thể tham chiếu tới các port thông qua match hoặc action). Chuyển tiếp gói tin tới một port không còn tồn tại sẽ bị drop. Tuy nhiên, hành vi của một số nhóm có thể thay đổi thông qua liveness checking.

- Nếu một port bị xóa và port number của nó sau đó được sử dụng lại cho một cổng vật lý hoặc logic khác, bất kì flow entry hoặc group entry nào còn tham chiếu tới port number đó có thể có hiệu lực với port mới, có thể với kết quả không mong muốn. Do đó, khi một port bị xóa thì nên xóa các flow entry hoặc group entry tham chiếu tới nó, nếu cần.

<a name = '5'></a>


### 4.3. Flow table và flow entry
Một bảng flow table gồm các flow entry:

![img](https://github.com/hocchudong/thuctap012017/raw/master/TamNT/TimHieuSDN/images/2.2.2.png)

Mỗi flow table gồm các cột sau:

- **Match field**: để so sánh với các gói tin. Trường này bao gồm thông tin về ingress port và các packet header, và có thể các trường pipeline field thêm vào như metadata chỉ định trong các bảng trước đó.

- **Priority**: Mức độ ưu tiên của flow entry.

- **Counters**: được cập nhật khi các gói tin được match.

- **Instructions**: điều chỉnh thiết lập action hoặc xử lý pipeline.

- **Timeouts**: số lượng thời gian giới hạn hoặc thời gian chờ trước khi flow bị vô hiệu bởi switch.

- **Cookie**: Dữ liệu không rõ ràng được chọn bởi switch. Có thể được sử dụng bởi controoler để lọc các flow entry ảnh howngr bởi các flow tĩnh, yêu cầu chỉnh sửa hoặc xóa flow. Không sử dụng khi xử lý các gói tin.

- **Flags**: Các flag thay đổi cách mà các flow entry được quản lý, ví dụ: cờ OFPFF_SEND_FLOW_REM tự động loại bỏ các bản tin bị xóa cho flow entry đó.

Một entry flow trong bảng được xác định bởi trường match fields và priority của nó: 2 trường này kết hợp tạo nên sự duy nhất cho flow entry trong một bảng. Flow không khớp (tất cả các trường đều không khớp) và có độ ưu tiên bằng 0 được gọi là flow entry table-miss.
Instruction có thể chứa các action được thực hiện trên gói tin ở một vài điểm của của pipeline. Action `set-field` có thể chỉ định viết một số trường header. 

<a name = '3'></a>

- Ngoài các flow entry mỗi flow table còn chứa một table miss flow entry được sử dụng để xử lý các gói tin khi không có flow entry nào trong flow table match với gói tin đó. Table miss flow entry có thể sẽ chuyển tiếp gói tin đó đến controller, gửi gói tin tới flow table tiếp theo hoặc loại bỏ gói tin.

![](https://thinhcaominh.files.wordpress.com/2019/05/sdn_openflow_pipeline_processing.png)

Với các openflow switch chứa nhiều bảng flow table, các flow table sẽ được đánh số bắt đầu từ table 0. Việc xử lý pipeline sẽ luôn được bắt đầu tại table 0. Các table khác có thể sẽ được sử dụng phụ thuộc vào lối ra của match entry trong table đầu tiên. Việc chia ra nhiều flow table thay vì chỉ sử dụng một flow table sẽ tiết kiệm thời gian xử lý các gói tin hơn.

Trong một số trường hợp Flow table có thể chuyển hướng của một flow (các gói tin cùng loại) tới một group table để kích hoạt một hoặc nhiều hành động để xử lý flow. Metter table có thể được kích hoạt để tác động đến hiệu suất xử lý của một flow.

Group table cho phép nhóm một số lượng port thành một output port thiết lập hỗ trợ multicasting, multipath, indirection và fast-failover.

Metter table cho phép Openflow switch thực hiện các hành động QoS. Metter table sẽ thực hiện tính toán tốc độ của gói tin và kích hoạt điều khiển tốc độ gói tin đó. Metter được gắn trực tiếp vào các flow entry, bất kỳ một flow entry nào cùng có thể chỉ định metter. Metter đo và kiểm soát tốc độ tổng hợp của tất cả các flow entry mà nó được gắn vào.

![](https://thinhcaominh.files.wordpress.com/2019/05/openflow_chart_processing.png)

Việc xử lý một gói tin bởi Openflow switch sẽ được thực hiện như trên hình vẽ. Khi một gói tin từ ngoài mạng được gửi tới Switch, quá trình xử lý gói tin được bắt đầu từ table 0. Gói tin sẽ được kiểm tra có một flow entry nào match với gói tin, trỏ gói tin tới table thứ n nào không? Nếu không có chúng sẽ được tìm kiếm trong table miss flow entry. Nếu tiếp tục không tìm thấy thì gói tin lập tức bị drop. Ngược lại nếu tồn tại một flow entry nào đó match với gói tin bên trong flow table hoặc table miss flow entry thì counter sẽ được update và thực thi các câu lệnh: Cập nhật thiết lập hành động, cập nhật các trường thiết lập gói tin, cập nhật metadata. Gói tin được gửi đến table thứ n, tại đây gói tin sẽ tiếp tục kiểm tra xem có cần phải gửi đến table nào khác không, nếu có thì gói tin tiếp tục được gửi đến table đó. Nếu không thì thực thi hành động đã được thiết lập.

Việc sử dụng Openflow Switch là cách làm đơn giản và tiết kiệm chi phí để tiến tới SDN. Đây cũng là cách làm của nhiều Vendor cung cấp giải pháp SDN như giải pháp Nuage của Nokia, Agile của Huawei, Programbale flow switch của NEC… Tận dụng những tài nguyên mã nguồn mở sau đó tối ưu, tùy biến thành giải pháp của riêng họ.

Song song với lợi ích thì việc triển khai Openflow switch cũng tiềm ẩn rủi ro. Hiện nay Openflow switch và giao thức Openflow mới chỉ được chuẩn hóa bởi tổ chức ONF. Chưa có một tổ chức nào đủ uy tín, sức ảnh hưởng để chuẩn hóa Openflow trở thành tiêu chuẩn giao thức chung cho SDN. Dẫn đến các giải pháp SDN của các hãng cung cấp lại đi theo các hướng khác nhau và lock in vendor. Điều này khiến Openflow Switch sẽ không thể kết nối với SDN controller từ các hãng cung cấp thiết bị lớn. Openflow switch buộc phải sử dụng các bộ SDN controller mã nguồn mở và hỗ trợ Openflow, nhưng hiệu suất thiết bị thì sẽ khó được đảm bảo.

Openflow switch cũng có thể được sử dụng thay thế cho các router, switch trong mạng truyền tải truyền thống. Openflow switch có thể được sử dụng để thay thế các thiết bị từ lớp Core tới lớp Access như các router đặt tại vị trí của khách hàng, thay thế cho site router, thiết bị AGG, Core tỉnh, Core khu vực. Giúp tập trung hóa việc điều khiển, tiết kiệm chi phí cho các thiết bị chuyển mạch. Việc triển khai có thể chỉ cần cài đặt trên các thiết bị white box. Năng lực của white box được đầu tư phù hợp nhu cầu, vị trí thiết bị thay thế.

Openflow switch cũng có thể được sử dụng để triển khai mạng campus nội bộ, sử dụng cho các phòng ban để kiểm soát, tối ưu cho các ứng dụng.