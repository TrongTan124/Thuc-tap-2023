## Nội dung chính

- Cái nhìn khái quát về VictoriaMetrics
- Các thành phần chính
- Các cách cài đặt cơ bản

>Lưu ý: các công cụ khác được nhắc đến trong bài viết cũng là công cụ tương tự như VictoriaMetrics

[Giới thiệu chung](#giới-thiệu-chung)

[Các thành phần](#các-thành-phần)

- [vmui](#vmui)
- [vmagent](#vmagent)
- [vmalert](#vmalert)
- [vmauth](#vmauth)
- [vmbackup](#vmbackup)
- [vmrestore](#vmrestore)
- [vmctl](#vmctl)
- [vmgateway](#vmgateway)
- [vmbackupmanager](#vmbackupmanager)
- [vmanomaly](#vmanomaly)

___

## Giới thiệu chung

- Phát triển và phát hành từ những năm 2019, VictoriaMetrics là một giải pháp giám sát và lưu trữ dữ liệu theo thời gian (Time series database) mã nguồn mở, có hiệu năng cao, khả năng mở rộng, lưu trữ phân tán,...

- Dữ liệu chuỗi thời gian (Time-Series Data) là một chuỗi các điểm dữ liệu được thực hiện từ cùng một nguồn trong một khoảng thời gian nhất định. Các điểm dữ liệu này thường được đóng dấu thời gian (time-stamped data) và bao gồm các phép đo liên tiếp được thực hiện từ cùng một nguồn trong một khoảng thời gian nhất định. Dữ liệu chuỗi thời gian thường được sử dụng để phân tích xu hướng và dự đoán trong nhiều lĩnh vực, bao gồm kinh tế học, tài chính, khoa học dữ liệu và sản xuất. Các cơ sở dữ liệu chuỗi thời gian (Time Series Database) được sử dụng để lưu trữ và quản lý dữ liệu chuỗi thời gian, và đôi khi được sử dụng để phân tích dữ liệu chuỗi thời gian.

- Metrics là một tập hợp các số liệu cung cấp thông tin về một quá trình hoặc hoạt động cụ thể. Metrics được sử dụng để đo lường và theo dõi các chỉ số quan trọng trong các lĩnh vực khác nhau, bao gồm kinh doanh, tiếp thị, khoa học dữ liệu,...VD: tỉ lệ đăng ký mua một sản phẩm nào đó, tốc độ tải của một web-site, số lượng người truy cập và hệ thống trong một khoảng thời gian,...

>có thể xem thêm về time series database tại bài viết này: <https://viblo.asia/p/tan-man-mot-chut-ve-time-series-data-p1-1VgZv6DpZAw>

- Kết hợp tốt với các trình giám sát khác như Prometheus, Grafana,...
- Chuyển đổi, ghi chép dữ liệu linh hoạt với cả các trình lưu dữ liệu theo thời gian khác như: InfluxDB và TimescaleDB tới 20 lần.
- Trang github của VictoriaMetrics: <https://github.com/VictoriaMetrics/VictoriaMetrics>
- Trang docs: <https://docs.victoriametrics.com/>

### Tính năng nổi bật

- Là một phương án tốt để thay thế cho Prometheus: lưu trữ dữ liệu, kết hợp với Grafana,...
- Yêu cầu phần cứng đơn giản hơn so với trình Graphite
- Dễ dàng triển khai, cấu hình, vận hành với dòng lệnh đơn giản
- Dữ liệu sẽ được lưu trong một thư mục duy nhất và được trỏ đến bởi: `-storageDataPath`
- Dế dàng sao lưu, phục hồi với các công cụ có sẵn: vmbackup / vmrestore
- Ngôn ngữ truy vấn MetricsQL mới nhưng vẫn tương thích ngược với PromQL đã phổ biến
- Các công cụ khác có thể ghi dữ liệu (hay nhập dữ liệu) vào VictoriaMetrics. Rồi các dữ liệu này có thể được truy vẫn thông qua một câu lệnh duy nhất.
- Nó cung cấp hiệu suất cao và khả năng mở rộng theo chiều dọc và chiều ngang tốt cho cả việc nhập dữ liệu và truy vấn dữ liệu . Nó vượt trội hơn InfluxDB và TimescaleDB tới 20 lần.
- Hiệu suất cao hơn dù với cùng một cấu hình phần cứng khi phải xử lý một lượng lớn dữ liệu so với: InfluxDB, Prometheus, Thanos hoặc Cortex
- Cung cấp khả năng nén dữ liệu cao, nên có thể lưu trũ nhiều hơn.
- Nó có thể lưu trữ dữ liệu trên các kho lưu trữ dựa trên NFS như Amazon EFS và Google Filestore.
- Được tối ưu hoá để lưu trữ trên các kho lưu trữ trên mạng như: ổ cứng và lưu trữ mạng trong AWS, Google Cloud, Microsoft Azure, v.v.
- Hỗ trợ dán nhãn lại dữ liệu (metrics) thu thập được
- Phân biệt rõ ràng giữa 2 hình thức triển khai là 1 node hay một cụm (cluster version)
- VictoriaMetrics cho kết quả hoạt động tốt nhất khi được triển khai trên các môi trường rộng lớn như các cụm công nghiệp, theo dõi dữ liệu tài chính và các hoạt động của doanh nghiệp trên môi trường số, các cụm Kubernetes,...

## Các thành phần

_Đây là các thành phần nền, cơ bản trong VictoriaMetrics, trên phiên bản single-node và cluster có thể có sự khác nhau._

### vmui

VictoriaMetrics cung cấp giao diện người dùng để khám phá (Explore) và khắc phục sự cố truy vấn. Giao diện người dùng có sẵn tại `http://<victoriametrics>:8428/vmui`. Giao diện người dùng cho phép xem kết quả truy vấn thông qua biểu đồ và bảng. Nó cũng cung cấp các tính năng sau:

- Explore:
  - Metrics explorer - tự động tạo biểu đồ cho các chỉ số đã chọn;
  - Cardinality explorer - số liệu thống kê về các số liệu hiện có trong TSDB;
  - Top queries - hiển thị các truy vấn được thực hiện thường xuyên nhất;

- Tools:
  - Trace analyzer (bộ phân tích dấu vết) - để tải các dấu vết truy vấn ở định dạng JSON;
  - Bộ kiểm tra biểu thức WITH  - kiểm tra cách thức hoạt động của biểu thức WITH trong bộ truy vấn MetricsQL;
  - Trình gỡ lỗi dán nhãn lại số liệu (Metric relabel debugger ) - để gắn nhãn lại các cấu hình.

- Có thể thu phóng các biểu đồ, thay đổi thời gian truy vấn,...
- Xem chi tiết hơn tại đây: <https://docs.victoriametrics.com/#vmui>

### vmagent

Một công cụ cần thiết để lấy dữ liệu, gán lại nhãn, lọc các chỉ số từ nhiều nguồn khác nhau rồi gửi chúng về lưu trữ lại VictoriaMetrics hay bất kỳ hệ thống tương tự nào khác thông qua giao thức `remote_write` của Prometheus.

Mặc dù bản thân VictoriaMetrics cũng có thể tự thu tập và lưu trữ các Metrics, nhưng các hệ thống có thể khác nhau nên người dùng cần thứ gì đó nhanh gọn để trích xuất các dữ liệu sẵn có hay thu thập chúng từ các hệ thống khác tương thích với Prometheus. vmagent có tính linh hoạt cao khi chấp nhận các giao thức gửi dữ liệu phổ biết như: tcp, udp, http,...Ngoài ra nó còn có thể quét và tìm các mục tiêu có tương thích với Prometheus.

- Các tính năng

  - Có thể được sử dụng như một sự thay thế drop-in cho Prometheus để khám phá và thu thập dữ liệu (scraping) từ các mục tiêu là [node_exporter](https://github.com/prometheus/node_exporter).
  >Lưu ý rằng VictoriaMetrics nút đơn cũng có thể khám phá và thu thập dữ liệu (scraping) từ các mục tiêu tương thích với Prometheus theo cùng một cách hoạt động.
  - Chấp nhận thu thập data thông qua tất cả các phương thức mà VictoriaMetrics hỗ trợ, vd: http, https,... Tài liệu chính thức về các phương thức mà VictoriaMetrics hỗ trợ: <https://docs.victoriametrics.com/vmagent.html#how-to-push-data-to-vmagent>
  - Có thể thêm, xóa và sửa đổi nhãn - labels (aka tags - còn gọi là thẻ) thông qua việc dán nhãn lại của Prometheus. Có thể lọc dữ liệu trước khi gửi đến bộ lưu trữ từ xa. Xem [tài liệu](https://docs.victoriametrics.com/vmagent.html#relabeling) chính thức
  - Có thể tổng hợp các mẫu đến (incoming samples) theo thời gian và theo nhãn trước khi gửi chúng đến bộ lưu trữ từ xa
  - Có thể sao chép đồng thời các chỉ số đã thu thập sang nhiều hệ thống lưu trữ từ xa tương thích với `remote-write` của Prometheus.
  - Có thể tiết kiệm chi phí sử dụng băng thông mạng đầu ra khi giao thức ghi từ xa của VictoriaMetrics được sử dụng để gửi dữ liệu đến VictoriaMetrics.
  - Hoạt động trơn tru trong môi trường có kết nối không ổn định với bộ lưu trữ từ xa. Nếu bộ nhớ từ xa không khả dụng, các chỉ số đã thu thập sẽ được lưu vào bộ đệm ở `-remoteWrite.tmpDataPath`. Các số liệu được lưu vào bộ nhớ đệm được gửi đến bộ lưu trữ từ xa ngay sau khi kết nối với bộ lưu trữ từ xa được sửa chữa. Việc sử dụng đĩa tối đa cho bộ đệm có thể được giới hạn với `-remoteWrite.maxDiskUsagePerURL`.
  - Sử dụng lượng RAM, CPU, đĩa IO và băng thông mạng thấp hơn so với Prometheus.
  - Có thể đọc/ghi dữ liệu từ Kafka.
  - v.v

Chi tiết hơn tại: <https://docs.victoriametrics.com/vmagent.html>

### vmalert

Vmalert thực thi một danh sách các quy tắc cảnh báo ([alerting](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)) hoặc ghi chú ([recording](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/)) được cấu hình trên `-datasource.url` tương thích với giao diện HTTP API của Prometheus. Để gửi thông báo cảnh báo, vmalert phụ thuộc vào [Alertmanager](https://github.com/prometheus/alertmanager) được cấu hình thông qua cờ `-notifier.url`. Kết quả của các quy tắc ghi chú được lưu trữ thông qua giao thức ghi từ xa [remote write](https://prometheus.io/docs/prometheus/latest/storage/#remote-storage-integrations) và yêu cầu cấu hình với cờ `-remoteWrite.url`. Vmalert được lấy cảm hứng rất nhiều từ việc triển khai [Prometheus](https://prometheus.io/docs/alerting/latest/overview/) và mục tiêu của nó là tương thích với cú pháp của Prometheus. Vì thế nếu đã từng làm với Prometheus thì rất dễ.

Phiên bản một nút ([single-node](https://docs.victoriametrics.com/Single-server-VictoriaMetrics.html#vmalert)) hoặc cụm ([cluster version](https://docs.victoriametrics.com/Cluster-VictoriaMetrics.html#vmalert)) của VictoriaMetrics có khả năng ủy quyền các yêu cầu tới vmalert thông qua cờ dòng lệnh `-vmalert.proxyURL`. Sử dụng tính năng này cho các trường hợp sau:

- Các yêu cầu đến từ  [Grafana Alerting UI](https://grafana.com/docs/grafana/latest/alerting/);
- để truy cập giao diện người dùng vmalerts thông qua VictoriaMetrics Web

Vì được lấy gần như toàn bộ từ Prometheus sang, nên các tính năng cơ bản như:

- Tương thích hoàn toàn với VictoriaMetrics;
- Hỗ trợ truy vấn từ MetricsQL;
- Hỗ trợ cấu hình với format cấu hình alert của Prometheus;
- Tương thích hoàn toàn với công cụ [Alertmanager](https://github.com/prometheus/alertmanager) từ phiên bản [v0.16.0-alpha;](https://github.com/prometheus/alertmanager/releases/tag/v0.16.0-alpha.0)
- Tải lên các quy tắc ghi và cảnh báo từ hệ thống tệp cục bộ, URL, GCS và S3...
- Phát hiện các quy tắc cảnh báo mà nó không khớp với bất kỳ chuỗi nào.

Các hạn chế nổi cộm:

- Cảnh báo chủ yếu được truyền thông qua mạng, nên sẽ bị ảnh hưởng khi mạng có vấn đề. Đặc biệt là với các cụm
- Theo mặc định, khi thực hiện cảnh báo theo nhóm, hay một danh sách có liên kết. Thì khi triển khai trong một cụm thì rất dễ gặp trường hợp bất đồng bộ giữa các kết quả thu được. Gây ra cảnh báo cuối cùng nhận được bị sai.

Chi tiết hơn tại: <https://docs.victoriametrics.com/vmalert.html>

### vmauth

Vmauth là một proxy xác thực đơn giản, trình định tuyến và cân bằng tải ([load balancing](https://docs.victoriametrics.com/vmauth.html#load-balancing)) cho VictoriaMetrics. Nó đọc thông tin xác thực từ tiêu đề http Authorization (hỗ trợ Basic Auth, Bearer token và InfluxDB authorization), so khớp chúng với các cấu hình được chỉ định bởi cờ [-auth.config](https://docs.victoriametrics.com/vmauth.html#auth-config) và chuyển tiếp các yêu cầu HTTP đến `url_prefix` được cấu hình cho từng người dùng khi đã khớp về mặt xác thực (on successful match). Cờ `-auth.config` có thể trỏ đến tệp cục bộ hoặc đến url http.

Ví dụ về cú pháp của cờ `-auth.config`

```sh
-auth.config=/path/to/auth/config.yml
```

- Một số cách xác thực phổ biến như: thông qua token, IP, username-password,...Có thể dùng riêng từng cách hoặc dùng kết hợp đều được.

Chi tiết hơn tại: <https://docs.victoriametrics.com/vmauth.html>

### vmbackup

Khởi tạo dữ liệu sao lưu cho VictoriaMetrics từ việc tạo các snapshots ([instant snapshots.](https://docs.victoriametrics.com/Single-server-VictoriaMetrics.html#how-to-work-with-snapshots)).

vmbackup hỗ trợ sao lưu tăng dần (Incremental) và đầy đủ. Sao lưu tăng dần được tạo tự động nếu đường dẫn đích đã chứa dữ liệu từ bản sao lưu trước đó. Sao lưu đầy đủ có thể được tăng tốc bằng cách sử dụng cờ `-origin` trỏ đến một bản sao lưu đã tồn tại trên một bộ lưu trữ từ xa (backups with server-side copy from existing backup). Trong trường hợp này, vmbackup tạo bản sao giữa các máy chủ cho, sao chép dữ liệu giữa bản sao lưu hiện tại và bản sao lưu mới. Nó tiết kiệm thời gian và chi phí truyền dữ liệu.

Có thể dừng giữa chừng và tiếp tục sao lưu dữ liệu trở lại ngay tại vị trí dừng trước đó.

Bảo sao lưu có thể dùng [vmrestore](https://docs.victoriametrics.com/vmrestore.html) để khôi phục.

Công cụ hỗ trợ tạo sao lưu tự động theo giờ, ngày, tuần, tháng [vmbackupmanager](https://docs.victoriametrics.com/vmbackupmanager.html)

Có thể lưu trữ bản sao lưu tại:

- Trên máy local, với cờ `-dst=fs://</absolute/path/to/backup>`

>Lưu ý rằng vmbackup ngăn không cho lưu trữ bản sao lưu vào thư mục được trỏ bởi cờ `-storageDataPath`, vì thư mục này chỉ nên được quản lý bởi `vmstorage`.

- Bất kỳ dạng lưu trữ nào tương thích với S3. vd: ceph, swift...
- Lưu trữ trên Azure Blob Storage, hay GCS...

VD: câu lệnh cơ bản để tạo backup đầy đủ

```sh
./vmbackup -storageDataPath=</path/to/victoria-metrics-data> -snapshot.createURL=http://localhost:8428/snapshot/create -dst=gs://<bucket>/<path/to/new/backup>
```

Trong đó:

- `</path/to/victoria-metrics-data>`: đường dẫn đến nơi lưu trữ data của VictoriaMetrics. Đối với một nút thì nó được chỉ định bởi cờ `-storageDataPath`; đối với một cụm, thì nó là đường dẫn đến `vmstorage`. Không cần phải dừng hoạt động của VictoriaMetrics để tạo backup.
- `http://<victoriametrics>:8428/snapshot/create`: khai báo khởi tạo một bản backup bằng cách snapshot ngay tức thì, bản snapshot sẽ được lưu vào `<-storageDataPath>/snapshots`. Sau đó dựa vào bản snapshot để tạo ra bản backup, sau khi hoàn thành thì bản snapshot sẽ bị xoá bỏ. Xem chi tiết cơ chế tại đây: <https://docs.victoriametrics.com/Single-server-VictoriaMetrics.html#how-to-work-with-snapshots>
- `-dst`: nơi sẽ lưu trữ bản backup
- `gs://<bucket>/<path/to/new/backup>`: lưu trữ trên GCS (Google Cloud Storage), với `bucket` là tên một kho lưu trữ đã tồn tại; `<path/to/new/backup>` là đường dẫn đến thư mục sẽ lưu trữ bản backup.

VD: backups with server-side copy from existing backup

```sh
./vmbackup -storageDataPath=</path/to/victoria-metrics-data> -snapshot.createURL=http://localhost:8428/snapshot/create -dst=gs://<bucket>/<path/to/new/backup> -origin=gs://<bucket>/<path/to/existing/backup>
```

trong đó:

- cờ `-origin` chỉ đến nơi đã lưu trữ một bản backup trước đó.


VD: Tạo backup gia tăng

```sh
./vmbackup -storageDataPath=</path/to/victoria-metrics-data> -snapshot.createURL=http://localhost:8428/snapshot/create -dst=gs://<bucket>/<path/to/existing/backup>
```

- Khi sử dụng cờ `-dst` để chỉ đến một bản backup đã có sẵn thì VictoriaMetrics sẽ tự hiểu và sử dụng backup gia tăng (Incremental backups). Lúc này chỉ những dữ liệu mới sẽ được tải lên và tiếp tục ghi vào thư mục lưu trữ đã có từ trước.

**Smart backup**: lưu trữ một bản backup cho một ngày vào thư mục có định dạng `YYYYMMDD`, bản backup gia tăng cho từng giờ sẽ được lưu vào thư mục `latest`.

- Câu lệnh backup cho từng giờ:

```sh
./vmbackup -storageDataPath=</path/to/victoria-metrics-data> -snapshot.createURL=http://localhost:8428/snapshot/create -dst=gs://<bucket>/latest
```

- Câu lệnh backup cho từng ngày, từng ngày nó sẽ là dạng backup - server-side copy from existing backup. Túc là gộp nhiều bản backup thành một bản duy nhất:

```sh
./vmbackup -storageDataPath=</path/to/victoria-metrics-data> -snapshot.createURL=http://localhost:8428/snapshot/create -dst=gs://<bucket>/<YYYYMMDD> -origin=gs://<bucket>/latest
```

Chi tiết hơn tại đây: <https://docs.victoriametrics.com/vmbackup.html>

### vmrestore

Khôi phục dữ liệu đã được khởi tạo bởi [vmbackup](https://docs.victoriametrics.com/vmbackup.html)

Có thể dừng việc khôi phục và khôi phục trở lại bất kỳ lúc nào với hoạt động được tiếp tục tại cùng một điểm.

VictoriaMetrics bắt buộc phải dừng mọi hoạt động trong khi thực hiện khôi phục dữ liệu bằng vmrestore.

Nếu trong quá trình khôi phục, vmrestore chiếm dụng toàn bộ băng thông mạng thì hãy đặt giới hạn cho nó với cờ `-maxBytesPerSecond`

Nếu trong quá trình khôi phục bị dừng với lỗi không xác định, hãy khởi động lại việc khôi phục với cùng một đối số ban đầu để tiếp tục hoạt động khôi phục.

Cách sử dụng cơ bản:

```sh
./vmrestore -src=<storageType>://<path/to/backup> -storageDataPath=<local/path/to/restore>
```

trong đó:

- `-src`: nơi lưu trữ bản backup mà `vmbackup` tạo ra và lưu trữ
- `-storageDataPath`: đường dẫn đến nơi cần khôi phục dữ liệu. Có thể là nơi được trỏ đến bởi cờ `-storageDataPath` hoặc không. Thường thì là một nơi khác, sau khi hoàn tất khôi phục hãy dùng cờ `-storageDataPath` để trỏ lại thư mục đó. Nếu là thư mục cũ, thì mọi thứ sẽ được xoá bỏ và thay thế bởi nội dung trong bản backup; nó tương tự như khi chạy câu lệnh [rsync –delete](https://askubuntu.com/questions/476041/how-do-i-make-rsync-delete-files-that-have-been-deleted-from-the-source-folder)

Chi tiết hơn tại: <https://docs.victoriametrics.com/vmrestore.html>

### vmctl

Công cụ dòng lệnh VictoriaMetrics (VictoriaMetrics command-line tool)

vmctl cung cấp nhiều hành động hữu ích với các thành phần VictoriaMetrics.

Để xem danh sách đầy đủ các chế độ được hỗ trợ, hãy chạy lệnh sau:

```sh
vmctl --help
```

Chủ yếu được sử dụng để chuyển dịch dữ liệu từ các nền tảng khác sang VictoriaMetrics, như: từ Prometheus sang VictoriaMetrics sử dụng snapshots API, từ Thanos, Cortex, Minir, InfluxDB, OpenTSDB sang VictoriaMetrics,...

Hay chuyển dịch từ VictoriaMetrics một nốt sang một cụm.

Xác minh các bản báo cáo được xuất từ một nốt hay một cụm VictoriaMetrics.

Chi tiết hơn tại: <https://docs.victoriametrics.com/vmctl.html>

### vmgateway

_Là một phần của gói Enterprise. Tuy nhiên vẫn khả dụng trong gói miễn phí cho cộng đồng_

Là một proxy (trung gian, được uỷ quyền nhiệm vụ là chuyển tiếp) cho VictoriaMetrics Time Series Database, cung cấp 2 tình năng chính

- Rate Limiter (giới hạn truy cập): giới hạn việc truy xuất dữ liệu trong database cho đối tượng cụ thể. Hỗ trợ cả single-node hoặc cluster
- Kiểm soát truy cập theo token (Token Access Control):
  - Hỗ trợ kiểm soát truy cập theo nhãn dán bổ sung được thêm bởi VictoriaMetrics trên cả phiên bản Single-node hay cluster.
  - Kiểm soát truy cập theo tenantID trên phiên bản Cluster (cụm)
  - Cho phép truy cập với các quyền đọc/ghi/quản trị, được tách riêng một cách rõ ràng

>Token là một chuỗi ký tự mang thông tin xác định người dùng hoặc quyền truy cập trong ứng dụng

#### Access Control (kiểm soát truy cập)

vmgateway hỗ trợ `jwt` (JSON Web Token (JWT) là một chuẩn mở được định nghĩa trong RFC 7519, được sử dụng để truyền đạt thông tin giữa các bên một cách an toàn và nhỏ gọn). Với jwt, ta có thể cấu hình truy cập đọc/ghi cho từng đối tượng cụ thể với từng nhãn dán cụ thể.

một format cơ bản của jwt:

```sh
{
  "exp": 1617304574,
  "vm_access": {
      "tenant_id": {
        "account_id": 1,
        "project_id": 5
      },
      "extra_labels": {
         "team": "dev",
         "project": "mobile"
      },
      "extra_filters": ["{env=~\"prod|dev\",team!=\"test\"}"],
      "mode": 1
  }
}
```

Trong đó:

- `exp`: đối số bắt buộc, thời gian mà một token hết hạn, được tính theo unix_timestamp (là số giây tính từ thời điểm 00:00:00 UTC ngày 1/1/1970 đến thời điểm cần tính). Tham khảo công cụ tính sau <https://www.unixtimestamp.com/>
- `vm_access`: đối số bắt buộc, các thông tin yêu cầu trong token. Format tối thiểu là: `{"vm_access": {"tenant_id": {}}`
- `tenant_id`: đối số tuỳ chọn, dành cho cluster, định hướng tới các đối tượng yêu cầu (tenant) truy cập tương ứng.

>tenant là khái niệm chỉ đối tượng sử dụng các tài nguyên trong cluster

- `extra_labels`: đối số tuỳ chọn, là một bộ lọc có các cặp key-value được sử dụng để lọc dữ liệu trong các metric được chọn hoặc được thu thập. Sử dụng nhiều bộ lọc với tuỳ chọn `and`. Khi bộ lọc được định nghĩa thì các bộ lọc mặc định sẽ bị bỏ qua.
- `extra_filters`: đối số tuỳ chọn, là [series selectors](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors) được thêm vào các câu lệnh truy vấn để lọc ra một vài giá trị. Nhiều selectors có thể thể kết hợp bởi tuỳ chọn `or`. Nếu được định nghĩa thì các giá trị mặc định ban đầu sẽ được bỏ qua.
- `mode`: tuỳ chọn, chế độ truy cập của api. Có 3 chế theo các con số: 0 - đầy đủ quyền, 1-(mặc đinh): chỉ đọc, 2: chỉ ghi.

#### Rate Limiter (giới hạn truy cập)

Giới hạn các yêu cầu đến bằng cách cấu hình trước. Hỗ trợ giới hạn việc đọc/ghi dựa trên các tenant, tức là dù cùng một database nhưng các tenant khác nhau thì bị giới hạn khác nhau.

vmgateway cần có data nguồn để có thể thực hiện giới hạn. Các metric mà bạn muốn giới hạn tốc độ bắt buộc phải được thu thập từ cluster.

Danh sách các loại giới hạn được hỗ trợ:

- `queries`: Số lần yêu cầu API được thực hiện tại tenant để đọc API, vd như `/api/v1/query`, `/api/v1/series`
- `active_series`: các chuỗi hoạt động hiện tại của bất kỳ tenant nào

><https://docs.victoriametrics.com/FAQ.html#what-is-an-active-time-series>

- `new_series`: số lượng chuỗi đã tạo; aka churn rate

>churn rate: có thể hiểu, đây là tỷ lệ của một đối tượng bị biến mất trong một khoảng thời gian rồi lại xuất hiện trở lại. Hay dịch ra nghĩa là tỷ lệ rời bỏ. Tỷ lệ rời bỏ càng cao thì khả năng biến mất của đối tượng càng lớn. Trong VictoriaMetrics thì có khái niệm sau [high churn rate](https://docs.victoriametrics.com/FAQ.html#what-is-high-churn-rate)

- `rows_inserted`: số hàng được chèn thêm trên mỗi tenant

Danh sách các dạng thời gian hỗ trợ giới hạn:

- phút - minute
- giờ - hour

Ví dụ về cấu hình

```yaml
limits:
  - type: queries
    value: 100
    resolution: minute
  - type: rows_inserted
    value: 100000
    resolution: minute
  - type: new_series
    value: 1000
  - type: active_series
    value: 1000
    resolution: hour
  - type: queries
    value: 1
    project_id: 5
    account_id: 15
```

Giới hạn có thể được chỉ định cho mỗi đối tượng tenant hoặc ở cấp độ toàn bộ nếu bạn bỏ qua `project_id` và `account_id`

#### xác minh chữ ký JWT

vmgateway hỗ trọ chũ ký JWT để chứng thực.

Các loại thuật toán hỗ trợ là: RS256, RS384, RS512, ES256, ES384, ES512, PS256, PS384, PS512. Các token không sử dụng một trong các thuật toán trên sẽ bị từ chối xác nhận.

Để bật xác thực JWT thì cần phải chỉ định các khoá, có 2 cách sau:

- `-auth.publicKeyFiles`: đường dẫn đến file chứa khoá
- `-auth.publicKeys`: nhập khoá trực tiếp

vd:

```sh
./bin/vmgateway -eula \
  -enable.auth \
  -write.url=http://localhost:8480 \
  -read.url=http://localhost:8481 \
  -auth.publicKeyFiles=public_key.pem \
  -auth.publicKeyFiles=public_key2.pem \
  -auth.publicKeys=`-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu1SU1LfVLPHCozMxH2Mo
4lgOEePzNm0tRgeLezV6ffAt0gunVTLw7onLRnrq0/IzW7yWR7QkrmBL7jTKEn5u
+qKhbwKfBstIs+bMY2Zkp18gnTxKLxoS2tFczGkPLPgizskuemMghRniWaoLcyeh
kd3qqGElvW/VDL5AaWTg0nLVkjRo9z+40RQzuVaE8AkAFmxZzow3x+VJYKdjykkJ
0iT9wCS0DRTXu269V264Vf/3jvredZiKRkgwlL9xNAwxXFg0x/XFw005UWVRIkdg
cKWTjpBP2dPwVZ4WWC+9aGVd+Gyn1o0CLelf4rEjGoXbAAEgAqeGUxrcIlbjXfbc
mwIDAQAB
-----END PUBLIC KEY-----
`
```

Lệnh trên sẽ sử dụng đến 3 khoá, trong đó 2 khoá là tệp, một khoá là nhập trực tiếp.

Xem chi tiết nhất tại: <https://docs.victoriametrics.com/vmgateway.html>

### vmbackupmanager

_Đây cũng là một phần của gói enterprise_

Đây là một công cụ hỗ trợ cho việc sao lưu trên VictoriaMetrics. Nó hỗ trợ việc lập lịch trình để sao lưu tự động cho: giờ, ngày, tuần, tháng. Ngoài ra còn hỗ trợ đa sao lưu, ví dụ như sao lưu cho từng giờ rồi tiếp tục sao lưu cho cả một ngày đó. Nó cần quyền truy cập đọc vào khu vực lưu trữ dữ liệu, vì thế tối ưu nhất nên cài cả 2 trên cùng một máy. Dịch vụ sao lưu sẽ tạo bản sao lưu rồi lưu vào một thư mục mới, sau khi sao lưu xong thì nó mới tiến hành copy vào thư mục thực sự lưu trữ các bản sao lưu.

**Các cờ bắt buộc để chạy dịch vụ**:

- `-eula`: nên là true, và nó có ý nghĩa là bạn có quyền hợp pháp để tạo bản sao lưu. Đó có thể là hợp đồng đã ký hoặc email có xác nhận chạy dịch vụ trong thời gian dùng thử.
- `-storageDataPath`: đường dẫn đến VictoriaMetrics hoặc vmstorage nơi cần tạo bản sao lưu.
- `-snapshot.createURL`: tạo đường dẫn URL cho bản snapshot, thông thường sẽ được tạo tự động. VD: `http://victoriametrics:8428/snapshot/create`
- `-dst`: Chỉ định nơi sao lưu. Nếu không lưu tại local thì có thể chỉ định nơi lưu trên internet, các loại lưu trữ hỗ trợ: <https://docs.victoriametrics.com/vmbackup.html#supported-storage-types>
- `-credsFilePath`: đường dẫn đến file chứa các thông tin đăng nhập cho GCS hoặc S3. Thông tin sẽ được lấy tại file mặc định nếu không chỉ định. Xem hướng dẫn cho GCS: <https://cloud.google.com/iam/docs/creating-managing-service-account-keys>, và S3 của AWS: <https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html>.

**Lịch sao lưu được kiểm soát bởi các cờ sau**:

- `-disableHourly` - disable hourly run. Default false
- `-disableDaily` - disable daily run. Default false
- `-disableWeekly` - disable weekly run. Default false
- `-disableMonthly` - disable monthly run. Default false

Ta có thể thấy mặc định thì dịch vụ sẽ tự chạy sao lưu theo hằng giờ, ngày, tuần, tháng.

**Hệ thống phân cấp thư mục lưu trữ cho các bản sao lưu**:

- `/latest/` - chứa bản sao lưu mới nhất
- `/hourly/` - chứa các bản sao lưu hàng giờ. Mỗi bản sao lưu được đặt tên là YYYY-MM-DD:HH
- `/daily/` - chứa các bản sao lưu hàng ngày. Mỗi bản sao lưu được đặt tên là YYYY-MM-DD
- `/weekly/` - chứa các bản sao lưu hàng tuần. Mỗi bản sao lưu được đặt tên là YYYY-WW
- `/monthly/` - chứa các bản sao lưu hàng tháng. Mỗi bản sao lưu được đặt tên là YYYY-MM

Để có danh sách đầy đủ các cờ được hỗ trợ, vui lòng chạy lệnh sau:

```sh
./vmbackupmanager --help
```

Dịch vụ tạo bản sao lưu đầy đủ mỗi lần chạy. Điều này có nghĩa là hệ thống có thể được khôi phục hoàn toàn từ bất kỳ bản sao lưu cụ thể nào bằng cách sử dụng [vmrestore](https://docs.victoriametrics.com/vmrestore.html). Quản lý sao lưu chỉ tải lên dữ liệu đã thay đổi hoặc được tạo ra kể từ bản sao lưu gần nhất (sao lưu tăng dần). Điều này giảm lưu lượng mạng tiêu thụ và thời gian cần thiết để thực hiện sao lưu.

Bài viết chi tiết về sao lưu: <https://medium.com/@valyala/speeding-up-backups-for-big-time-series-databases-533c1a927883>

>Lưu ý: khi tải bản sao lưu lên lần đầu tiên thì sẽ tốn khá nhiều băng thông và thời gian, có thể ảnh hưởng đến hiệu suất của cụm

Có 2 cờ có thể điều chỉnh hiệu suất của việc tải lên:

- `-maxBytesPerSecond` - tốc độ tải lên tối đa. Không có giới hạn nếu nó được đặt thành 0
- `-concurrency` - Số lượng công nhân đồng thời. Càng nhiều concurrency thì khả năng tải lên càng nhanh (mặc định là 10)


**Chính sách lưu trữ sao lưu**:

Chính sách lưu giữ dự phòng được kiểm soát bởi:

- `-keepLastHourly` - keep the last N hourly backups. Disabled by default
- `-keepLastDaily` - keep the last N daily backups. Disabled by default
- `-keepLastWeekly` - keep the last N weekly backups. Disabled by default
- `-keepLastMonthly` - keep the last N monthly backups. Disabled by default

>Lưu ý: Giá trị 0 trong mỗi cờ keepLast dẫn đến việc xóa TẤT CẢ các bản sao lưu cho loại cụ thể (hàng giờ, hàng ngày, hàng tuần và hàng tháng)

VD: `-keepLastDaily=3` thì cờ này sẽ cho hệ thống biết chỉ giữ lại 3 bản sao lưu theo ngày mới nhất trong danh sách, các bản cũ hơn sẽ bị xoá bỏ.

Để bảo vệ bản sao lưu không bị xoá bằng lệnh: `vmbackupmanager backups lock`

vd:

```sh
./vmbackupmanager backup lock daily/2021-02-13 -dst=<DST_PATH> -storageDataPath=/vmstorage-data -eula
```

Để loại bỏ bảo vệ, bạn có thể sử dụng lệnh: `vmbackupmanager backups unlock`

vd:

```sh
./vmbackupmanager backup unlock daily/2021-02-13 -dst=<DST_PATH> -storageDataPath=/vmstorage-data -eula
```

Xem chi tiết hơn tại: <https://docs.victoriametrics.com/vmbackupmanager.html>

### vmanomaly

_Là một phần trong bản Enterprise_

Trình phát hiện điểm bất thường trong data mà VictoriaMetrics thu thập được. Có thể theo dõi bất thường trong toàn bộ data hoặc một số đối tượng nhất định. Rồi đưa ra cảnh báo khi bất thường chạm ngưỡng đã đặt ra từ trước.

Có thể tự cấu hình bằng tay các chỉ số hoặc dựa vào các phương pháp có sẵn mà nhà phát triển cung cấp.

Để có thể thực hiện được cấu hình này thì cần phải am hiểu về data, sự bất thường trong data, nắm vững được hệ thống đang theo dõi và hệ thống VictoriaMetrics mà ta triển khai. Nên bài viết này chỉ mang tính chất giới thiệu cho công cụ này.

Để xem chi tiết nhất có thể thì truy cập hướng dẫn từ nhà phát hành:

<https://docs.victoriametrics.com/vmanomaly.html>
