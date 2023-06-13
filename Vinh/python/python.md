# Python core

## Lịch sử, đặc điểm của Python và giá trị sử dụng:

Python là một ngôn ngữ lập trình thông dịch, có cú pháp đơn giản và dễ đọc. Nó được tạo ra vào những năm 1990 bởi Guido van Rossum và hiện đang được phát triển và duy trì bởi Python Software Foundation. Một số đặc điểm của Python bao gồm:

- Dễ học: Python có cú pháp rõ ràng và dễ hiểu, giúp người mới học lập trình dễ dàng tiếp cận.
- Đa mục đích: Python hỗ trợ nhiều phong cách lập trình, bao gồm lập trình hướng đối tượng, lập trình hàm và lập trình cấu trúc.
- Cộng đồng phát triển mạnh mẽ: Python có một cộng đồng phát triển lớn, cung cấp nhiều thư viện và tài liệu hữu ích.
- Đa nền tảng: Python có thể chạy trên nhiều nền tảng, bao gồm Windows, macOS và Linux.
- Độ phổ biến: Python là một trong những ngôn ngữ lập trình phổ biến nhất, được sử dụng rộng rãi trong nhiều lĩnh vực như phân tích dữ liệu, trí tuệ nhân tạo, phát triển web, và nhiều hơn nữa.

## Cài đặt Python 3.9.12: Để cài đặt Python 3.9.12, bạn có thể làm theo các bước sau:

- Truy cập trang web chính thức của Python tại https://www.python.org/downloads/release/python-3912/ (hoặc phiên bản khác của Python 3.9).
- Tải xuống bản cài đặt phù hợp với hệ điều hành của bạn (Windows, macOS hoặc Linux).
- Chạy tệp cài đặt đã tải xuống và làm theo hướng dẫn để hoàn tất quá trình cài đặt.
- Cài đặt và sử dụng Jupyter Notebook: Jupyter Notebook là một môi trường lập trình tương tác cho Python (và nhiều ngôn ngữ khác). Để cài đặt và sử dụng Jupyter Notebook, bạn có thể làm theo các bước sau:

### Cài đặt Python (nếu chưa cài đặt).

- Mở Terminal hoặc Command Prompt và chạy lệnh sau để cài đặt Jupyter Notebook qua pip (Python package manager):
- pip install jupyter
- Sau khi cài đặt thành công, chạy lệnh sau để khởi động Jupyter Notebook:
- jupyter notebook
- Trình duyệt web mặc định của bạn sẽ mở và hiển thị giao diện Jupyter Notebook. Bạn có thể tạo mới một Notebook hoặc mở các Notebook đã tồn tại.
- Cài đặt các thư viện ngoài sử dụng pip module: Để cài đặt các thư viện Python bên ngoài, bạn có thể sử dụng pip, trình quản lý gói mặc định của Python. Ví dụ, để cài đặt thư viện requests, bạn có thể chạy lệnh sau trong

## Terminal hoặc Command Prompt:

- pip install requests
- Lệnh này sẽ tải xuống và cài đặt thư viện requests từ Python Package Index (PyPI). Bạn có thể thay đổi requests thành tên của thư viện bạn muốn cài đặt.

## Built-in functions: Python cung cấp một số hàm tích hợp sẵn (built-in functions) mà bạn có thể sử dụng trong chương trình của mình mà không cần phải cài đặt thêm bất kỳ thư viện nào. Một số hàm tích hợp sẵn phổ biến bao gồm print(), len(), range(), input(), type(), int(), float(), str(), list(), dict(), set() và nhiều hơn nữa.

## Kiểu dữ liệu (List, Dict, Set, Tuple): Python cung cấp nhiều kiểu dữ liệu như list, dict, set và tuple.

1. List: List là một mảng có thể thay đổi được các phần tử trong đó. Các phần tử trong list được phân tách bằng dấu phẩy và được đặt trong cặp dấu ngoặc vuông []. Ví dụ: [1, 2, 3].
2. Dict: Dict (Dictionary) là một tập hợp các cặp key-value không theo thứ tự. Mỗi phần tử trong dict được định nghĩa bởi một key duy nhất và giá trị tương ứng với key đó, phân tách bằng dấu hai chấm (:), các cặp key-value được phân tách bằng dấu phẩy và đặt trong cặp dấu ngoặc nhọn {}. Ví dụ: {'name': 'John', 'age': 25}.
3. Set: Set là một tập hợp các phần tử không theo thứ tự và không chứa các phần tử trùng lặp. Các phần tử trong set được phân tách bằng dấu phẩy và đặt trong cặp dấu ngoặc nhọn {}. Ví dụ: {1, 2, 3}.
4. Tuple: Tuple là một tập hợp các phần tử không thay đổi (bất biến). Các phần tử trong tuple được phân tách bằng dấu phẩy và đặt trong cặp dấu ngoặc tròn (). Ví dụ: (1, 2, 3).

## Cú pháp: Cú pháp trong Python rất dễ đọc và rõ ràng. Dưới đây là một số quy tắc cú pháp chung:

1. Thụt lề: Python sử dụng thụt lề (indentation) để xác định khối mã. Các dòng mã trong cùng một khối phải có cùng mức thụt lề. Thông thường, 4 dấu cách hoặc một tab được sử dụng để thụt lề.
2. Dấu phẩy: Các phần tử trong danh sách (list), tuple, dict, set được phân tách bằng dấu phẩy.
3. Dấu ngoặc: Các dấu ngoặc (ngoặc tròn, ngoặc vuông, ngoặc nhọn) được sử dụng để bao bọc các biểu thức, danh sách và tập hợp.
4. Dấu hai chấm: Dấu hai chấm (:) được sử dụng để đánh dấu khối mã (block) và phần thân của các câu lệnh điều khiển như if, for, while.
5. Package, module: Trong Python, một package là một cách tổ chức và quản lý các module liên quan nhau. Một package là một thư mục chứa các file Python và một tệp **init**.py để xác định rằng thư mục đó là một package. Một module là một tệp Python (.py) chứa mã Python. Module được sử dụng để tổ chức và tách biệt mã trong các phạm vi khác nhau.

## Quy tắc viết code: Trong Python, có một số quy tắc viết code chung để giữ mã của bạn dễ đọc và nhất quán. Một số quy tắc chung bao gồm:

1. Sử dụng thụt lề 4 dấu cách hoặc một tab để định dạng mã.
2. Đặt tên biến và hàm theo quy tắc snake_case (chữ thường và các từ cách nhau bằng dấu gạch dưới).
3. Đặt tên lớp theo quy tắc CamelCase (chữ cái đầu tiên của mỗi từ viết hoa, không có dấu gạch dưới).
4. Sử dụng các comment (chú thích) để giải thích mã và làm cho nó dễ đọc hơn.
5. Tuân thủ theo các quy tắc PEP 8, hướng dẫn viết code chuẩn của Python.

## Decorator: Decorator là một cú pháp đặc biệt trong Python cho phép bạn mở rộng hoặc thay đổi hành vi của một hàm mà không cần thay đổi mã nguồn của hàm đó. Decorator được áp dụng cho một hàm bằng cách đặt @ trước tên decorator trước khai báo hàm. Decorator thường được sử dụng để thêm chức năng bổ sung, như ghi log, đo thời gian hoặc kiểm tra điều kiện, cho một hàm.

## Lập trình hướng đối tượng trong Python

- Class, method: Trong lập trình hướng đối tượng (OOP), một class là một bản thiết kế hoặc mô tả cho một đối tượng cụ thể. Nó định nghĩa các thuộc tính (biến) và phương thức (hàm) mà đối tượng sẽ có khi được tạo từ class. Một method là một hàm được định nghĩa bên trong class và hoạt động trên các đối tượng của class đó.

Các tính chất của OOP trong Python:

1. Encapsulation (Đóng gói): Đóng gói là tính chất cho phép bạn kết hợp dữ liệu và mã liên quan vào một đối tượng duy nhất. Bạn có thể sử dụng các phương thức để tương tác với dữ liệu trong đối tượng.
2. Inheritance (Kế thừa): Kế thừa cho phép bạn xây dựng lớp mới trên cơ sở của lớp đã tồn tại. Lớp con (subclass) kế thừa các thuộc tính và phương thức của lớp cha (superclass), và có thể mở rộng hoặc ghi đè chúng.
3. Polymorphism (Đa hình): Đa hình cho phép các đối tượng cùng loại có thể thực hiện các hành động khác nhau dựa trên loại của đối tượng đó hoặc các đối tượng con của nó. Điều này được đạt được thông qua việc ghi đè phương thức hoặc sử dụng kỹ thuật gọi phương thức động (dynamic method dispatch).
4. Abstraction (Trừu tượng): Trừu tượng cho phép bạn ẩn đi các chi tiết cài đặt của một đối tượng và chỉ tập trung vào các phương thức công khai và giao diện bên ngoài của đối tượng.
5. Private, protected, public: Trong Python, không có từ khóa private, protected hoặc public như trong một số ngôn ngữ khác để xác định quyền truy cập vào các thuộc tính và phương thức. Tuy nhiên, có một quy ước về việc sử dụng dấu gạch dưới trước tên biến hoặc phương thức để chỉ định mức độ truy cập.

#### \_private_variable: Biến có dấu gạch dưới đầu tiên chỉ ra rằng biến là "private" và không nên được truy cập trực tiếp từ bên ngoài lớp. Tuy nhiên, biến vẫn có thể được truy cập và sử dụng từ bên ngoài, nhưng không nên làm điều đó.

#### \_\_private_variable: Biến có hai dấu gạch dưới đầu tiên chỉ ra rằng biến là "strongly private" và không nên được truy cập từ bên ngoài lớp hoặc các lớp con. Biến này sẽ được đổi tên theo quy tắc "name mangling" để ngăn truy cập trực tiếp từ bên ngoài.

- Không có cú pháp đặc biệt nào để chỉ định "protected" hoặc "public". Các thuộc tính và phương thức mà không có dấu gạch dưới đầu tiên được coi là "public" và có thể truy cập từ bất kỳ nơi nào.
  Static method, class method: Trong Python, có hai loại phương thức đặc biệt liên quan đến class:

#### Static method (phương thức tĩnh): Phương thức tĩnh là một phương thức không truy cập vào các thuộc tính hoặc phương thức của lớp. Nó được định nghĩa bằng cách sử dụng decorator @staticmethod và không có tham số đặc biệt như self hoặc cls.

#### Class method (phương thức lớp): Phương thức lớp là một phương thức được truyền vào một tham số đặc biệt đại diện cho lớp chứ không phải đối tượng. Nó được định nghĩa bằng cách sử dụng decorator @classmethod và có tham số đặc biệt là cls thay vì self.

#### Get, set, property: Trong Python, để truy cập và cập nhật các thuộc tính private hoặc protected, ta thường sử dụng các phương thức get và set. Tuy nhiên, có một cú pháp đặc biệt được sử dụng để định nghĩa các thuộc tính với các phương thức getter và setter một cách thuận tiện hơn, đó là sử dụng decorator @property và @<attribute_name>.setter.

#### Abstract class, method: Abstract class (lớp trừu tượng) là một lớp không thể được khởi tạo và được sử dụng như một bản thiết kế cho các lớp con. Trong Python, để định nghĩa một abstract class, bạn cần sử dụng module abc (Abstract Base Class). Một abstract class có thể chứa các phương thức trừu tượng (abstract method) mà các lớp con phải triển khai.

#### Interface: Trong Python, không có khái niệm interface giống như trong một số ngôn ngữ lập trình khác như Java. Tuy nhiên, bạn có thể sử dụng abstract class để định nghĩa một giao diện tương tự. Giao diện được hiểu là một tập hợp các phương thức trừu tượng mà các lớp khác nhau có thể triển khai. Một lớp có thể triển khai nhiều interface bằng cách kế thừa từ các abstract class tương ứng.

## Định nghĩa và lí do sử dụng virtual environment:

#### Virtual environment (môi trường ảo) là một công cụ trong Python cho phép bạn tạo ra một môi trường cách biệt, độc lập với các môi trường khác trên cùng một hệ thống. Mỗi môi trường ảo có thể có các phiên bản khác nhau của Python và các gói cài đặt, thư viện riêng.

#### Lí do sử dụng virtual environment:

1. Đảm bảo sự cách biệt: Một môi trường ảo giúp bạn cách biệt các dự án, ứng dụng khác nhau. Bạn có thể cài đặt và quản lý các phiên bản Python, các gói cài đặt riêng cho từng dự án mà không ảnh hưởng đến các môi trường khác.

2. Quản lý các phụ thuộc: Khi phát triển phần mềm, các ứng dụng thường phụ thuộc vào các phiên bản cụ thể của các thư viện và gói phần mềm. Sử dụng môi trường ảo cho phép bạn quản lý và cài đặt các phiên bản phụ thuộc một cách độc lập cho từng dự án.

3. Dễ dàng chia sẻ: Bằng cách sử dụng môi trường ảo, bạn có thể chia sẻ các yêu cầu về phiên bản và phụ thuộc của dự án với người khác. Điều này giúp đảm bảo rằng môi trường cài đặt trên máy tính của bạn và máy tính của người khác là giống nhau.

#### Cách khởi tạo và sử dụng Python virtual environment

Python cung cấp một công cụ có tên là venv để tạo và quản lý các môi trường ảo. Dưới đây là các bước để khởi tạo và sử dụng Python virtual environment:

1. Mở Terminal hoặc Command Prompt.

2. Để tạo một môi trường ảo mới, chạy lệnh sau:
   python -m venv myenv

Trong đó, myenv là tên môi trường ảo của bạn. Bạn có thể đặt tên theo ý muốn.

3. Để kích hoạt môi trường ảo, chạy lệnh tương ứng với hệ điều hành của bạn:

Trên Windows:
myenv\Scripts\activate

Trên macOS và Linux:

source myenv/bin/activate

4. Khi môi trường ảo được kích hoạt, bạn sẽ thấy tên môi trường ảo hiển thị trước dấu nhắc lệnh.

#### Bây giờ, bạn có thể cài đặt và sử dụng các gói Python trong môi trường ảo này. Bất kỳ gói nào được cài đặt sẽ chỉ tồn tại trong môi trường ảo này và không ảnh hưởng đến các môi trường khác.

#### Để thoát khỏi môi trường ảo, bạn chỉ cần chạy lệnh sau:

deactivate

Sau đó, bạn sẽ trở lại môi trường Python chính.

- Các công cụ hỗ trợ xây dựng môi trường ảo pipenv:

Pipenv là một công cụ được sử dụng phổ biến để xây dựng và quản lý môi trường ảo trong Python. Nó kết hợp cả việc quản lý các gói phụ thuộc và môi trường ảo trong một công cụ đơn giản.

- Cách sử dụng Pipenv:

- Cài đặt Pipenv bằng pip:

pip install pipenv

1. Để tạo một môi trường ảo mới và tự động cài đặt các gói từ tệp requirements.txt (nếu có), chạy lệnh:

pipenv install

Để kích hoạt môi trường ảo, chạy lệnh:

2. pipenv shell

Bây giờ, bạn có thể sử dụng Python và các gói cài đặt trong môi trường ảo này.

3. Để thoát khỏi môi trường ảo, chạy lệnh:
   Copy code
   exit

4. Venv + pip là một cách truyền thống để tạo và quản lý môi trường ảo trong Python.

- Cách sử dụng venv + pip:

1. Tạo một môi trường ảo mới:

python -m venv myenv

2. Kích hoạt môi trường ảo:

Trên Windows:

myenv\Scripts\activate

Trên macOS và Linux:

source myenv/bin/activate

3. Cài đặt các gói từ tệp requirements.txt (nếu có):

pip install -r requirements.txt
Sử dụng Python và các gói trong môi trường ảo.

4. Thoát khỏi môi trường ảo:

deactivate

#### Cả hai công cụ Pipenv và venv + pip đều hỗ trợ xây dựng và quản lý môi trường ảo trong Python. Tuy nhiên, Pipenv cung cấp một giao diện dễ sử dụng hơn và tự động quản lý các gói phụ thuộc, trong khi venv + pip là cách truyền thống và đơn giản hơn. Tùy thuộc vào sở thích và yêu cầu của bạn, bạn có thể chọn công cụ phù hợp cho dự án của mình.
