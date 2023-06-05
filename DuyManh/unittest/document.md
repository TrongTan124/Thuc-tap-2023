## REST API
- API là giao diện lập trình ứng dụng , là một bộ quy tắc xác định cách các ứng dụng hoặc thiết bị có thể kết nối và giao tiếp với nhau
- REST là một tập hợp các ràng buộc đặt ra cách thức hoạt động của API
- Nếu một API được gọi là RESTFUL, nghĩa là api tuân theo kiến trúc REST
#### REST design principles
- Uniform interface: Tất cả các yêu cầu API cho cùng một tài nguyên sẽ trông giống nhau, bất kể yêu cầu đến từ đâu. API REST phải đảm bảo rằng cùng một phần dữ liệu, chẳng hạn như tên hoặc địa chỉ email của người dùng, chỉ thuộc về một mã định danh tài nguyên thống nhất (URI). Tài nguyên không nên quá lớn nhưng phải chứa mọi thông tin mà khách hàng có thể cần.
- Client-server decoupling: Trong thiết kế API REST, các ứng dụng máy khách và máy chủ phải hoàn toàn độc lập với nhau. Thông tin duy nhất mà ứng dụng khách nên biết là URI của tài nguyên được yêu cầu; nó không thể tương tác với ứng dụng máy chủ theo bất kỳ cách nào khác. Tương tự, ứng dụng máy chủ không nên sửa đổi ứng dụng khách ngoài việc chuyển ứng dụng đó tới dữ liệu được yêu cầu qua HTTP.
- Statelessness: API REST là không trạng thái, nghĩa là mỗi yêu cầu cần bao gồm tất cả thông tin cần thiết để xử lý nó. Nói cách khác, API REST không yêu cầu bất kỳ phiên phía máy chủ nào. Các ứng dụng máy chủ không được phép lưu trữ bất kỳ dữ liệu nào liên quan đến yêu cầu của máy khách.
- Cacheability: Khi có thể, các tài nguyên phải được lưu trong bộ nhớ cache ở phía máy khách hoặc máy chủ. Phản hồi của máy chủ cũng cần chứa thông tin về việc liệu bộ nhớ đệm có được phép đối với tài nguyên được phân phối hay không. Mục tiêu là cải thiện hiệu suất ở phía máy khách, đồng thời tăng khả năng mở rộng ở phía máy chủ.
- Layered system architecture: Trong API REST, các cuộc gọi và phản hồi đi qua các lớp khác nhau. Theo nguyên tắc thông thường, ứng dụng máy khách và máy chủ không kết nối trực tiếp với nhau. Có thể có một số trung gian khác nhau trong vòng truyền thông. Các API REST cần được thiết kế sao cho cả máy khách và máy chủ đều không thể biết liệu nó giao tiếp với ứng dụng cuối hay ứng dụng trung gian.
#### Tool API design
- Swagger: là một công cụ phổ biến để thiết kế, xây dựng và tài liệu hóa API. Nó cho phép bạn định nghĩa, mô tả và chia sẻ thông tin về các điểm cuối (endpoints) của API, các tham số, kiểu dữ liệu và các tài liệu liên quan khác. Swagger cung cấp một giao diện tương tác đẹp và có thể được sử dụng để tạo tài liệu API tự động.
- Postman: Ngoài việc là một công cụ để kiểm thử API, Postman cũng cung cấp khả năng thiết kế API thông qua tính năng Collections và làm việc với tài liệu OpenAPI. Bạn có thể xây dựng và quản lý các yêu cầu API, thực hiện kiểm thử và tài liệu hóa API của mình trong Postman.
- Insomnia: Insomnia là một công cụ khác tương tự như Postman cho phép bạn xây dựng, thử nghiệm và tài liệu hóa các yêu cầu API. Insomnia hỗ trợ giao diện người dùng đẹp, hỗ trợ các tính năng như kiểm thử API, chia sẻ yêu cầu, tự động hoá và tạo tài liệu.
- Apiary: Apiary là một công cụ thiết kế API trực quan và hợp tác. Nó cho phép bạn định nghĩa cú pháp API bằng ngôn ngữ API Blueprint hoặc OpenAPI và tự động tạo tài liệu API dựa trên đó. Bên cạnh đó, Apiary còn cung cấp các tính năng như chia sẻ tài liệu, mô phỏng và kiểm tra API.
- Stoplight: Stoplight là một công cụ thiết kế API toàn diện với các tính năng như xây dựng giao diện API, kiểm thử, tạo tài liệu và quản lý API. Stoplight hỗ trợ OpenAPI và RAML và cung cấp giao diện người dùng trực quan và dễ sử dụng.
#### Flask Framework
- Là một micro web framework được viết bằng Python. Nó được phân loại là một framework vi mô bởi vì nó không yêu cầu các công cụ hoặc thư viện cụ thể. Nó không có lớp trừu tượng hóa cơ sở dữ liệu, xác thực biểu mẫu hoặc bất kỳ thành phần nào khác nơi các thư viện bên thứ ba có sẵn cung cấp các chức năng chung. Hiện framework này đã trở thành công cụ chính trong phát triển ứng dụng web của Python.
#### Ưu, nhược điểm của Flask Python 
**Ưu điểm:**
- Siêu nhỏ nhẹ, là một công cụ tối giản
- Tốc độ hoạt động cực nhanh
- Có khả năng hỗ trợ NoQuery
- Tương đối đơn giản (so với các framework có cùng chức năng khác)
- Mang lại khả năng kết nối với các tiện ích mở rộng bởi không có ORM
- Trình duyệt được nhúng sẵn trình gỡ rối
- Sử dụng các mã ngắn, đơn giản trong những bộ xương Python
- Ngăn chặn các rủi ro về bảo mật khi lập trình web do ít phụ thuộc vào bên thứ ba
- Có khả năng kiểm soát mọi vấn đề khi dùng Flask.
- Cho phép biên dịch mô-đun, thư viện, giúp việc lập trình nhanh chóng, dễ dàng hơn và không cần gõ code bậc thấp

**Nhược điểm:**  lập trình viên cần tự gọi tiện ích mở rộng nếu có nhu cầu hoặc thực hiện lượng công việc nhiều hơn.

#### Lý do sử dụng Flask
**Tùy biến linh hoạt:** Flask Python cung cấp khả năng tùy biến linh hoạt trong lập trình, phát triển ứng dụng, lập trình viên có thể sử dụng thư viện, công cụ hoặc các cơ chế trong các dự án. Ngoài ra, framework này còn hỗ trợ lập trình viên trong sử dụng tiện ích mở rộng nhằm tích hợp thêm tính năng cho ứng dụng. 
**Micro web framework:** Flask Python là micro web framework, không cần công cụ hoặc thư viện cụ thể, mang đến lõi chức năng tối giản nhưng có thể mở rộng cho các ứng dụng web. Nhiều thành phần tiện ích như xác thực biểu mẫu, tích hợp CSDL, công nghệ xác thực, RESTful,, email,...có thể đưa vào web bất cứ lúc nào. 
**Dễ cài đặt, triển khai:** Flask Python được cài đặt một cách dễ dàng và các thao tác của nó cũng rất đơn giản. Lập trình viên chỉ cần vài dòng lệnh là có thể xây dựng các ứng dụng đơn giản.
**Lựa chọn thông minh:** Framework này hỗ trợ xây dựng các API, web services, các ứng dụng web application cỡ vừa và nhỏ. Nó là công cụ tuyệt vời của các nhà phát triển. 
Hỗ trợ tập trung xây dựng các ý tưởng và mục tiêu riêng: Các đặc điểm như nhỏ gọn, linh hoạt, dễ sử dụng, tối giản, định tuyến dễ dàng, dễ mở rộng,... của Flask Python cho phép lập trình viên tập trung chủ yếu vào khâu xác định các ý tưởng, mục tiêu riêng cho ứng dụng web.
**Nhiều tài liệu:** Được biết đến và sử dụng rộng rãi nên Flask Python có tài liệu tham khảo rất phong phú. Bạn có thể tìm đọc các tài liệu miễn phí trên mạng hoặc đặt mua sách về nhà.
**Cộng đồng lớn:** Cộng đồng những người sử dụng Flask Python trải rộng trên khắp thế giới, bạn có thể liên hệ, trao đổi hoặc tìm kiếm sự giúp đỡ từ cộng đồng qua mạng xã hội hoặc các diễn đàn online một cách dễ dàng.
**Sử dụng phổ biến:** Flask Python được sử dụng trong phát triển khá nhiều ứng dụng nổi tiếng như Pinterest, LinkedIn,  Reddit, Twilio, Netflix, Uber… 