# CÁC THAO TÁC SỬ DỤNG GLANCE

##	***Mục lục***


[1.	Sử dụng glance command line	](#1)

- [1.1.	List image](#1.1)

- [1.2.	Tạo image mới](#1.2)

- [1.3.	Show image](#1.3)

- [1.4.	Upload image](#1.4)

- [1.5.	Thiết lập trạng thái của image](#1.5)

- [1.6.	Xóa image](#1.6)

- [1.7.	Tổng kết](#1.7)

[2.	Sử dụng Openstack client](#2)

- [2.1.	List image](#2.1)

- [2.2. Tạo image mới](#2.2)

- [2.3.	Show thông tin image](#2.3)

- [2.4.	Thiết lập cho image](#2.4)

- [2.5.	Xóa image](#2.5)

- [2.6.	Tổng kết](#2.6)

[3. Tham khảo](#4)

---

<a name = "1"></a>
# 1. Sử dụng glance command line

<a name = "1.1"></a>
## 1.1.	List image

Sử dụng để list các image mà user được phép truy cập.

- Ví dụ:

  `$ glance image-list`

  ![img](../images/2.1.png)

<a name = "1.2"></a>
## 1.2.	Tạo image mới

-	Cú pháp:

	```
	usage: glance image-create [--architecture <ARCHITECTURE>]
                           [--protected [True|False]] [--name <NAME>]
                           [--instance-uuid <INSTANCE_UUID>]
                           [--min-disk <MIN_DISK>] [--visibility <VISIBILITY>]
                           [--kernel-id <KERNEL_ID>]
                           [--tags <TAGS> [<TAGS> ...]]
                           [--os-version <OS_VERSION>]
                           [--disk-format <DISK_FORMAT>]
                           [--os-distro <OS_DISTRO>] [--id <ID>]
                           [--owner <OWNER>] [--ramdisk-id <RAMDISK_ID>]
                           [--min-ram <MIN_RAM>]
                           [--container-format <CONTAINER_FORMAT>]
                           [--property <key=value>] [--file <FILE>]
                           [--progress]
	```

-	Ví dụ: 

	`$ glance image-create --disk-format qcow2 --container-format bare --file cirros-0.3.5-x86_64-disk.img --name cirros-glance`

	![img](../images/2.2.png)

<a name = "1.3"></a>
## 1.3.	Show image

Xem thông tin image:

-	Cú pháp:

	`usage: glance image-show [--human-readable] [--max-column-width <integer>] <IMAGE_ID>`

-	Ví dụ: show thông tin image vừa tạo: có id như hình trên là: `e0a2e920-ca23-40ee-9fa7-5e7a1da86951`

	`$ glance image-show e0a2e920-ca23-40ee-9fa7-5e7a1da86951`

	![img](../images/2.3.png)

<a name = "1.4"></a>
## 1.4.	Upload image

Sử dụng để upload dữ liệu vào một image đã tạo trước đó. 

-	Cú pháp:

	`glance image-upload [--file <FILE>] [--size <IMAGE_SIZE>] [--progress]  <IMAGE_ID>`

-	Ví dụ: Tạo ra một image rỗng chưa có dữ liệu gì và upload data từ một image cirros có sẵn: 

	![img](../images/2.4.png)

	*(Lưu ý: file cirros-0.3.6-x86_64-disk.img đang có trong thư mục hiện tại đang thao tác)*

<a name = "1.5"></a>
## 1.5.	Thiết lập trạng thái của image

-	Đưa một image về trạng thái **deactive**: 

	`$ glance image-deactivate <IMAGE_ID>`

	ví dụ:

	![img](../images/2.5.png)

-	Đưa image từ trạng thái deactive về trạng thái active trở lại: 

	` $ glance image-reactivate <IMAGE_ID>`

	Ví dụ: 

	![img](../images/2.6.png)

<a name = "1.6"></a>
## 1.6.	Xóa image
- Cú pháp: 

	`$ glance image-delete <IMAGE_ID> [<IMAGE_ID> ...]`

- Ví dụ: Xóa image **cirros-glance** vừa tạo:

	![img](../images/2.7.png)

<a name = "1.7"></a>
## 1.7.	Tổng kết: 

\-	Là câu lệnh tương tác với glance từ những ngày ban đầu.

\-	Còn nhiều hạn chế so với bộ câu lệnh tương tác của Openstack client. 

\-	Các tùy chọn còn lại tham khảo thêm tại: https://docs.openstack.org/cli-reference/glance.html 

<a name = "2"></a>
# 2.	Sử dụng Openstack client

<a name = "2.1"></a>
## 2.1.	List image

`$ openstack image list`

![img](../images/2.8.png)

<a name = "2.2"></a>
## 2.2.	Tạo image mới

`$ openstack image create --disk-format qcow2 --container-format bare --name cirros-glance`

![img](../images/2.9.png)

***(Lưu ý: do image này chưa có dữ liệu nên đang ở trạng thái là queued)***

<a name = "2.3"></a>
## 2.3.	Show thông tin image

`$ openstack image show <image_name> `

![img](../images/2.10.png)

<a name = "2.4"></a>
## 2.4.	Thiết lập cho image
Sử dụng câu lệnh `openstack image set` để thiết lập các thông số cho image:

-	Thiết lập trạng thái deactive cho image **image-glance** :

	![img](../images/2.11.png)

-	Thiết lập cho image trên active trở lại: 

	![img](../images/2.12.png)

-	Thiết lập cho image image-glance ở chế độ public: 

	![img](../images/2.13.png)

<a name = "2.5"></a>
## 2.5.	Xóa image

Để xóa image sử dụng câu lệnh sau:

`$ openstack image delete <image_name>`

Ví dụ:

![img](../images/2.14.png)

<a name = "2.6"></a>
## 2.6.	Tổng kết

\- Câu lệnh `openstack client` có nhiều ưu điểm hơn câu lệnh `glance`. Hỗ trợ sử dụng tên của image thay vì id nếu tên đó là duy nhất. 

\- Mapping giữa câu lệnh glance và openstack client: 

![img](../images/2.15.png)

\-	Tham khảo thêm về câu lệnh openstack client cho glance tại: https://docs.openstack.org/developer/python-openstackclient/command-objects/image.html




<a name = "3"></a>
# 3. Tham khảo

[1] glance cli: https://docs.openstack.org/cli-reference/glance.html

[2] openstack client image: https://docs.openstack.org/developer/python-openstackclient/command-objects/image.html

Gửi request tới Glance API: 

[3] https://docs.openstack.org/developer/glance/glanceapi.html 

[4] https://github.com/thaihust/Thuc-tap-thang-03-2016/blob/master/ThaiPH/OpenStack/Glance/ThaiPH_baocaotimhieuglance.md#cURL

[5] https://developer.openstack.org/api-ref/image/v2/index.html





