## Package là gì?

Chẳng hạn như bạn muốn dùng application nào đó. Vì ngày xưa chỉ được cung cấp source code thôi, cho nên cần compile. Tuy nhiên, chỉ như thế thì không đủ, nên cần phải cung cấp cả code binary đã compile lại và nhóm những file liên quan.

Chúng ta gọi nhóm file đã tập hợp lại là Package.

Sẽ thật không tốt nếu chúng ta nghĩ package là thứ gì đó giống như zip. Chúng ta không giải nén package rồi tự mình bố trí nó. Chúng ta có thể tiến hành install/uninstall package bằng application có thể xử lý nó

Trong CentOS thì chúng ta xử lý package bằng command là rpm.

RPM Package Hình thức của package sẽ khác nhau dựa trên distribution của Linux

Dựa theo Wikipedia:

- RPM: Nhóm Red Hat (CentOS chẳng hạn)
- deb : Dùng cho Debian (Có cả Ubuntu )
- ports : FreeDSB
- pkg : Solaris

Như pkg thì installer của Mac sẽ nhận thấy đây là pkg nhưng có phải là cùng 1 thứ không thì không phán đoán rõ ràng được.

Cho nên nói về RMP package thì tạm thời chỉ nói về cái mà tôi đang dùng là CentOS nên sẽ là Package dành cho CentOS Đuôi là `.rpm` ( là chuỗi kí tự tùy ý)

Ngoài ra, package có quy tắc đặt tên. Có vẻ là [ Tên OS - CPU - số bit ]

Package của format source code ？

Như đã nói ở trên, rpm là file binary của application và các loại file cần cho việc chạy file binary đó.

Cho nên tôi cũng không hiểu rõ ý nghĩa của cụm từ [ package của hình thức source code] nhưng khi đọc giải thích về nó thì tôi thấy khái niệm [SPRM(Source package)] trong phần giải thích đó.

Extension là 「*.src.rpm」

Chúng ta có thể hiểu cái này là 1 khái niệm khác so với RPM package. SPRM tức là source dùng cho việc tạo RPM package, thông qua việc build SPRM mà có thể tạo RPM package.

Tóm lại

・Package là file gồm binary của application và những thứ cần để chạy nó ・Package của Linux thuộc nhóm Red Hat thì chủ yếu là được bố trí như là [RPM Package] ・RPM Package thì có thể install/ uninstall bằng rpm command ・SRPM là source code để chế tạo RPM package

Về quản lý package Khái quát Tiếp theo tôi sẽ giải thích về package mà Linux Distribution thuộc nhóm Red Hat. Tôi cũng sẽ tổng hợp về command rpm dùng để xử lý RPM package

rpm là viết tắt của RedHat Package Manager

## Package management

Package management là một phương thức nhằm cài đặt và bảo trì các phần mềm được cài đặt trong hệ thống. Mỗi một bản phân phối Linux lại có một hệ thống phân phối package riêng được gọi là packaging system.

Các thành phần cơ bản trong packaging system đó là:

- `Package files`: đơn vị cơ bản nhất của một package và được quản lý bởi maintainer, là một dạng file compressed chứa tất cả thông tin cần thiết để cài đặt chương trình.

- `Repositories`: Một nơi tập trung chứa các package files, một distribution có thể có một vài repositories khác nhau phục vụ nhiều mục đích khác nhau, hoặc phục vụ cho từng quá trình phát trình phần mềm (repository cho quá trình test,...).

- `Dependencies`: Một package thì rất it khi mang tính standalone mà nó thường được xây dựng dựa trên các package khác, cũng giống như khi các bạn lập trình, khi cài đặt sử dụng một thư viện thì thư viện đó đều xây dựng dựa trên một thư viện khác, các thư viện khác đó gọi là dependencies.

Có hai loại packaging system phổ biến nhất là Debian và RedHat:

| Packaging system | Distributions |
|--------------|-----------|
| Debian-style (.deb) | Debian, Ubuntu, Linux Mint, Raspbian |
| Red Hat–style (.rpm) | Fedora, CentOS, Red Hat Enterprise Linux, OpenSUSE  |

Packaging system thì được chia ra làm hai loại công cụ, gọi là high và low level package tools:

- `Low-level package tool` sẽ chịu trách nhiệm cho các tác vụ như là install, và remove package files.

- `High-level package tool` xử lý các tác vụ liên quan đến tìm kiếm thông tin metadata và cài đặt dependencies.

Các công cụ package tool được liệt kê trong bảng sau:

| Distributions | Low-level tool | High-level tool |
| ------------- | -------------- | --------------- |
| Debian-style  | dpkg           | apt-get, apt, aptitude |
|Fedora, Red Hat Enterprise Linux, CentOS|rpm|yum,dnf|

## Một vài câu lệnh thường dùng

- Tìm kiếm package trên repository:
    Sử dụng high-level packaging tool để tìm kiếm thông tin ở metadata của repo, một package có thể xác định bằng tên package, hoặc description của nó:

    |Packaging system|Command|
    | :--------------: | ----- |
    |Debian|apt-cache search <search_string>|
    |ReaHat|yum search <search_string>|

- Cài đặt package từ repository:
    Một lệnh quá quen thuộc với người dùng Linux, dùng để cài đặt package hay chương trình từ repo, lệnh này cũng sẽ auto cài đặt các dependency cần thiết cho chương trình.

    |Packaging system | Command|
    |:--------------: | -------|
    |Debian | apt-get install package_name|
    |RedHat|yum install package_name|

- Cài đặt package từ package file:
    Một lệnh khác cũng được sử dụng để cài đặt chương trình hoặc package từ package file đã được download sẵn về máy, tuy nhiên lệnh low-level không có dependency resolution nên nó sẽ không auto cài đặt các dependencies cần thiết. Đôi khi gây ra thiếu sót khi ta down bị thiếu, làm cho chương trình không chạy hoặc chạy không đúng.

    | Packaging system | Command |
    |:---------------: | ------- |
    | Debian | dpkg -i package_file |
    | RedHat |rpm -i package_file |

- Remove package

    |Packaging system|Command|
    |:---------------|-------|
    |Debian|apt-get remove package_name|
    ||apt-get purge package_name|
    ||dpkg -P package_file|
    |RedHat|yum erase package_name|

    Nhiều người thường hay gặp vấn đề về việc muốn reinstall một package, xảy ra khi họ muốn xóa hết toàn bộ một package rồi install lại nhưng khi install lại thì lại gặp lỗi y hệt lần cài đặt trước do các file config vẫn giữ y hệt lúc họ remove. Một số cách có thể hữu ích trên Ubuntu.

    remove package cùng với các dependencies liên quan của nó.

    ```sh
    apt-get remove package_name
    ```

    cũng như câu trên nhưng đồng thời xóa cả những file config liên quan, trừ những file tại user's home.

    ```sh
    apt-get purge package_name
    ```

    cũng như câu purge của tool apt-get nhưng vì là low-level tool nên nó không remove những dependency liên quan.

    ```sh
    dpkg -P package_file
    ```

    Ngoài ra, có một lệnh khác liên quan tới remove của high-level tool đó là `apt-get autoremove` sử dụng để remove những package là dependency của package khác, nhưng do trong quá trình update không còn cần sử dụng tới nữa nên sẽ được loại bỏ khi chạy lệnh này.

- Update package từ repository

    Lệnh sau sử dụng để update cùng lúc tất cả các package trong system với version mới nhất trên repo.

    |Packaging system|Command|
    |:--------------:|-------|
    |Debian|apt-get upgrade|
    |RedHat|yum update|

- Upgrade package từ file system

    Đối với những package đã download sẵn file package chứa version mới nhất về máy, ta có thể chạy lệnh low-level sau để update

    |Packaging system|Command|
    |:--------------:|-------|
    |Debian|dpkg -i package_file|
    |RedHat|rpm -U package_file|


- Liệt kê package

    Lệnh sau được sử dụng để liệt kê các package đã được cài đặt trong hệ thống

    |Packaging system|Command|
    |:--------------:|-------|
    |Debian|dpkg --list|
    |RedHat|rpm -qa|


- Xác định package đã được install chưa

    |Packaging system|Command|
    |:--------------:|-------|
    |Debian|dpkg -s package_name|
    |RedHat|rpm -q package_name|

- Hiển thị thông tin của package đã được install

    |Packaging system|Command|
    |:--------------:|-------|
    |Debian|apt-cache show package_name|
    |RedHat|yum info package_name|

- Tìm xem package nào đã cài đặt một file bất kỳ nào đó.

    |Packaging system|Command|
    |:--------------:|-------|
    |Debian|dpkg -S file_name|
    |RedHat|rpm -qf file_name|

- Như vậy là với bài viết ngắn ngủi này, chúng ta đã làm quen được với công cụ package management và một số lệnh cơ bản thường dùng với nó

## Repository hay còn gọi là Repo

- dịch ra tiếng Việt có nghĩa là kho, đây chính là nơi chứa tất cả mã nguồn, các ứng dụng cho một dự án mã nguồn mở nói chung (như Git, Linux,...). Bạn cũng có thể hiểu một cách khác là Repository chính khai báo thư mục chứa dự án của bạn trên local hoặc remote.

- Có lại loại repository đó là local repositoryvà remote repository.

  - Local repository: Là repo được cài đặt trên máy tính của lập trình viên, repo này sẽ đồng bộ hóa với remote repo bằng các lệnh quản lý.
  - Remote repository: Là repo được cài đặt trên server chuyên dụng, điển hình hiện nay là Github.

Vì repository là tập hợp các gói như vậy nên người dùng có thể tìm và tải xuống gói mình cần trong các kho này. Bạn có thể tìm thấy hầu hết mọi công cụ bạn cần ở đây.

Ngoài ra, các bản phân phối Linux khác nhau có bộ repository riêng. Trên Ubuntu, những repository mặc định sẽ thuộc về chính Ubuntu. Ngoài ra, người dùng cũng có thể thêm bất kỳ repository nào khác bằng cách sử dụng lệnh `add-apt-repository`.

Để cài đặt các gói trên Ubuntu, bạn nên sử dụng các repository chính thức, do các gói bạn tìm thấy trong các kho này được phát triển đặc biệt cho Ubuntu. Ngoài ra, các bản cập nhật thường xuyên do các nhà phát triển đẩy ra đảm bảo phần mềm hoạt động bình thường

## Các loại repository trong Ubuntu

Ubuntu có bốn loại repository khác nhau: Main, Restricted, Universe, and Multiverse. Một số trong đó, ví dụ như Main, được mở theo mặc định. Nhưng đối với những loại khác, bạn phải bật universe và multiverse trước khi có thể bắt đầu tải các gói từ chúng.

### Main (chính)

Main bao gồm phần mềm và các gói được hỗ trợ đầy đủ bởi đội ngũ Ubuntu. Nếu bạn đã cài đặt phần mềm từ Main repository, Ubuntu sẽ thường xuyên cung cấp cho bạn các bản cập nhật bảo mật và sửa lỗi cho các gói đó.

Kho này bao gồm các gói mã nguồn mở mà người dùng có thể tự do sử dụng và phân phối lại. Ngoài ra, bạn sẽ thấy rằng Ubuntu đi kèm với hầu hết các gói trong Main repository vì chúng là những tiện ích quan trọng được yêu cầu bởi hệ thống cũng như người dùng.

### Restricted (Hạn chế)

Mặc dù bạn có thể sử dụng miễn phí phần mềm có sẵn trong Kho lưu trữ Restricted theo giấy phép miễn phí (free license), nhưng bạn không thể phân phối lại các gói này. Kho lưu trữ này bao gồm các công cụ và trình điều khiển cần thiết cho hoạt động bình thường của hệ điều hành.

Đội ngũ Ubuntu không cung cấp hỗ trợ cho các chương trình như vậy vì chúng thuộc về một tác giả khác. Ngoài ra, Canonical, công ty chịu trách nhiệm quản lý Ubuntu, không thể sửa đổi gói này vì hầu hết phần mềm có trong repository Restricted là độc quyền.

### Universe (vũ trụ)

Universe chứa mọi gói mã nguồn mở được phát triển cho hệ điều hành Linux. Các gói này không được quản lý trực tiếp bởi nhóm Ubuntu. Cộng đồng các nhà phát triển làm việc trên một gói hoàn toàn chịu trách nhiệm đẩy các bản cập nhật và sửa lỗi bảo mật.

Tuy nhiên, Ubuntu có thể chuyển gói từ Universe sang Main nếu các nhà phát triển đồng ý tuân theo các tiêu chuẩn cụ thể do họ đặt ra.

### Multiverse (đa vũ trụ)

Mặc dù các repository được đề cập ở trên chứa các gói sử dụng miễn phí hoặc mã nguồn mở, multiverse bao gồm phần mềm không miễn phí. Các chương trình độc quyền không có các vấn đề pháp lý cũng được đưa vào Multiverse.

Việc cài đặt các gói từ repository này không được khuyến khích vì rủi ro đáng kể liên quan đến các chương trình này.

Tham khảo tại:

<https://viblo.asia/p/cac-cau-lenh-linux-phan-7-mot-so-tac-vu-va-mot-so-cong-cu-co-ban-package-management-Do754DB05M6>

<https://funix.edu.vn/chia-se-kien-thuc/huong-dan-cho-nguoi-moi-bat-dau-ve-kho-phan-mem-repository-trong-ubuntu/#:~:text=Tr%C3%AAn%20Ubuntu%20v%C3%A0%20c%C3%A1c%20h%E1%BB%87%20%C4%91i%E1%BB%81u%20h%C3%A0nh%20d%E1%BB%B1a,th%E1%BB%83%20c%C3%A0i%20%C4%91%E1%BA%B7t%20tr%C3%AAn%20h%E1%BB%87%20th%E1%BB%91ng%20c%E1%BB%A7a%20m%C3%ACnh.>

## Repo của redhat

>Lưu ý: lệnh `yum` đã ngừng hỗ trợ trên CentOS 8 và chuyển dịch dần sang dùng câu lệnh `dnf`, cũng gần tương tự như lệnh `yum`

- Tìm kiếm các repo có sẵn

```sh
yum repolist all
```

- Hiển thị tất cả Group Packages

Trong Linux thì số lượng các package sẽ được đưa vào một nhóm cụ thể. Ví dụ nhóm Installed Group sẽ chứa những package đã cài đặt, nhóm Available Groups sẽ chứa những package có sẵn để cài đặt.

Lệnh sau sẽ hiển thị những nhóm đó.

```sh
yum grouplist
```

Giả sử bạn cần cài đặt tất cả những package nằm trong nhóm Available Group thì chạy lệnh sau.

```sh
yum groupinstall 'Available Group'
```

Bạn muốn update các package nằm trong nhóm đó thì chạy lệnh.

```sh
# yum groupupdate 'Available Group'
```

Bạn muốn xóa tất cả package trong group thì chạy lệnh.

```sh
# yum groupremove 'Available Group'
```

- Cài đặt package ở repo bị disabled

Để cài đặt một package nằm trong repo nào đó thì bạn có thể sử dụng lệnh này. Như ví dụ dưới đây mình cần cài đặt package tên là phpmyadmin nằm trong repo epel. Thường thì chỉ cài được các repo có sẵn, nếu như không cấu hình thêm

```sh
yum --enablerepo=epel install phpmyadmin
```

<https://rhel.pkgs.org/>






