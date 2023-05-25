## Systemctl
- systemd là công cụ dùng để quản lý các tính năng của hệ thống và service, và giúp quản lý hệ điều hành và trạng thái của các service, dùng command systemctl
## Cấu trúc tập tin service:
- service: 1 script được chạy trong background
- systemd quản lý các service bằng unit file, đây là các đối tượng được systemd dùng để quản lý service
có 12 loại unit file:
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
 - systemd giúp cho việc quản lý các service, ví dụ khởi động, dừng hoặc kiểm tra trạng thái service, và quản lý unit file
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
 5. enable service:
 ```
 systemctl enable application.service
 ```
 6. disable service:
 ```
 systemctl disable application.service
 ```
 7. kiểm tra trạng thái:
 ```
 systemctl status application.service
 ```
 8. hiển thị các unit đang hoạt động:
 ```
 systemctl list-units
 ```
## Nguồn tham khảo
1. [Nguồn 1](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)
2.  [Nguồn 2](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/assembly_working-with-systemd-unit-files_configuring-basic-system-settings)
