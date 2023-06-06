## Mục lục



## Mở đầu

VictoriaMetrics là hoàn toàn miễn phí và sẵn sàng để tải xuống và cài đặt các phiên bản mới nhất từ nhà phát hành.

Được chia rõ ràng thành 2 lựa chọn độc lập đó là Single-node và cluster.

- [Single-node version](https://github.com/VictoriaMetrics/VictoriaMetrics): dễ dàng cài đặt, triển khai, cấu hình, thân thiện với RAM, CPU, dung lượng lưu trữ mặc định hiện có. Với các cấu hình mặc định cực kỳ tối ưu.
- [Cluster version](https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html): hiệu suất cao khi được giám sát các hệ thống lớn, hỗ trợ đầy đủ các tính năng mà single-node có, mở rộng theo nhiều ngang nhanh hơn, hỗ trợ lưu trữ phân tán, tính sẵn sàng cao.
Tuy nhiên, nó khó để cài đặt, triển khai, cấu hình. Yêu cầu người quản trị có kinh nghiệm trong việc vận hành và giám sát hệ thông.

Mặc dù chia ra hai lựa chọn rõ ràng như thê nhưng chúng vẫn sẵn sàng để tải xuống theo các cách phổ biến như:

- [binary releases](https://github.com/VictoriaMetrics/VictoriaMetrics/releases): tự tải về, tự cài đặt các phiên bản mong muốn, tự cấu hình luôn

- [Docker images trên docker hub](https://hub.docker.com/r/victoriametrics/victoria-metrics/): gần như sẵn sàng để sử dụng chỉ cần cấu hình theo nhu cầu của hệ thống hiện tại.

- [Helm charts for single-node and cluster versions of VictoriaMetrics.](https://github.com/VictoriaMetrics/helm-charts)

- [Kubernetes operator for VictoriaMetrics.](https://github.com/VictoriaMetrics/operator)

- [Ansible role for installing cluster VictoriaMetrics (by VictoriaMetrics).](https://github.com/VictoriaMetrics/ansible-playbooks)

- [Ansible role for installing cluster VictoriaMetrics (by community).](https://github.com/Slapper/ansible-victoriametrics-cluster-role)

- [Ansible role for installing single-node VictoriaMetrics (by community).](https://github.com/dreamteam-gg/ansible-victoriametrics-role)

- [Snap package for VictoriaMetrics.](https://snapcraft.io/victoriametrics)

_Trong bài viết này sẽ tập trung chủ yếu vào tìm hiểu cluster_


## Cluster overview - Các thành phần cơ bản

Ngoài các thành phần cơ bản cần có của VictoriaMetrics ra thì một cụm VictoriaMetrics còn có các thành phần sau:

- `vmselect`: thực hiện các truy vấn bằng cách tìm nạp dữ liệu cần thiết từ tất cả vmstorage trên các nút được định cấu hình

- `vmstorage`: lưu trữ dữ liệu thô và trả về dữ liệu được truy vấn trong khoảng thời gian nhất định cho các bộ lọc đã gán nhãn nhất định

- `vminsert`: chấp nhận dữ liệu được nhập từ các công cụ khác - có tương thích với Prometheus, và phân phối dữ liệu đó đến các `vmstorage` trên các nút theo hàm băm với sự nhất quán dựa trên tên chỉ số (metric name) và tất cả các nhãn của nó (all its labels)

Mỗi dịch vụ có thể cài đặt trên các nút độc lập, mở rộng độc lập và có thể chạy trên phần cứng phù hợp nhất. Các `vmstorage` trên các nút riêng biệt sẽ không biết về nhau, không giao tiếp với nhau và không chia sẻ bất kỳ dữ liệu nào. Đây là một kiến ​​trúc không chia sẻ gì cả ([shared nothing architecture](https://en.wikipedia.org/wiki/Shared-nothing_architecture)). Nó làm tăng tính khả dụng của cụm và đơn giản hóa việc bảo trì cụm cũng như mở rộng quy mô cụm.

![Cluster-VictoriaMetrics_cluster-scheme](images/Cluster-VictoriaMetrics_cluster-scheme.png)

### Multitenancy (đa người dùng trong hệ thống)

Một cụm VictoriaMetrics hỗ trợ cho nhiều người dùng tới hệ thống (multiple isolated tenants (aka namespaces)). Mỗi người dùng (Tenants) sẽ được xác định bởi `accountID` hoặc `accountID:projectID` Được đặt bên trong các yêu cầu URLs (request urls). Xem chi tiết trong tài liệu sau: <https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html#url-format>

Một vài điều về tenants của VictoriaMetrics:

- Mỗi `accountID` và `projectID` được xác định bởi một số nguyên 32 bit tùy ý trong phạm vi [0 .. 2^32). Nếu `projectID` bị thiếu, nó sẽ tự động được gán là `0`. Các thông tin khác về tenant như: tokens, name, limits (giới hạn), accounting (các hành động truy vấn),v.v sẽ được lưu trữ trong cơ sở dữ liệu quan hệ riêng biệt. Thứ chịu trách nhiệm quản lý cơ sở dữ liệu quan hệ đó cần phải đứng bên trên (hoặc phía trước) VictoriaMetrics như `vmauth` or `vmgateway`.

- Tenants được tạo tự động khi điểm dữ liệu đầu tiên được viết vào tenant cụ thể.

- Dữ liệu cho tất cả các tenant được phân bố đồng đều giữa các node `vmstorage` có sẵn. Điều này đảm bảo tải được phân bố đồng đều giữa các node `vmstorage` khi các tenant khác nhau có số lượng dữ liệu và tải truy vấn khác nhau.

- Hiệu suất cơ sở dữ liệu và sử dụng tài nguyên không phụ thuộc vào số lượng tenant mà phụ thuộc chủ yếu vào tổng số lượng chuỗi thời gian hoạt động của tất cả các tenant. Một chuỗi thời gian được coi là hoạt động nếu nó nhận được ít nhất một mẫu trong giờ cuối cùng hoặc nó đã được truy vấn trong giờ cuối cùng.

- VictoriaMetrics không hỗ trợ truy vấn nhiều tenant trong một yêu cầu duy nhất.

- Danh sách các tenant đã đăng ký có thể được lấy thông qua url `http://<vmselect>:8481/admin/tenants` với quyền của người quản trị (admin). Xem chi tiết tại tài liệu: <https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html#url-format>

- VictoriaMetrics cung cấp các thống kê theo tenant khác nhau thông qua các chỉ số tương ứng. Xem chi tiết tại: <https://docs.victoriametrics.com/PerTenantStatistic.html>

### Multitenancy via labels (đa người dùng thông qua gán nhãn)

vminsert có thể chấp nhận dữ liệu từ nhiều tenant thông qua các giá trị multitenant cuối đặc biệt `http://vminsert:8480/insert/multitenant/<suffix>`, trong đó `suffix` có thể được thay thế bằng bất kỳ hậu tố nào, được hỗ trợ cho việc tiếp nhận dữ liệu, từ danh sách này: <https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html#url-format>. Trong trường hợp này, `account id` and `project id` được lấy từ các nhãn (label) `vm_account_id` và `vm_project_id`của các mẫu đầu vào. Nếu các nhãn `vm_account_id` hoặc `vm_project_id` bị thiếu hoặc không hợp lệ, thì `accountID` hoặc `projectID` tương ứng được đặt thành `0`. Những nhãn này sẽ được tự động loại bỏ khỏi các mẫu trước khi chuyển tiếp chúng đến `vmstorage`. Ví dụ, nếu các mẫu sau được viết vào `http://vminsert:8480/insert/multitenant/prometheus/api/v1/write:`.

```sh
http_requests_total{path="/foo",vm_account_id="42"} 12
http_requests_total{path="/bar",vm_account_id="7",vm_project_id="9"} 34
```

Khi đó: `http_requests_total{path="/foo"} 12` sẽ được lưu trữ với tenant có `accountID=42, projectID=0`, còn `http_requests_total{path="/bar"} 34` sẽ được lưu trữ với `accountID=7, projectID=9`.

Nhãn `vm_account_id` và `vm_project_id` được trích xuất sau khi áp dụng [relabeling](https://docs.victoriametrics.com/relabeling.html) (bộ lọc lại) thông qua việc sử dụng cờ dòng lệnh `-relabelConfig`, do đó những nhãn này có thể được đặt ở giai đoạn này.

>Các lời khuyên bảo mật: nên hạn chế truy cập đến các điểm cuối `multitenant` chỉ cho các nguồn đáng tin cậy, vì nguồn không đáng tin cậy có thể phá vỡ dữ liệu theo tenant bằng cách viết các mẫu không mong muốn vào các tenant tùy ý.

## Các cách cài đặt được khuyến nghị

- Nếu bạn là nhà phát triển hoặc người dùng muốn thử nghiệm các phiên bản mới nhất thì có thể xem hướng dẫn sau: <https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html#development-builds>

- Có thể tải xuống và tự xây dựng từ mã nguồn chính thức trên github. Mã nguồn: <https://github.com/VictoriaMetrics/VictoriaMetrics/releases>

- Hoặc tải xuống từ Docker:

  - `vminsert`: <https://hub.docker.com/r/victoriametrics/vminsert/tags>
  - `vmselect`: <https://hub.docker.com/r/victoriametrics/vmselect/tags>
  - `vmstorage`: <https://hub.docker.com/r/victoriametrics/vmstorage/tags>

Hướng dẫn chi tiết việc triển khai với Docker: <https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/deployment/docker/README.md>

## Cluster setup

Bắt buộc phải có 3 thành phần

- `vmstorage` bắt buộc chứa 2 cờ [-retentionPeriod](https://github.com/VictoriaMetrics/VictoriaMetrics#retention) (thời gian lưu trữ tối đa, Lưu giữ mặc định là 1 tháng) and `-storageDataPath` (nơi lưu trữ, thường là ngay tại nơi cài đặt vmstorage)
- `vminsert` bắt buộc có cờ `-storageNode=<link_to_vmstorage_host>`
- `vmselect` bắt buộc có cờ `-storageNode=<link_to_vmstorage_host>`

Nên triển khai trên ít nhất 2 nút, để đảm bảo tính sẵn sàng cho cụm. Có thể tuỳ thuộc vào thông số phần cứng mà cài đặt các thành phần của cụm.

Nên chạy nhiều nút `vmstorage` hơn là chạy một vài nút, chia nhỏ được công việc storage ra càng nhiều thì khi thực hiện tính chất dự phòng càng đảm bảo hơn. Có thể hiểu là khi bất kỳ một nút nào không hoạt động thì nhiều nút `vmstorage` sẽ đảm nhiệm tốt và nhanh hơn công việc của nút hỏng, mà không gây ảnh hưởng quá nhiều đến hiệu suất. Còn khi chỉ có một vài nút đảm nhiệm `vmstorage` thì công việc phải tiếp quản sẽ rất nhiều, gây ảnh hưởng đến hiệu suất và tính sẵn sàng của cụm.

Các công cụ http load balancer như [vmauth](https://docs.victoriametrics.com/vmauth.html) hay `nginx` cần được cài đặt phía trước các nút chứa `vminsert` and `vmselect` để có thể định hướng các request.

- Các request bắt đầu bằng `/insert` phải được định tuyến đến cổng `8480` trên các nút chứa `vminsert`.
- Các request bắt đầu bằng `/select` phải được định tuyến đến cổng `8481` trên các nút chứa `vmselect`.

>Đây là các cổng mặc định, có thể thay đổi được với cờ `-httpListenAddr=<port_number>` trên các nút tương ứng.

- Có thể triển khai cluster trên một nút duy nhất, nhưng không khuyến khích. Nên sử dụng nhánh single-node khi chỉ có một nút duy nhất

## Automatic vmstorage discovery

Một tính năng được giới thiệu trong bản [enterprise](https://docs.victoriametrics.com/enterprise.html). Hỗ trợ 2 cách để tự phát hiện các nút `vmstorage`

- file-based discovery -  đặt danh sách các nút `vmstorage` vào một tệp - một địa chỉ nút trên một dòng. Rồi trên các nút `vminsert` and `vmselect` thực hiện đọc file và quét với cờ `-storageNode=file:/path/to/file-with-vmstorage-list`, hoặc có thể đọc file trên một host khác thông qua HTTP hay HTTPS với dạng `http://some-host/vmstorage-list`. Kết hợp với cờ, sẽ tương tự như `-storageNode=file:http://some-host/vmstorage-list`. Sự thay đổi trong file có thể được phát hiện sau một khoảng thời gian nhất định. Khoảng thời gian đó có thể được thay đổi với cờ `-storageNode.discoveryInterval`.
- [dns+srv](https://en.wikipedia.org/wiki/SRV_record) cũng là một giá trị trong cờ `-storageNode`. Với chức nằng của `dns+srv` là cung cấp tên của máy chủ `vmstorage` rồi các máy `vminsert` và `vmselect` sẽ phân giải thành địa chỉ tcp, với cấu trúc là `dns+srv:<tên_vmstorage>`. Sau khi phát hiện, nếu có bất kỳ thay đổi nào ở tên thì nó sẽ được cập nhật sau một khoảng thời gian. Khoảng thời gian đó có thể được cấu hình bởi `-storageNode.discoveryInterval`. VD: `-storageNode='dns+srv:vmstorage-hot'` ở đây tên là: vmstorage-hot

Có thể kết hợp cả 2 cách trong một lần khám phá. Trong trường hợp này, tất cả các tên này được phân giải thành địa chỉ tcp của các nút `vmstorage` để kết nối:

```sh
-storageNode=file:/path/to/local-vmstorage-list -storageNode='dns+srv:vmstorage-hot' -storageNode='dns+srv:vmstorage-cold'.
```

Các địa chỉ được phát hiện có thể được lọc bằng `-storageNode.filter` cờ này có thể lọc theo tuỳ ý. VD:

```sh
-storageNode.filter='^[^:]+:8400$'
```

sẽ chỉ để lại các địa chỉ được phát hiện kết thúc bằng port 8400. Đây là port mặc định để gửi dữ liệu từ `vminsert` sang `vmstorage`. Có thể thay đổi bằng `-vminsertAddr`

Các nút được phát hiện có thể được theo dõi ([monitored](https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html#monitoring)) với 2 metrics: `vm_rpc_vmstorage_is_reachable` and `vm_rpc_vmstorage_is_read_only`

## Security

Khuyến nghị bảo mật chung:

- Tất cả các thành phần của cụm phải được chạy trong mạng bảo mật riêng (private network) mà không cần phải truy cập trực tiếp vào môi trường internet.
- Các máy khách bên ngoài muốn truy cập `vminsert` và `vmselect` phải thông qua proxy xác thực như [vmauth](https://docs.victoriametrics.com/vmauth.html) hoặc [vmgateway](https://docs.victoriametrics.com/vmgateway.html)
- Các proxy xác thực chỉ chấp nhận các mã xác thực (token) từ các mạng không đáng tin cậy (vd internet) khi được gửi qua giao thức HTTPS.
- Sử dụng các token riêng biệt cho từng [tenant](https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html#multitenancy)
- Ưu tiên sử dụng các [endpoint API](https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html#url-format) đáng tin cậy và được phép, vd như Prometheus hay Grafana. KHÔNG cho phép các endpoint không đáng tin được phép truy cập vào `vminsert` và `vmselect` trước khi cấu hình các proxy xác thực.

## Bảo mật mTLS (mutual Transport Layer Security)

Mặc định, các nút `vminsert` và `vmselect` sử dụng các kết nối không được mã hóa tới `vmstorage`, vì tin tưởng chúng được triển khai trong môi trường an toàn. Phiên bản enterprise cung cấp chế độ bảo mật mTLS cho cụm VictoriaMetrics.

>TLS là một giao thức bảo mật được sử dụng để bảo vệ dữ liệu truyền tải qua mạng. TLS hoạt động bằng cách sử dụng các thuật toán mã hóa đối xứng và mã hóa bất đối xứng để đảm bảo dữ liệu được an toàn khi truyền tải giữa các thiết bị. mTLS là mã hoá bảo mật ở cả 2 đầu nhận và gửi.

Xem chi tiết về bảo mật mTLS tại đây: <https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html#mtls-protection>

## Giám sát cụm

Tất cả các thành phần cụm hiển thị các chỉ số khác nhau ở định dạng tương thích với Prometheus tại `/metrics` trên cổng TCP được đặt trong cờ `-httpListenAddr`. Các giá trị mặc định là:

- vminsert - 8480
- vmselect - 8481
- vmstorage - 8482

Để lấy dữ liệu giám sát cụm ta nên cài đặt [vmagent](https://docs.victoriametrics.com/vmagent.html) hoặc Prometheus để quét các `/metrics` từ các thành phần của cụm

Để đọc và phân tích các dữ liệu thu được ta nên sử dụng [the official Grafana dashboard for VictoriaMetrics cluster](https://grafana.com/grafana/dashboards/11176-victoriametrics-cluster/) hoặc phiên bản khác [an alternative dashboard for VictoriaMetrics cluster](https://grafana.com/grafana/dashboards/11831)

Cũng nên sử dụng [vmalert](https://docs.victoriametrics.com/vmalert.html) hoặc tính năng tương tự của Prometheus để cảnh cáo về tình trạng cụm.

Xem tài liệu chi tiết về giám sát cụm: <https://victoriametrics.com/blog/victoriametrics-monitoring/?_gl=1*1bdzgd8*_ga*MTkzOTI2MzMyMy4xNjg1NTkzODYw*_ga_N9SVT8S3HK*MTY4NjAyNTI3My4yMi4xLjE2ODYwMjU5MjYuMC4wLjA.>



## Tài liệu tham khảo

<https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html>

<https://github.com/VictoriaMetrics/VictoriaMetrics>

<https://chungphan.com/2020-08-18-victoriametric.html>

