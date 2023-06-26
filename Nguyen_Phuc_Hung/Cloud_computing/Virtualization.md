# Giới thiệu về Cloud Computing

## Tổng quan về ảo hóa

Trước khi khái niệm Cloud Computing ra đời, ảo hóa đóng một vai trò quan trọng và là nền tảng của khái niệm này.

### Khái niệm
- Ảo hóa (virtualization) được định nghĩa là sự triển khai một hệ thống máy tính ảo trên nền một hệ thống máy tính thật. 
- Nó là một công nghệ được thiết kế để tạo ra tầng trung gian giữa hệ thống phần cứng máy tính và phần mềm chạy trên nó. 
- Ảo hóa đề cập đến việc giả lập mọi thiết bị bằng bao gồm sự ảo hóa các nền tảng phần cứng máy tính, các thiết bị lưu trữ, tài nguyên cũng như hệ thống mạng máy tính. Nói cách khác, ảo hóa cũng có thể được coi là một kỹ thuật cho phép người dùng chia sẻ một instance vật lý của một tài nguyên hoặc một ứng dụng giữa nhiều người dùng và tổ chức khác nhau. Mỗi một máy ảo đều có một thiết lập nguồn hệ thống riêng rẽ, hệ điều hành riêng và các ứng dụng riêng. 
- Các thành phần có thể được ảo hóa: Phần cứng (Hardware), Phần mềm (Software), Bộ nhớ (Memory), Lưu trữ (Storage), Hệ thống mạng (Network)
-  Ảo hóa có nguồn gốc từ việc phân chia ổ đĩa, chúng phân chia một máy chủ thực thành nhiều máy chủ logic. Một khi máy chủ thực được chia, mỗi máy chủ logic có thể chạy một hệ điều hành và các ứng dụng độc lập.


 ![](https://thegioimaychu.vn/blog/wp-content/uploads/2019/12/tgmc-blog-5e0318c311470.png)

### Các mức độ ảo hóa
#### Ảo hóa toàn phần (full virtualization)
- Đây là loại ảo hóa mà ta không cần chỉnh sửa hệ điều hành khách (guest OS) cũng như các phần mềm đã được cài đặt trên nó để chạy trong môi trường hệ điều hành chủ (host OS). Khi một phần mềm chạy trên guest OS, các đoạn code của nó không bị biến đổi mà chạy trực tiếp trên host OS và phần mềm đó như đang được chạy trên một hệ thống thực sự
- Trình điều khiển máy ảo phải cung cấp cho máy ảo một “ảnh” của toàn bộ hệ thống, bao gồm BIOS ảo, không gian bộ nhớ ảo, và các thiết bị ảo. Trình điều khiển máy ảo cũng phải tạo và duy trì cấu trúc dữ liệu cho các thành phần ảo (đặc biệt là bộ nhớ), và cấu trúc này phải luôn được cập nhật cho mỗi một truy cập tương ứng được thực hiện bởi máy ảo.

![](https://raw.githubusercontent.com/ImKifu/thuctapsinh/master/HungNK/Basic_Linux_Command/Picture/aohoa1.png)

#### Ảo hóa bán phần (para-virtualization)
- Ảo hóa song song là một phương pháp ảo hóa mà trong đó các máy ảo biết về sự tồn tại của nhau và có thể tương tác trực tiếp. 
- Máy ảo trong môi trường ảo hoá song song được sửa đổi để chạy trong một giao diện lập trình phần mềm (API) đặc biệt, được gọi là giao diện para-virtualization. Giao diện này cho phép các máy ảo truy cập trực tiếp vào các tài nguyên vật lý và chia sẻ thông tin với nhau một cách hiệu quả. 
- Ảo hóa song song có thể mang lại hiệu suất tốt hơn so với ảo hóa toàn phần, nhưng đòi hỏi sự sửa đổi trong hệ điều hành và ứng dụng để hỗ trợ giao diện para-virtualization.

![](https://raw.githubusercontent.com/ImKifu/thuctapsinh/master/HungNK/Basic_Linux_Command/Picture/aohoa4.png)

- Ảo hóa song song đem lại tốc độ cao hơn so với ảo hóa toàn phần và hiệu quả sử dụng các nguồn tài nguyên cũng cao hơn. Nhưng nó yêu cầu các hệ điều hành khách chạy trên máy áo phải được chỉnh sửa
- cực kỳ hữu ích khi người ta chỉ muốn dùng máy ảo để chạy một phần mềm quan trọng nào đó, họ sẽ dùng ảo hóa một phần để tạo ra đủ tài nguyên cần thiết để chạy nó mà không cần phải ảo hóa cả một hệ thống phức tạp. Nếu dùng ảo hóa toàn phần chỉ để chạy một phần mềm duy nhất thì coi như là ta đã lãng phí tài nguyên máy tính một cách vô ích.

![](https://raw.githubusercontent.com/ImKifu/thuctapsinh/master/HungNK/Basic_Linux_Command/Picture/aohoa5.png)

#### Assisted Virtualization
- Sự kết hợp của Full Virtualization và Paravirtualization, có tất cả ưu điểm của cả hai, vừa không bị sửa đổi OS, tương thích với phần cứng mà vẫn được chạy ở ring 0.
- ![](https://raw.githubusercontent.com/ImKifu/thuctapsinh/master/HungNK/Basic_Linux_Command/Picture/aohoa7.png)

 ![](https://raw.githubusercontent.com/ImKifu/thuctapsinh/master/HungNK/Basic_Linux_Command/Picture/aohoa8.png)

### Hypervisor
**Loại-1: Native**

Một hypervisor ở dạng native (hay còn gọi “bare-metal”) chạy trực tiếp trên phần cứng. Nó nằm giữa phần cứng và một hoặc nhiều hệ điều hành khách (guest operating system). Nó được khởi động trước cả hệ điều hành và tương tác trực tiếp với kernel. Điều này mang lại hiệu suất cao nhất có thể vì không có hệ điều hành chính nào cạnh tranh tài nguyên máy tính với nó. Tuy nhiên, nó cũng đồng nghĩa với việc hệ thống chỉ có thể được sử dụng để chạy các máy ảo vì hypervisor luôn phải chạy ngầm bên dưới.

Các hypervisor dạng native này có thể kể đến như VMware ESXi, Microsoft Hyper-V và Apple Boot Camp.

![](https://raw.githubusercontent.com/ImKifu/thuctapsinh/master/HungNK/Basic_Linux_Command/Picture/hypervisor-Native-Baremetal.png)

**Loại-2: Hosted**
Một hypervisor dạng hosted được cài đặt trên một máy tính chủ (host computer), mà trong đó có một hệ điều hành đã được cài đặt. Nó chạy như một ứng dụng cũng như các phần mềm khác trên máy tính. Hầu hết các hypervisor dạng hosted có thể quản lý và chạy nhiều máy ảo cùng một lúc. Lợi thế của một hypervisor dạng hosted là nó có thể được bật lên hoặc thoát ra khi cần thiết, giải phóng tài nguyên cho máy chủ. Tuy nhiên, vì chạy bên trên một hệ điều hành, nó có thể đem lại hiệu suất tương tự như một hypervisor ở dạng native.

![](https://raw.githubusercontent.com/ImKifu/thuctapsinh/master/HungNK/Basic_Linux_Command/Picture/Hosted-Hypervisor-type-2.png)

Ví dụ về các hypervisor dạng hosted bao gồm VMware Workstation, Oracle VirtualBox và Parallels Desktop for Mac.

## Cloud Computing

### Khái niệm

- Cloud computing còn được định nghĩa là mô hình cung cấp các tài nguyên hệ thống máy tính (như network, server, storage, ứng dụng và dịch vụ), đặc biệt là khả năng lưu trữ và khả năng tự động xử lý mà người dùng không quản trị một cách trực tiếp. Cloud computing còn được mô tả việc nhiều người dùng sử dụng tài nguyên của các data center thông qua Internet. Các hệ thống Cloud computing thường phân tán các tính năng tại các vị trí khác nhau trong các cụm server. 
- Đặc điểm: 5-4-3

- Muốn được gọi là Cloud Computing, phải đủ 5 đặc điểm, thuộc 1 hoặc nhiều trong 4 mô hình triển khai và phải cung cấp 1 hoặc nhiều trong 3 mô hình dịch vụ


#### 5 đặc tính cuả Cloud Computing

1. On-demand self-service (Dịch vụ tự phục vụ khi cần): Cloud computing cung cấp khả năng tự phục vụ cho người dùng. Người dùng có thể tự đăng ký, triển khai và quản lý các tài nguyên máy tính một cách độc lập mà không cần sự can thiệp từ phía nhà cung cấp dịch vụ đám mây. Điều này mang lại tính linh hoạt và tiện lợi, giúp người dùng tiết kiệm thời gian và tăng tốc độ triển khai các ứng dụng và dịch vụ.

2. Broad network access (Truy cập mạng rộng): Cloud computing cho phép người dùng truy cập vào các dịch vụ và tài nguyên từ bất kỳ thiết bị nào có kết nối internet. Người dùng có thể truy cập thông qua máy tính cá nhân, máy tính xách tay, điện thoại thông minh, máy tính bảng và các thiết bị di động khác mà không bị giới hạn bởi vị trí vật lý.

3. Resource pooling (Gom nhóm tài nguyên): Cloud computing cho phép tổng hợp các tài nguyên máy tính, chẳng hạn như máy chủ, lưu trữ và mạng, vào một môi trường chung. Các tài nguyên này được quản lý và phân phối một cách linh hoạt để đáp ứng nhu cầu của nhiều người dùng. Tài nguyên không cần phải được cấu hình cụ thể cho từng người dùng, mà có thể được chia sẻ và sử dụng một cách hiệu quả.

4. Rapid elasticity or expansion (Độ co giãn và mở rộng nhanh chóng): Cloud computing cho phép tài nguyên máy tính có thể được mở rộng hoặc thu hẹp một cách nhanh chóng và linh hoạt theo nhu cầu của người dùng. Người dùng có thể tăng hoặc giảm số lượng máy chủ, lưu trữ và tài nguyên khác một cách tự động hoặc theo yêu cầu, giúp đáp ứng cho các tình huống khác nhau mà không gặp trở ngại về khả năng mở rộng.

5. Measured service (Dịch vụ đo lường): Cloud computing cung cấp khả năng đo lường và theo dõi việc sử dụng tài nguyên máy tính. Người dùng được tính phí dựa trên việc sử dụng thực tế của tài nguyên, chẳng hạn như số lượng máy chủ, băng thông mạng hoặc lưu trữ đã sử dụng. Điều này giúp người dùng có hiểu biết rõ về việc sử dụng tài nguyên và đưa ra quyết định quản lý và tối ưu hóa tài nguyên một cách hiệu quả.

#### 4 Mô hình triển khai

- **Public Cloud**

Cái tên đã thể hiện chính nó: public clouds có sẵn cho công chúng và dữ liệu được tạo, lưu trữ trên các máy chủ của bên thứ ba. Cơ sở hạ tầng máy chủ thuộc về các nhà cung cấp dịch vụ quản lý nó và quản lý tài nguyên của pool, đó là lý do tại sao các công ty người dùng không cần phải mua và bảo trì phần cứng của riêng họ. Các công ty cung cấp tài nguyên cung cấp dịch vụ miễn phí hoặc trả tiền cho mỗi lần sử dụng thông qua Internet. Người dùng có thể mở rộng tài nguyên theo yêu cầu. 

Mô hình triển khai đám mây public cloud là lựa chọn hàng đầu cho các doanh nghiệp có mối quan tâm về quyền riêng tư thấp.

![](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/355618284_1257068044930453_6099336377683492796_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=f5_59E79HycAX_aQZTF&_nc_ht=scontent.fhan2-5.fna&oh=03_AdTxRTAjUnPI14G8dLRzZT0ab9S0HNNNQOp0MOpElkOQfg&oe=64BB7442)


- Ưu điểm của mô hình Public Cloud
  - Quản lý cơ sở hạ tầng dễ dàng. Có một bên thứ ba chạy cơ sở hạ tầng đám mây của bạn rất tiện lợi: bạn không cần phải phát triển và bảo trì phần mềm của mình vì nhà cung cấp dịch vụ sẽ làm điều đó cho bạn. Ngoài ra, việc thiết lập và sử dụng cơ sở hạ tầng không phức tạp.

  - Khả năng mở rộng cao. Bạn có thể dễ dàng mở rộng dung lượng của đám mây khi yêu cầu của công ty bạn tăng lên.

  - Giảm chi phí: Bạn chỉ trả tiền cho dịch vụ bạn sử dụng, vì vậy không cần đầu tư vào phần cứng hoặc phần mềm.

  - Thời gian hoạt động 24/7: Mạng lưới rộng lớn của các máy chủ của nhà cung cấp đảm bảo cơ sở hạ tầng của bạn luôn sẵn sàng và có thời gian hoạt động được cải thiện.

- Nhược điểm của Public Cloud

  - Độ tin cậy tương đối: Mạng máy chủ tương tự đó cũng có nghĩa là để đảm bảo chống lại sự cố. Nhưng thỉnh thoảng, public clouds gặp sự cố và trục trặc, như trong trường hợp sự cố CRM của Salesforce năm 2016 gây ra sự cố bộ nhớ.

  - Vấn đề bảo mật dữ liệu và quyền riêng tư làm phát sinh mối quan tâm. Mặc dù việc truy cập vào dữ liệu rất dễ dàng, nhưng mô hình triển khai công khai khiến người dùng không biết thông tin của họ được lưu giữ ở đâu và ai có quyền truy cập vào nó.

  - Việc thiếu một dịch vụ đặt trước. Các nhà cung cấp dịch vụ chỉ có các lựa chọn dịch vụ được tiêu chuẩn hóa, đó là lý do tại sao họ thường không đáp ứng được các yêu cầu phức tạp hơn.


- **Private Cloud**

Có rất ít hoặc không có sự khác biệt giữa mô hình public và mô hình private từ quan điểm kỹ thuật, vì kiến ​​trúc của chúng rất giống nhau. Tuy nhiên, trái ngược với public clouds có sẵn cho người dùng, private clouds chỉ có một công ty cụ thể sở hữu đám mây riêng. Đó là lý do tại sao nó còn được gọi là mô hình nội bộ (internal) hoặc mô hình công ty (corporate).

Máy chủ có thể được lưu trữ bên ngoài hoặc tại cơ sở của công ty chủ sở hữu. Bất kể vị trí thực tế của chúng là gì, các cơ sở hạ tầng này được duy trì trên một mạng riêng được chỉ định và sử dụng phần mềm và phần cứng chỉ được sử dụng bởi công ty chủ sở hữu.

Phạm vi mọi người được xác định rõ ràng có quyền truy cập vào thông tin được lưu giữ trong kho lưu trữ riêng tư, điều này ngăn công chúng sử dụng thông tin đó. Do nhiều vụ vi phạm trong những năm gần đây, ngày càng nhiều tập đoàn lớn đã quyết định sử dụng mô hình private clouds, vì điều này giảm thiểu các vấn đề về bảo mật dữ liệu.

So với mô hình public, private clouds cung cấp nhiều cơ hội hơn để tùy chỉnh cơ sở hạ tầng theo yêu cầu của công ty. Mô hình tư nhân đặc biệt thích hợp cho các công ty tìm cách bảo vệ các hoạt động quan trọng của họ hoặc cho các doanh nghiệp có yêu cầu thay đổi liên tục.

![](https://static.wixstatic.com/media/22ad9e_dbd6834e8959405c9835c609a1852704~mv2.jpg/v1/fill/w_700,h_761,al_c,q_85,enc_auto/22ad9e_dbd6834e8959405c9835c609a1852704~mv2.jpg)

- Lợi ích của Private Cloud

Tất cả những lợi ích của mô hình triển khai này là kết quả của sự tự chủ của nó. Những lợi ích của private cloud như sau:
Phát triển riêng và linh hoạt và khả năng mở rộng cao, cho phép các công ty tùy chỉnh cơ sở hạ tầng phù hợp với yêu cầu của họ
Bảo mật, quyền riêng tư và độ tin cậy cao, vì chỉ những người được ủy quyền mới có thể truy cập tài nguyên.

- Mặt hạn chế của Private Cloud

Nhược điểm lớn của mô hình triển khai đám mây riêng là chi phí của nó, vì nó đòi hỏi chi phí đáng kể về phần cứng, phần mềm và đào tạo nhân viên. Đó là lý do tại sao mô hình triển khai tính toán linh hoạt và an toàn này không phải là lựa chọn phù hợp cho các công ty nhỏ.

- **Community Cloud**

Mô hình triển khai Community Cloud phần lớn giống với mô hình Private Cloud; sự khác biệt duy nhất là tập hợp người dùng. Trong khi chỉ có một công ty sở hữu máy chủ đám mây riêng, một số tổ chức có nền tảng tương tự chia sẻ cơ sở hạ tầng và các tài nguyên liên quan của community cloud.

Nếu tất cả các tổ chức tham gia đều có các yêu cầu về bảo mật, quyền riêng tư và hiệu suất đồng nhất, thì kiến ​​trúc trung tâm dữ liệu nhiều bên thuê này sẽ giúp các công ty này nâng cao hiệu quả của họ, như trong trường hợp các dự án chung. Một đám mây tập trung tạo điều kiện thuận lợi cho việc phát triển, quản lý và thực hiện dự án. Các chi phí được chia sẻ bởi tất cả người dùng.

![](https://static.wixstatic.com/media/22ad9e_1c3930061b4c4724825f78338d3dff88~mv2.jpg/v1/fill/w_700,h_754,al_c,q_85,enc_auto/22ad9e_1c3930061b4c4724825f78338d3dff88~mv2.jpg)

- Điểm mạnh của Community Cloud
  - Tiết kiệm chi phí
  - Cải thiện bảo mật, quyền riêng tư và độ tin cậy
  - Dễ dàng chia sẻ dữ liệu và cộng tác

- Điểm yếu của Community Cloud
  - Chi phí cao so với mô hình public cloud
  - Chia sẻ dung lượng băng thông và dung lượng lưu trữ cố định
  - Chưa được sử dụng phổ biến
  



- **Hybrid Cloud**

Như thường thấy với bất kỳ sự kết hợp nào, hybrid cloud bao gồm các tính năng tốt nhất của các mô hình triển khai nói trên (public, private và community). Nó cho phép các công ty mix and match các khía cạnh của ba loại phù hợp nhất với yêu cầu của họ.

Ví dụ: một công ty có thể cân bằng lượng công việc của mình bằng cách định vị khối lượng công việc quan trọng trên private cloud an toàn và triển khai các khối lượng ít quan trọng hơn cho public cloud. Mô hình triển khai hybrid cloud không chỉ bảo vệ và kiểm soát các tài sản quan trọng về mặt chiến lược mà còn theo cách hiệu quả về chi phí và tài nguyên. Ngoài ra, cách tiếp cận này tạo điều kiện thuận lợi cho tính di động của dữ liệu và ứng dụng.

![](https://static.wixstatic.com/media/22ad9e_9f5b92a93b2446ef95822c19f6836855~mv2.jpg/v1/fill/w_700,h_739,al_c,q_85,enc_auto/22ad9e_9f5b92a93b2446ef95822c19f6836855~mv2.jpg)



#### 3 mô hình dịch vụ

![](https://toidicodedao.files.wordpress.com/2018/10/iaas-paas-saas-comparison.jpg)

![](https://toidicodedao.files.wordpress.com/2018/10/iaas-paas-saas-hierarchy-diagram-e1538834082956.png)
**1. IaaS (Infrastructure as a Service - Cơ sở hạ tầng như một Dịch vụ)**:

- IaaS cung cấp hạ tầng cơ bản của một môi trường đám mây, bao gồm máy chủ ảo, lưu trữ, mạng, và tài nguyên khác, cho phép người dùng tự quản lý và triển khai ứng dụng, dịch vụ và hệ thống mà không cần lo lắng về việc quản lý phần cứng cơ bản.
Người dùng có toàn quyền kiểm soát hệ điều hành, phần mềm, và ứng dụng của mình trên môi trường đám mây được cung cấp bởi nhà cung cấp dịch vụ.
- Linh hoạt và tiết kiệm chi phí: Người dùng có toàn quyền kiểm soát hệ điều hành, phần mềm và ứng dụng, và chỉ trả phí cho tài nguyên thực sự sử dụng.
- Mở rộng dễ dàng: Có khả năng mở rộng tài nguyên theo nhu cầu tăng trưởng của doanh nghiệp.
- Quản lý dễ dàng: Nhà cung cấp dịch vụ quản lý và duy trì phần cứng và hạ tầng mạng.

**2. PaaS (Platform as a Service - Nền tảng như một Dịch vụ)**:

- PaaS cung cấp một nền tảng phát triển và triển khai ứng dụng cho người dùng. Người dùng có thể xây dựng, kiểm thử, và triển khai ứng dụng mà không cần quan tâm đến việc quản lý cơ sở hạ tầng.
- PaaS cung cấp các công cụ phát triển ứng dụng, ngôn ngữ lập trình, cơ sở dữ liệu và môi trường thực thi để người dùng xây dựng và triển khai ứng dụng của mình.
- Người dùng chỉ cần quan tâm đến việc phát triển ứng dụng và dịch vụ, không cần lo lắng về việc quản lý phần cứng hay hạ tầng mạng.

**3. SaaS (Software as a Service - Phần mềm như một Dịch vụ)**:

- SaaS cung cấp các ứng dụng phần mềm hoàn chỉnh và sẵn sàng sử dụng thông qua internet.
- Người dùng có thể truy cập và sử dụng các ứng dụng từ bất kỳ thiết bị nào có kết nối internet, mà không cần cài đặt hoặc quản lý phần mềm trên máy tính của mình.
- Các ứng dụng SaaS được cung cấp và duy trì bởi nhà cung cấp dịch vụ đám mây, và người dùng chỉ cần trả phí sử dụng dịch vụ theo mô hình thuê bao hoặc thanh toán theo lượt sử dụng.
Ví dụ: Gmail, Dropbox, Salesforce.


### Tài liệu tham khảo:

https://www.osam.io/post/4-mo-hinh-dien-toan-dam-may-pho-bien
https://toidicodedao.com/2018/10/23/so-sanh-iaas-paas-saas-la-gi/
https://viblo.asia/p/tan-man-ao-hoa-ai-cung-biet-nhung-cu-the-no-la-gi-Do754NV3ZM6
https://news.cloud365.vn/kvm-tong-quan-ve-virtualization-va-hypervisor/
