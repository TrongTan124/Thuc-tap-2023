## Systemd
-systemd là trình quản lý hệ thống và dịch vụ cho hệ điều hành linux. systemd có thể được sử dụng để kiểm soát và quản lý các dịch vụ và unitfile, chẳng hạn như sử dụng lệnh systemctl.
- service: nhóm các routine để điều khiển một thiết bị phần cứng trả về thông tin của hệ thống hiện tại, thường chạy ở chế độ background
- systemd giúp cho việc quản lý các service, ví dụ khởi động, dừng hoặc kiểm tra trạng thái service, và quản lý unit file
## Unit file:
- systemd quản lý các service bằng unit file, đây là các đối tượng được systemd dùng để quản lý service
- unit file có file extension dựa trên 12 loại unit file như sau:
1. service( quản lý hoạt động của các chương trình)
2. socket( quản lý kết nối)
3. device(quản lý thiết bị)
4. mount(gắn thiết bị)
5. automount(tự động gắn thiết bị)
6. swap(quản lý vùng không gian bộ nhớ trên đĩa cứng)
7. target(quản lý tạo liên kết)
8. path( quản lý đường dẫn)
9. timer(dùng cho cron-job để quản lý scheduling(Cron là hệ thống giúp linux user thực hiện scheduling)
10. snapshot( sao lưu)
11. slice( quản lý tiến trình)
12. scope( quy định không gian hoạt động của service)
## lệnh tương tác:
 1. khởi động service
 ```
 systemctl start application.service
 ```
 2. dừng service:
 ```
 systemctl stop application.service
 ```
 3. khởi động lại service:
 ```
 systemctl restart application.service
 ```
 4. reload service
 ```
 systemctl reload application.service
 ```
 Theo mặc định, một số unit file của systemd không được bật luôn khi khởi động. Người dùng có thể bật hoặc tắt các file này như sau:
 5. enable service:
 ```
 systemctl enable application.service
 ```
 6. disable service:
 ```
 systemctl disable application.service
 ```
 Người dùng có thể kiểm tra trạng thái của các unit file bằng những lệnh sau:
 7. kiểm tra trạng thái:
 ```
 systemctl status application.service
 ```
 8. hiển thị các unit đang hoạt động:
 ```
 systemctl list-units
 ```
 9. hiển thị các unit file, bao gồm unit file không hoạt động:
 ```
 systemctl list-unit-files
 ```
 10. edit service files
 ```
 systemctl edit application.service
 ```
## Nguồn tham khảo
1. [Nguồn 1](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)
2.  [Nguồn 2](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/assembly_working-with-systemd-unit-files_configuring-basic-system-settings)
