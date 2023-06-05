## Tổng quan về Linux Namespace

Linux Namespace là một tính năng quan trọng trong hệ điều hành Linux, được giới thiệu từ phiên bản kernel 2.6.24. Nó cung cấp một cơ chế cho phép chia sẻ và cô lập các tài nguyên hệ thống giữa các quá trình và ứng dụng chạy trên cùng một hệ điều hành.

### 1. Khái niệm

Khái niệm Linux Namespace được sử dụng để **tạo ra các không gian tên ảo**, trong đó **các tiến trình chạy trong mỗi không gian tên có thể nhìn thấy và tương tác với các tài nguyên và quá trình trong không gian tên của chúng mà không bị ảnh hưởng bởi các tài nguyên và quá trình nằm ngoài không gian tên đó**.


### 2. Phân loại

Linux Namespace có năm loại chính:

1. **PID Namespace**: PID Namespace cho phép mỗi không gian tên có một tập hợp PID riêng biệt. Điều này có nghĩa là mỗi không gian tên có một không gian PID độc lập, trong đó các tiến trình trong không gian tên chỉ nhìn thấy và thao tác với các PID trong không gian tên của chúng. Việc sử dụng PID Namespace giúp giữ cho các quá trình được cô lập và không xung đột với các quá trình khác chạy trên hệ thống.

2. **Network Namespace**: Network Namespace cung cấp cô lập về mạng cho các tiến trình. Mỗi không gian tên có một bộ giao diện mạng, bảng định tuyến và tường lửa riêng biệt. Điều này cho phép các tiến trình trong không gian tên tương tác với mạng mà không ảnh hưởng đến mạng của các không gian tên khác. Điều này rất hữu ích khi triển khai các ứng dụng mạng cô lập như các container Docker.

3. **Mount Namespace**: Mount Namespace cung cấp cô lập về hệ thống tệp và điểm gắn. Mỗi không gian tên có một bảng điểm gắn riêng biệt, cho phép các tiến trình trong không gian tên nhìn thấy và truy cập vào các tệp và thư mục chỉ trong không gian tên của chúng. Điều này cho phép các tiến trình chạy trong không gian tên có các không gian tên tệp hệ thống độc lập, giúp đảm bảo tính riêng tư và cô lập của dữ liệu.

4. **IPC Namespace**: IPC Namespace cung cấp cơ chế cô lập về giao tiếp qua bộ nhớ chia sẻ. Mỗi không gian tên có một tập hợp riêng biệt các khóa, hàng đợi, v.v., cho phép các tiến trình trong không gian tên tương tác với các IPC trên hệ thống mà không ảnh hưởng đến các IPC của các không gian tên khác. Điều này giúp đảm bảo tính riêng tư và an toàn của giao tiếp giữa các tiến trình.

5. **UTS Namespace**: UTS Namespace cho phép mỗi không gian tên có một hostname và thông tin hệ thống độc lập. Điều này cho phép các tiến trình trong không gian tên thay đổi hostname và thông tin hệ thống mà không ảnh hưởng đến các không gian tên khác trên hệ thống.

=> Linux Namespace là một công nghệ mạnh mẽ trong hệ điều hành Linux, **cho phép cô lập và chia sẻ tài nguyên hệ thống** một cách linh hoạt và an toàn. Nó đã tạo ra một cách tiếp cận mới trong việc triển khai ứng dụng, nhất là trong lĩnh vực containerization. Việc sử dụng Linux Namespace giúp **tăng tính bảo mật, cải thiện hiệu suất và quản lý tài nguyên hiệu quả** trên hệ thống Linux.

## 2. Network Namespace

### Khái niệm

Network Namespace là một tính năng trong Linux Namespace cho phép cô lập và quản lý độc lập các tài nguyên mạng giữa các tiến trình và ứng dụng chạy trên hệ điều hành Linux. Mỗi Network Namespace có một bộ giao diện mạng, bảng định tuyến và tường lửa riêng biệt, tạo ra một môi trường mạng ảo độc lập. Điều này cho phép các tiến trình trong cùng một Network Namespace tương tác với mạng mà không ảnh hưởng đến mạng của các Network Namespace khác trên hệ thống.

**Một số khái niệm quan trọng liên quan đến Network Namespace:**

*Giao diện mạng (Network Interface)*: Mỗi Network Namespace có các giao diện mạng độc lập. Các giao diện mạng trong một Network Namespace chỉ nhìn thấy và tương tác với các giao diện trong cùng không gian tên đó. Ví dụ, một giao diện mạng có tên eth0 trong một Network Namespace sẽ khác với giao diện mạng cùng tên trong một Network Namespace khác.

*Bảng định tuyến (Routing Table)*: Mỗi Network Namespace có một bảng định tuyến riêng, quyết định cách các gói tin mạng được định tuyến trong không gian tên đó. Điều này cho phép quy định cách tiến trình trong Network Namespace gửi và nhận các gói tin trên mạng.

*Tường lửa (Firewall)*: Mỗi Network Namespace có một tường lửa độc lập, quản lý quy tắc truy cập mạng. Tường lửa này kiểm soát luồng dữ liệu trên giao diện mạng của không gian tên đó, bảo vệ và kiểm soát quyền truy cập vào và ra khỏi không gian tên.

**Các ứng dụng và lợi ích của Network Namespace:**

- Containerization: Network Namespace là một thành phần quan trọng trong việc triển khai container. Mỗi container Docker hoặc môi trường cô lập khác có thể sử dụng một Network Namespace riêng, giúp chúng hoạt động như các máy tính ảo độc lập về mạng. Điều này cho phép chạy nhiều container trên cùng một máy chủ mà không gây xung đột về mạng.

- Quản lý mạng: Network Namespace cung cấp khả năng quản lý mạng tốt hơn. Bằng cách tạo ra các Network Namespace riêng, người quản trị có thể cấu hình và kiểm soát mạng cho các tiến trình và ứng dụng riêng biệt, đồng thời giảm thiểu rủi ro xung đột và cải thiện bảo mật hệ thống.

- Môi trường phát triển và kiểm thử: Network Namespace cung cấp một môi trường cô lập cho phát triển và kiểm thử ứng dụng mạng. Bằng cách sử dụng Network Namespace, nhà phát triển có thể tạo ra các môi trường mạng độc lập để thử nghiệm và kiểm tra ứng dụng mà không ảnh hưởng đến mạng chính trên hệ thống.

Tổng kết, Network Namespace trong Linux Namespace cho phép cô lập và quản lý độc lập các tài nguyên mạng giữa các tiến trình và ứng dụng. Nó đóng vai trò quan trọng trong việc triển khai container, quản lý mạng và tạo môi trường phát triển cô lập. Sử dụng Network Namespace giúp tăng tính linh hoạt, bảo mật và hiệu suất trong việc triển khai ứng dụng mạng trên hệ điều hành Linux.

## 3. Lab thử nghiệm tính năng Linux Network Namespaces

### 3.1. Kết nối hai host trên 2 namespaces sử dụng OpenvSwitch
  **a. Topology:**

Kết nối 2 interfaces trên 2 namespace thông qua OpenvSwitch. Tạo 2 network namespaces:
  - RED Namespace: kết nối với OpenvSwitch thông qua virtual pair interface eth0-r - veth-r.
  - GREEN Namespace: kết nối với OpenvSwitch thông qua virtual pair interface eth0-g - veth-g.
  
Thiết lập địa chỉ IP dải 10.0.0.0/24 cho hai interfaces eth0-r và eth0-g rồi tiến hành ping giữa hai interfaces này kiểm tra kết nối.

![](https://camo.githubusercontent.com/4a164417d3367313bc54ae1a0d297313f902afae1e1d127937b0d73a8b8fd3d8/687474703a2f2f692e696d6775722e636f6d2f504b555657746d2e706e67)

**b. Cấu hình:**
B1: tạo switch ảo
```sh
ovs-vsctl add-br ovs
```
B2: Tạo 2 network namespaces
```sh
ip netns add red
ip netns add green
```
B3:  tạo một cặp giao diện Ethernet ảo với tên `eth0-r` và `veth-r`. Cặp giao diện này được kết nối với nhau, trong đó `eth0-r` là giao diện mà chúng ta muốn thêm vào một không gian tên (namespace) cụ thể, và `veth-r` là giao diện được sử dụng bên ngoài namespace:
```sh
ip link add eth0-r type veth peer name veth-r
ip link set eth0-r netns red 
ovs-vsctl add-port ovs veth-r
```
B4: Tương tự với namespace green:
```sh
ip link add eth0-g type veth peer name veth-g 
ip link set eth0-g netns green 
ovs-vsctl add-port ovs veth-g
```
B5: Kiểm tra cấu hình các interface trên switch ảo
![](https://scontent.fhan14-3.fna.fbcdn.net/v/t1.15752-9/345567467_788325912918858_5158986189663090921_n.png?_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_ohc=vwfN_cYQWpIAX9ZWpPU&_nc_ht=scontent.fhan14-3.fna&oh=03_AdRpIFBF6QJ3dEOdp6VHcdM31gnWgDw39N86ZUOZTohxiA&oe=64A42B32)

B6: Kiểm tra địa chỉ các interface và bảng định tuyến trong green namespace

![](https://scontent.fhan14-4.fna.fbcdn.net/v/t1.15752-9/350880963_816481656506917_1212651247445420406_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_ohc=mISbQeOMtAoAX_mrA8V&_nc_ht=scontent.fhan14-4.fna&oh=03_AdRMm14ejydTQBT5ktNufHaCXTOOmTLqVE-RgmLLrxqPXQ&oe=64A407BA)

B7: Kiểm tra địa chỉ các interface và bảng định tuyến trong red namespace

![](https://scontent.fhan14-3.fna.fbcdn.net/v/t1.15752-9/349678738_1403844083733284_5137382800110856598_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=PxkomvE9a_wAX_ZrdLg&_nc_ht=scontent.fhan14-3.fna&oh=03_AdSBk8Cx1xzl5LT7MXLZYT3EfrDunODiy4jB_v4twflb6g&oe=64A42FD2)

B8: Tiến hành ping thử sang địa chỉ của interface eth0-r (10.0.0.1)

![](https://scontent.fhan14-1.fna.fbcdn.net/v/t1.15752-9/350231294_803570290944917_2641501482027395175_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_ohc=AX5OqOvx7s8AX9fIp8r&_nc_ht=scontent.fhan14-1.fna&oh=03_AdRbaHr17DjOVPSo2jAehS5aIS6o4iAib4reuBcA_lRnTw&oe=64A42863)

### 3.2. Lab DHCP cấp IP cho các host thuộc các namespaces khác nhau

** Topology:**

Topology sau đây lấy ý tưởng từ hệ thống OpenStack. Trên mỗi máy Compute, các máy ảo thuộc về mỗi vlan đại diện cho các máy của một tenant. Chúng tách biệt về layer 2 và được cấp phát IP bởi các DHCP server ảo cùng VLAN (các DHCP server ảo này thuộc về các namespaces khác nhau và không cùng namespace với các máy ảo của các tenant, được cung cấp bởi dịch vụ dnsmasq). Các DHCP server này hoàn toàn có thể cấp dải địa chỉ trùng nhau do tính chất của namespace. Sau đây là mô hình:
<br><br>
<img src="http://i.imgur.com/fbnJ94q.png">
<br><br>

Mô hình bài lab bao gồm 2 DHCP namespace (dhcp-r, dhcp-g) và hai namespaces dành cho các máy ảo của 2 tenant (red, green), các máy ảo trên 2 tenant này thuộc về hai vlan khác nhau (vlan 100 và vlan 200). DHCP server trên các namespace dhcp-r, dhcp-g sẽ cấp địa chỉ IP cho các máy ảo của 2 tenant trên 2 namespace tương ứng là red và green. 
</li>

**b. Cấu hình**
B1: Trước hết cấu hình theo các bước của bài lab trên. Sau đó tiến hành xóa cấu hình địa chỉ IP của 2 interfaces eth0-r và eth0-g. Gán 2 interfaces veth-r và veth-g vào 2 VLAN tương ứng là 100 và 200.
```sh
ovs-vsctl set port veth-r tag=100
ovs-vsctl set port veth-g tag=200
ip netns exec red ip address del 10.0.0.1/24 dev eth0-r
ip netns exec green ip address del 10.0.0.2/24 dev eth0-g
```

B2: Tạo 2 namespace cho 2 DHCP server:
```sh    
ip netns add dhcp-r
ip netns add dhcp-g
```
B3: Trên **switch** ảo ovs tạo 2 internal interface là `tap-r` và `tap-g` để kết nối với 2 namespaces tương ứng là `dhcp-r` và `dhcp-g`. Chú ý gán tap-r vào vlan 100, tap-g vào vlan 200.

```sh
    # cau hinh tap-r
ovs-vsctl add-port ovs tap-r
ovs-vsctl set interface tap-r type=internal
ovs-vsctl set port tap-r tag=100
# cau hinh tap-g
ovs-vsctl add-port ovs tap-g
ovs-vsctl set interface tap-g type=internal
ovs-vsctl set port tap-g tag=200
```
B4: Kiểm tra cấu hình các interfaces của switch ovs. Kết quả tương tự như sau:

![](https://scontent.fhan2-4.fna.fbcdn.net/v/t1.15752-9/351716566_777060933894969_7596731353044774130_n.png?_nc_cat=110&ccb=1-7&_nc_sid=ae9488&_nc_ohc=pZ_X8hZLF9cAX_WTS6W&_nc_ht=scontent.fhan2-4.fna&oh=03_AdRy2YQD7kL-OI3_KG8zf1aVfIWTyhUxsY8EenrBZHQpVA&oe=64A4DA60)

B5: Gán 2 internal interface tap-r và tap-g trên lần lượt vào các namespace dhcp-r và dhcp-g. Chú ý là thực hiện hai thao tác này trên bash của root namespace. Nếu đang thao tác trong các namespace red và green thì phải thoát ra bằng lệnh exit cho tới khi trở về root namespace.

```sh
ip link set tap-r netns dhcp-r
ip link set tap-g netns dhcp-g
```
B5: Thiết lập IP cho các internal interfaces tap-r và tap-g. Thiết lập dải địa chỉ cấp phát cho các máy ảo trên các các tenant namespaces tương ứng red và green
- Cấu hình tap-r
```sh
ip netns exec dhcp-r bash 
ip link set dev lo up
ip link set dev tap-r up
ip address add 10.50.50.2/24 dev tap-r
ip netns exec dhcp-r dnsmasq --interface=tap-r \
--dhcp-range=10.50.50.10,10.50.50.100,255.255.255.0
```
- Cấu hình cho tap-g

```sh
ip netns exec dhcp-g bash
ip link set dev lo up
ip link set dev tap-g up
ip address add 10.50.50.2/24 dev tap-g
# cau hinh dai dia chi cap phat cho cac may ao trong namespace green
ip netns exec dhcp-g dnsmasq --interface=tap-g \
--dhcp-range=10.50.50.10,10.50.50.100,255.255.255.0
```

B6: Kiểm tra các tiến trình đang sử dụng dnsmasq
```sh
nobody     9191  0.0  0.0  56128  1104 ?        S    01:14   0:00 dnsmasq --interface=tap-r --dhcp-range=10.50.50.10,10.50.50.100,255.255.255.0
nobody     9206  0.0  0.0  56128  1104 ?        S    01:15   0:00 dnsmasq --interface=tap-g --dhcp-range=10.50.50.10,10.50.50.100,255.255.255.0
```
Như kết quả kiểm tra ở trên, có thể thấy hai tiến trình có PID 3671 và 3674 đang sử dụng dịch vụ dnsmasq. Kiểm tra xem các tiến trình đó thuộc về namespaces nào:
![](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/350088899_814758776661431_1729275877797523109_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_ohc=7hn8ZKNlUj0AX8rMMt3&_nc_ht=scontent.fhan2-3.fna&oh=03_AdSWvabIzb9O3xRqf4jSZHI0gmWHGHRomQP6f8ZLI1wfcA&oe=64A4DE9C)

B7: Như vậy hai tiến trình này thuộc về 2 namespaces tương ứng là dhcp-r và dhcp-g. Giờ ta tiến hành cấp địa chỉ IP cho các máy ảo tương ứng trên 2 tenant namespaces red và green.
Ở đây không sử dụng máy ảo nên ta sẽ cấp phát IP cho các virtual interfaces eth0-r và eth0-g thuộc hai namespaces tương ứng red và green.

- Xin cấp IP cho eth0-r và kiểm tra địa chỉ IP trong namespace red.
```sh
ip netns exec red dhclient eth0-r # xin cap dia chi IP
ip netns exec red ip a
```
-Kết quả:
![](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/352109368_738978261448219_8734678292704453595_n.png?_nc_cat=109&ccb=1-7&_nc_sid=ae9488&_nc_ohc=m3JkH4a6Nw8AX-w7jbX&_nc_ht=scontent.fhan2-5.fna&oh=03_AdT5Bg4ZsC0Ox189CJQztdBbAW9CACtutUdYqHxRuMDWLw&oe=64A4D685)   

- Xin cấp IP cho eth0-g
```sh
ip netns exec green dhclient eth0-g
ip netns exec green ip a
```
- Kết quả:

![](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/352131427_194737830189864_2034428736474161088_n.png?_nc_cat=109&ccb=1-7&_nc_sid=ae9488&_nc_ohc=ZqHbaF-UdrAAX_QWfuC&_nc_ht=scontent.fhan2-5.fna&oh=03_AdTZshBRwpEW240yEdjkMeyHX4qvvoRObAJbAYaqBEuHPQ&oe=64A4E028)

## Tài liệu tham khảo
[1] - <a href="http://blog.scottlowe.org/2013/09/04/introducing-linux-network-namespaces/">http://blog.scottlowe.org/2013/09/04/introducing-linux-network-namespaces/</a>
<br>
[2] - <a href="http://www.opencloudblog.com/?p=42">http://www.opencloudblog.com/?p=42</a>
<br>
[3] - <a href="https://www.youtube.com/watch?v=_WgUwUf1d34">https://www.youtube.com/watch?v=_WgUwUf1d34</a>
[4] - <a href="http://www.packetu.com/2012/07/12/vrfing-101-understing-vrf-basics/">http://www.packetu.com/2012/07/12/vrfing-101-understing-vrf-basics</a>
</div>