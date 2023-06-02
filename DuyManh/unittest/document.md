## REST API
- API là giao diện lập trình ứng dụng , là một bộ quy tắc xác định cách các ứng dụng hoặc thiết bị có thể kết nối và giao tiếp với nhau
- REST là một tập hợp các ràng buộc đặt ra cách thức hoạt động của API
- Nếu một API được gọi là RESTFUL, nghĩa là api tuân theo kiến trúc REST
#### REST design principles
- Uniform interface: Tất cả các yêu cầu API cho cùng một tài nguyên sẽ trông giống nhau, bất kể yêu cầu đến từ đâu. API REST phải đảm bảo rằng cùng một phần dữ liệu, chẳng hạn như tên hoặc địa chỉ email của người dùng, chỉ thuộc về một mã định danh tài nguyên thống nhất (URI). Tài nguyên không nên quá lớn nhưng phải chứa mọi thông tin mà khách hàng có thể cần.
- Client-server decoupling: 
- Statelessness: Trong thiết kế API REST, các ứng dụng máy khách và máy chủ phải hoàn toàn độc lập với nhau. Thông tin duy nhất mà ứng dụng khách nên biết là URI của tài nguyên được yêu cầu; nó không thể tương tác với ứng dụng máy chủ theo bất kỳ cách nào khác. Tương tự, ứng dụng máy chủ không nên sửa đổi ứng dụng khách ngoài việc chuyển ứng dụng đó tới dữ liệu được yêu cầu qua HTTP.

- Cacheability: 
- Layered system architecture: 
- Code on demand (optional): 
#### Tool API design
- Swagger: là một công cụ phổ biến để thiết kế, xây dựng và tài liệu hóa API. Nó cho phép bạn định nghĩa, mô tả và chia sẻ thông tin về các điểm cuối (endpoints) của API, các tham số, kiểu dữ liệu và các tài liệu liên quan khác. Swagger cung cấp một giao diện tương tác đẹp và có thể được sử dụng để tạo tài liệu API tự động.
- postman: Ngoài việc là một công cụ để kiểm thử API, Postman cũng cung cấp khả năng thiết kế API thông qua tính năng Collections và làm việc với tài liệu OpenAPI. Bạn có thể xây dựng và quản lý các yêu cầu API, thực hiện kiểm thử và tài liệu hóa API của mình trong Postman.
- Insomnia: Insomnia là một công cụ khác tương tự như Postman cho phép bạn xây dựng, thử nghiệm và tài liệu hóa các yêu cầu API. Insomnia hỗ trợ giao diện người dùng đẹp, hỗ trợ các tính năng như kiểm thử API, chia sẻ yêu cầu, tự động hoá và tạo tài liệu.
- Apiary: Apiary là một công cụ thiết kế API trực quan và hợp tác. Nó cho phép bạn định nghĩa cú pháp API bằng ngôn ngữ API Blueprint hoặc OpenAPI và tự động tạo tài liệu API dựa trên đó. Bên cạnh đó, Apiary còn cung cấp các tính năng như chia sẻ tài liệu, mô phỏng và kiểm tra API.
- Stoplight: Stoplight là một công cụ thiết kế API toàn diện với các tính năng như xây dựng giao diện API, kiểm thử, tạo tài liệu và quản lý API. Stoplight hỗ trợ OpenAPI và RAML và cung cấp giao diện người dùng trực quan và dễ sử dụng.
#### Flask Framework
- Là một micro web framework được viết bằng Python . Nó được phân loại là mộtkhung vi môbởi vì nó không yêu cầu các công cụ hoặc thư viện cụ thể. Nó không có lớp trừu tượng hóa cơ sở dữ liệu, xác thực biểu mẫu hoặc bất kỳ thành phần nào khác nơi các thư viện bên thứ ba có sẵn cung cấp các chức năng chung.