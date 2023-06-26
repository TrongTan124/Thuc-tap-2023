## Nội dung chính

_Cài đặt VictoriaMetrics single-node hay Single-server_


[Chuẩn bị](#chuẩn-bị)

[Tiến hành](#tiến-hành)

- [1. Xây dựng từ mã nguồn](#1-xây-dựng-từ-mã-nguồn)
- [2. Xây dựng từ gói của nhà phát hình](#2-xây-dựng-từ-gói-của-nhà-phát-hình)
  - [Cấu hình cho VictoriaMetrics single-node](#cấu-hình-cho-victoriametrics-single-node)

- [3. Cài đặt với hỗ trợ từ Snap](#3-cài-đặt-với-hỗ-trợ-từ-snap)
- [Kết hợp](#kết-hợp)

[Tài liệu tham khảo](#tài-liệu-tham-khảo)

## Chuẩn bị

- 01 máy Ubuntu, ít nhất là phiên bản 18.04.
- Có ít nhất 01 network có kết nối với internet
- Tối thiểu RAM 2GB, ổ cứng 20GB
- Có thể thực hiện môi trường ảo hoá hoặc vật lý. Tuy nhiên ưu tiên môi trường ảo hoá.
- Thêm người dùng để quản lý VictoriaMetrics:

```sh
groupadd -r victoriametrics
useradd -g victoriametrics -d /var/lib/victoria-metrics-data -s /sbin/nologin --system victoriametrics
```

- Tạo thư mục cần thiết để VictoriaMetrics làm việc:

```sh
mkdir -p /etc/victoriametrics/single
mkdir -p /var/lib/victoria-metrics-data
```

- Trong quá trình cài đặt nếu xuất hiện lỗi và muốn kiểm tra thì hãy sử dụng câu lệnh

```sh
tail /var/log/syslog
```

hoặc

```sh
journalctl -xe
```


## Tiến hành

Về cơ bản có vài cách sau để có thể cài đặt VictoriaMetrics single-node.

- Cài từ mã nguồn: ta sẽ tự build từ mã nguồn trên github:

Trang gihub: <https://github.com/VictoriaMetrics/VictoriaMetrics>

- Tải về và sử dụng từ trang chủ các phiên bản ổn định mới nhất

Trang phân phối chính thức: <https://github.com/VictoriaMetrics/VictoriaMetrics/releases/>

- Tải về và sử dụng từ Docker

Hướng dẫn từ Docker: <https://hub.docker.com/r/victoriametrics/victoria-metrics/>

- Sử dụng chương trình `Snap` để hỗ trợ cài đặt:

Hướng dẫn sử dụng `Snap`: <https://snapcraft.io/victoriametrics>

Ngoài ra còn rất nhiều cách khác có thể sử dụng. Hãy tham khảo thêm tại đây: <https://docs.victoriametrics.com/Quick-Start.html>

### 1. Xây dựng từ mã nguồn

Gần như đây là cách khó thực hiện và dễ mắc sai lầm nhất.

Ta cần 2 thứ để thực hiện đó là: Docker engine và Mã nguồn VictoriaMetrics.

- Docker engine có thể tham khảo cách cài đặt từ hướng dẫn sau: <https://docs.docker.com/engine/install/debian/>
- Mã nguồn trên Github: <https://github.com/VictoriaMetrics/VictoriaMetrics>

`B1`: Cài đặt Docker engine theo hướng dẫn từ bài viết trên

`B2`: Tải mã nguồn về máy. Tại thư mục làm việc của mình hãy chạy câu lệnh

```sh
git clone https://github.com/VictoriaMetrics/VictoriaMetrics
```

Câu lệnh sẽ tự tạo ra một thư mục có tên `VictoriaMetrics` để lưu trữ mã nguồn.
Di chuyển vào thư mục đó

```sh
cd VictoriaMetrics/
```

Sau đó hãy thực hiện cả 2 câu lệnh sau:

```sh
apt install make -y
make victoria-metrics-prod
```

>Chú ý: quá trình make sẽ nhanh hay chậm tuỳ thuộc vào kết nối mạng và cấu hình máy của bạn.

Câu lệnh sẽ tạo ra file binary có tên là `victoria-metrics-prod` và sẽ tự chuyển file đến thư mục `/bin`

`B3`: nên di chuyển sang một thư mục khác, nơi mà mình sẽ quản lý các file binary mà mình tạo ra.

```sh
mv /bin/victoria-metrics-prod /usr/bin
```

Cấp quyền thực thi

```sh
chmod +x /usr/bin/victoria-metrics-prod
chown root:root /usr/bin/victoria-metrics-prod
```


### 2. Xây dựng từ gói của nhà phát hình

`B1`: Tải xuống từ trang phát hành chính thức

```sh
wget https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v1.91.2/victoria-metrics-linux-amd64-v1.91.2.tar.gz -O /tmp/victoria-metrics.tar.gz
```

>Đây là phiên bản mới nhất tại thời điểm viết bài, phù hợp với các máy chạy kiến trúc AMD64

- Trong các file dạng `vmutils-*.tar.gz`, file nén sẽ chứa các thành phần sau:

  - [vmagent](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/app/vmagent/README.md)
  - [vmalert](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/app/vmalert/README.md)
  - [vmauth](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/app/vmauth/README.md)
  - [vmbackup](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/app/vmbackup/README.md)
  - [vmctl](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/app/vmctl/README.md)
  - [vmrestore](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/app/vmrestore/README.md)

- Trong các file dạng `vmutils-*-enterprise.tar.gz`, sẽ chứa thêm các thành phần

  - [vmbackupmanager](https://docs.victoriametrics.com/vmbackupmanager.html)
  - [vmgateway](https://docs.victoriametrics.com/vmgateway.html)


`B2`: giải nén và di chuyển file đến đúng thư mục.


```sh
tar xvf /tmp/victoria-metrics.tar.gz -C /usr/bin
```

Cấp quyền thực thi:

```sh
chmod +x /usr/bin/victoria-metrics-prod
chown root:root /usr/bin/victoria-metrics-prod
```

### Cấu hình cho VictoriaMetrics single-node

Việc cấu hình này là bắt buộc khi sử dụng một trong hai cách trên để cài đặt VictoriaMetrics

Tạo file điều khiển cho VictoriaMetrics service:

```sh
cat <<END >/etc/systemd/system/vmsingle.service
[Unit]
Description=VictoriaMetrics is a fast, cost-effective and scalable monitoring solution and time series database.
# https://docs.victoriametrics.com
After=network.target

[Service]
Type=simple
User=victoriametrics
Group=victoriametrics
WorkingDirectory=/var/lib/victoria-metrics-data
StartLimitBurst=5
StartLimitInterval=0
Restart=on-failure
RestartSec=5
EnvironmentFile=-/etc/victoriametrics/single/victoriametrics.conf
ExecStart=/usr/bin/victoria-metrics-prod \$ARGS
ExecStop=/bin/kill -s SIGTERM \$MAINPID
ExecReload=/bin/kill -HUP \$MAINPID

# See docs https://docs.victoriametrics.com/Single-server-VictoriaMetrics.html#tuning

ProtectSystem=full
LimitNOFILE=1048576
LimitNPROC=1048576
LimitCORE=infinity
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=vmsingle

[Install]
WantedBy=multi-user.target
END
```

Tạo file cấu hình

```sh
cat <<END >/etc/victoriametrics/single/victoriametrics.conf
# See https://docs.victoriametrics.com/Single-server-VictoriaMetrics.html#list-of-command-line-flags to get more information about supported command-line flags
# 
# If you use IPv6 pleas add "-enableTCP6" to args line
ARGS="-promscrape.config=/etc/victoriametrics/single/scrape.yml -storageDataPath=/var/lib/victoria-metrics-data -retentionPeriod=12 -httpListenAddr=:8428 -graphiteListenAddr=:2003 -opentsdbListenAddr=:4242 -influxListenAddr=:8089 -enableTCP6"
END
```

Tạo file cấu hình cho hành động thu thập của VictoriaMetrics:

```sh
cat <<END >/etc/victoriametrics/single/scrape.yml
# Scrape config example
#
scrape_configs:
  - job_name: self_scrape
    scrape_interval: 10s
    static_configs:
      - targets: ['127.0.0.1:8428'] 
END
```

Thay đổi sở hữu cho file cấu hình

```sh
chown -R victoriametrics:victoriametrics /etc/victoriametrics/single
```

Mặc định trên Ubuntu sẽ có filewall. Có thể tắt đi nếu sử dụng firewall khác, không thì hãy khai báo mở port

```sh
sed -e 's|DEFAULT_FORWARD_POLICY=.*|DEFAULT_FORWARD_POLICY="ACCEPT"|g' \
    -i /etc/default/ufw

ufw allow ssh comment "SSH port"
ufw allow http comment "HTTP port"
ufw allow https comment "HTTPS port"
ufw allow 8428 comment "VictoriaMetrics Single HTTP port"
ufw allow 8089/tcp comment "TCP Influx Listen port for VictoriaMetrics"
ufw allow 8089/udp comment "UDP Influx Listen port for VictoriaMetrics"
ufw allow 2003/tcp comment "TCP Graphite Listen port for VictoriaMetrics"
ufw allow 2003/udp comment "UDP Graphite Listen port for VictoriaMetrics"
ufw allow 4242 comment "OpenTSDB Listen port for VictoriaMetrics"

ufw --force enable
```

Kiểm tra trạng thái của firewall

```sh
ufw status
```

Khởi động và kiểm tra trạng thái hoạt động của VictoriaMetrics service

```sh
systemctl enable vmsingle.service
systemctl restart vmsingle.service
systemctl daemon-reload
systemctl status vmsingle.service
```

Output có thể như sau là đã cài đặt thành công:

```sh
root@phuc:~# systemctl status vmsingle.service
● vmsingle.service - VictoriaMetrics is a fast, cost-effective and scalable monitoring solution and time series databas>
     Loaded: loaded (/etc/systemd/system/vmsingle.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2023-06-08 13:27:36 +07; 24h ago
   Main PID: 19408 (victoria-metric)
      Tasks: 8 (limit: 1591)
     Memory: 38.0M
        CPU: 3min 17.724s
     CGroup: /system.slice/vmsingle.service
             └─19408 /usr/bin/victoria-metrics-prod -promscrape.config=/etc/victoriametrics/single/scrape.yml -storageD>

Jun 08 15:27:42 phuc systemd[1]: /etc/systemd/system/vmsingle.service:23: Standard output type syslog is obsolete, auto>
Jun 08 15:27:42 phuc systemd[1]: /etc/systemd/system/vmsingle.service:24: Standard output type syslog is obsolete, auto>
Jun 08 15:27:43 phuc systemd[1]: /etc/systemd/system/vmsingle.service:23: Standard output type syslog is obsolete, auto>
Jun 08 15:27:43 phuc systemd[1]: /etc/systemd/system/vmsingle.service:24: Standard output type syslog is obsolete, auto>
Jun 09 08:21:57 phuc vmsingle[19408]: 2023-06-09T01:21:57.306Z        warn        VictoriaMetrics/app/vmselect/promql/r>
Jun 09 08:21:57 phuc vmsingle[19408]: 2023-06-09T01:21:57.334Z        info        VictoriaMetrics/app/vmselect/promql/r>
Jun 09 13:06:03 phuc vmsingle[19408]: 2023-06-09T06:06:03.283Z        warn        VictoriaMetrics/app/vmselect/promql/r>
Jun 09 13:06:03 phuc vmsingle[19408]: 2023-06-09T06:06:03.297Z        info        VictoriaMetrics/app/vmselect/promql/r>
Jun 09 13:13:09 phuc systemd[1]: /etc/systemd/system/vmsingle.service:23: Standard output type syslog is obsolete, auto>
Jun 09 13:13:09 phuc systemd[1]: /etc/systemd/system/vmsingle.service:24: Standard output type syslog is obsolete, auto>
lines 1-20/20 (END)
```

Sử dụng trình duyệt truy cập vào VMUI theo đường dẫn sau:

```sh
http://<ip-host>:8428/vmui
```

### 3. Cài đặt với hỗ trợ từ Snap

`B1`: Cài đặt Snap

```sh
sudo apt install -y snapd
```

`B2`: Kiểm tra và cài đặt

- Kiểm tra sự hiện diện của VictoriaMetrics

```sh
snap info victoriametrics
```

Output có thể:

```sh
summary: VictoriaMetrics is fast, cost-effective and scalable time-series
  database.
publisher: VictoriaMetrics (f41gh7)
store-url: https://snapcraft.io/victoriametrics
contact:   info@victoriametrics.com
license:   Apache-2.0
description: |
  * VictoriaMetrics can be used as long-term storage for Prometheus or for
....
channels:
  latest/stable:    v1.89.1 2023-03-14 (220) 9MB -
  latest/candidate: v1.89.1 2023-03-14 (220) 9MB -
  latest/beta:      v1.89.1 2023-03-14 (220) 9MB -
  latest/edge:      v1.89.1 2023-03-14 (220) 9MB -
```

- Cài đặt:

```sh
sudo snap install victoriametrics
```

>Tốc độ cài đặt tuỳ thuộc vào tốc độ mạng và cấu hình máy.


`B3`: Sau khi hoàn thành có thể kiểm tra tình trạng hoạt động của VictoriaMetrics bằng câu lệnh:

```sh
curl http://localhost:8428/metrics
```

Output tương tự như sau là thành công:

```sh
.....
flag{name="snapshotAuthKey", value="secret", is_set="false"} 1
flag{name="snapshotCreateTimeout", value="0s", is_set="false"} 1
flag{name="snapshotsMaxAge", value="0", is_set="false"} 1
flag{name="sortLabels", value="false", is_set="false"} 1
flag{name="storage.cacheSizeIndexDBDataBlocks", value="0", is_set="false"} 1
flag{name="storage.cacheSizeIndexDBIndexBlocks", value="0", is_set="false"} 1
flag{name="storage.cacheSizeIndexDBTagFilters", value="0", is_set="false"} 1
flag{name="storage.cacheSizeStorageTSID", value="0", is_set="false"} 1
flag{name="storage.maxDailySeries", value="0", is_set="false"} 1
flag{name="storage.maxHourlySeries", value="0", is_set="false"} 1
flag{name="storage.minFreeDiskSpaceBytes", value="10000000", is_set="false"} 1
flag{name="storageDataPath", value="/var/lib/victoriametrics", is_set="true"} 1
flag{name="streamAggr.config", value="", is_set="false"} 1
flag{name="streamAggr.dedupInterval", value="0s", is_set="false"} 1
flag{name="streamAggr.keepInput", value="false", is_set="false"} 1
flag{name="tls", value="false", is_set="false"} 1
flag{name="tlsCertFile", value="", is_set="false"} 1
flag{name="tlsCipherSuites", value="", is_set="false"} 1
flag{name="tlsKeyFile", value="secret", is_set="false"} 1
flag{name="tlsMinVersion", value="", is_set="false"} 1
flag{name="usePromCompatibleNaming", value="false", is_set="false"} 1
flag{name="version", value="false", is_set="false"} 1
flag{name="vmalert.proxyURL", value="", is_set="false"} 1
flag{name="vmui.customDashboardsPath", value="", is_set="false"} 1
```

## Kết hợp

VictoriaMetrics chủ yếu nghiêng về phần lưu trữ nhiều hơn. Cho nên tối ưu nhất là sử dụng kèm với một vài chương trình giám sát khác như: Prometheus, Grafana,...

Sẽ update sau....


## Tài liệu tham khảo

bash scrip: [install-victoriametrics-single-ubuntu](install-victoriametrics-single-ubuntu.sh)

<https://computingforgeeks.com/install-use-victoriametrics-time-series-database-on-ubuntu/>

<https://gist.github.com/denisgolius/8b38b4233207627e46c6f8fe4efc3487>

<https://docs.victoriametrics.com/Quick-Start.html>

<https://www.youtube.com/watch?v=6AIu6oA_Zag>

Date accessed: 09/05/2023
