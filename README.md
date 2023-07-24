# SQL Injection

## SQL Injection là gì?
SQL Injection là một kỹ thuật lợi dụng những lỗ hổng về câu truy vấn của các ứng dụng. Được thực hiện bằng cách chèn thêm một đoạn SQL để làm sai lệnh đi câu truy vấn ban đầu, từ đó có thể khai thác dữ liệu từ database. SQL injection có thể cho phép những kẻ tấn công thực hiện các thao tác như một người quản trị web, trên cơ sở dữ liệu của ứng dụng.

## Ví dụ thực tiễn SQL Injection

Ví dụ, trong form đăng nhập, người dùng nhập dữ liệu, trong trường tìm kiếm người dùng nhập văn bản tìm kiếm, trong biểu mẫu lưu dữ liệu, người dùng nhập dữ liệu cần lưu. Tất cả các dữ liệu được chỉ định này đều đi vào cơ sở dữ liệu.

Thay vì nhập dữ liệu đúng, kẻ tấn công lợi dụng lỗ hổng để insert và thực thi các câu lệnh SQL bất hợp pháp để lấy dữ liệu của người dùng… SQL Injection được thực hiện với ngôn ngữ lập trình SQL. SQL (Structured Query Language) được sử dụng để quản lý dữ liệu được lưu trữ trong toàn bộ cơ sở dữ liệu.

## Sự nguy hiểm của SQL Injection

- Hack tài khoản cá nhân.
- Ăn cắp hoặc sao chép dữ liệu của trang web hoặc hệ thống.
- Thay đổi dữ liệu nhạy cảm của hệ thống.
- Xóa dữ liệu nhạy cảm và quan trọng của hệ thống.
- Người dùng có thể đăng nhập vào ứng dụng với tư cách người dùng khác, ngay cả với tư cách quản trị viên.
- Người dùng có thể xem thông tin cá nhân thuộc về những người dùng khác, ví dụ chi tiết hồ sơ của người dùng khác, chi tiết giao dịch của họ,…
- Người dùng có thể sửa đổi cấu trúc của cơ sở dữ liệu, thậm chí xóa các bảng trong cơ sở dữ liệu ứng dụng.
- Người dùng có thể kiểm soát máy chủ cơ sở dữ liệu và thực thi lệnh theo ý muốn.

## Cơ sở dữ liệu quan hệ

Để hiểu rõ về SQLi, trước tiên, chúng ta sẽ nêu lại một chút về cơ sở dữ liệu quan hệ. Các cơ sở dữ liệu quan hệ và hệ sinh thái hỗ trợ cho chúng - các hệ quản trị cơ sở dữ liệu quan hệ (Relational Database Management Systems - RDBMS) đang phát triển rất mạnh. Tuy rằng chúng ta chỉ nói đến SQL injection một cách tổng quát, nhưng trên thực tế có nhiều khía cạnh liên quan của SQLi phụ thuộc vào đặc tính của RDBMS được sử dụng (ví dụ như Oracle Database, MySQL, MS SQL server, PostgreSQL, ...).

Chúng ta cần tìm hiểu thêm một chút về SQL. Những động từ sau đây là những động từ SQL phổ biến nhất và được hỗ trợ rộng rãi bởi các RDBMS:

- **SELECT** - truy vấn dữ liệu từ một bảng
- **INSERT** - thêm dữ liệu vào bảng
- **UPDATE** - chỉnh sửa dữ liệu đã có
- **DELETE** - xóa dữ liệu trong một bảng
- **DROP** - xóa một bảng
- **UNION** - ghép dữ liệu từ nhiều truy vấn với nhau

Tiếp theo chúng ta sẽ xét tới những từ khóa dùng để tùy chỉnh truy vấn hay gặp nhất trong SQL:

- **WHERE** - bộ lọc SQL được sử dụng khi có điều kiện đi kèm
- **AND/OR** - kết hợp với từ khóa WHERE để làm truy vấn cụ thể hơn
- **LIMIT #1, #2** - Giới hạn lượng dữ liệu trả về #2 bắt đầu từ vị trí #1 (Ví dụ LIMIT 3,2; sẽ trả về 2 dòng dữ liệu thứ 4 và 5.)
- **ORDER BY** - sắp xếp dữ liệu theo cột

Từ khóa **WHERE** được sử dụng ở khắp mọi nơi. Trên thực tế, vị trí từ khóa **WHERE** chính là nơi mà chúng ta dễ dàng tìm ra SQL injection nhất, vì đó là nơi mà dữ liệu đầu vào được cung cấp và tìm kiếm.

## Các ký tự đặc biệt trong SQL

Mỗi RDBMS có hệ thống các ký tự đặc biệt riêng cho các mục đích cụ thể. Tuy nhiên có những mục đích có thể có nhiều ký tự cùng được sử dụng.

![](https://images.viblo.asia/full/849b0172-7ff7-4a50-9650-25d60662ca5d.jpg)

## Phân loại các kiểu tấn công SQL Injection

![](https://images.viblo.asia/full/9cb0e7e8-ba42-4296-b4e4-cd8c5f7999e5.png)

SQL Injection có thể chia nhỏ thành các dạng sau

- In-band SQLi
   - Error-based SQLi
   - Union-based SQLi
- Inferential SQLi (Blind SQLi)
- Blind-boolean-based SQLi
   - Time-based-blind SQLi
- Out-of-band SQLi

### In-band SQLi

- Đây là dạng tấn công phổ biến nhất và cũng dễ để khai thác lỗ hổng SQL Injection nhất
- Xảy ra khi hacker có thể tổ chức tấn công và thu thập kết quả trực tiếp trên cùng một kênh liên lạc
- In-Band SQLi chia làm 2 loại chính:
  - Error-based SQLi
  - Union-based SQLi

##### Error-based SQLi

- Là một kỹ thuật tấn công SQL Injection dựa vào thông báo lỗi được trả về từ Database Server có chứa thông tin về cấu trúc của cơ sở dữ liệu.
- Trong một vài trường hợp, chỉ một mình Error-based là đủ cho hacker có thể liệt kê được các thuộc tính của cơ sở dữ liệu

![](https://images.viblo.asia/full/0b0b172a-4973-442c-b01c-affb3938e3b2.png)

##### Union-based SQLi

- Là một kỹ thuật tấn công SQL Injection dựa vào sức mạnh của toán tử UNION trong ngôn ngữ SQL cho phép tổng hợp kết quả của 2 hay nhiều câu truy vấn SELECTION trong cùng 1 kết quả và được trả về như một phần của HTTP response

![](https://images.viblo.asia/full/7b915ff5-7164-4be7-82ec-db06354fc2f3.png)

### Inferential SQLi (Blind SQLi)

- Không giống như In-band SQLi, Inferential SQL Injection tốn nhiều thời gian hơn cho việc tấn công do không có bất kì dữ liệu nào được thực sự trả về thông qua web application và hacker thì không thể theo dõi kết quả trực tiếp như kiểu tấn công In-band.
- Thay vào đó, kẻ tấn công sẽ cố gắng xây dựng lại cấu trúc cơ sở dữ liệu bằng việc gửi đi các payloads, dựa vào kết quả phản hồi của web application và kết quả hành vi của database server.
- Có 2 dạng tấn công chính
   - Blind-boolean-based
   - Blind-time-based SQLi

### Blind-boolean-based

- Là kĩ thuật tấn công SQL Injection dựa vào việc gửi các truy vấn tới cơ sở dữ liệu bắt buộc ứng dụng trả về các kết quả khác nhau phụ thuộc vào câu truy vấn là True hay False.
- Tuỳ thuộc kết quả trả về của câu truy vấn mà HTTP reponse có thể thay đổi, hoặc giữ nguyên.
- Kiểu tấn công này thường chậm (đặc biệt với cơ sở dữ liệu có kích thước lớn) do người tấn công cần phải liệt kê từng dữ liệu, hoặc mò từng kí tự.

![](https://images.viblo.asia/full/a6bb8f4e-e2d1-4577-8e6b-4ad27ee9e177.png)

##### Time-based Blind SQLi

- Time-base Blind SQLi là kĩ thuật tấn công dựa vào việc gửi những câu truy vấn tới cơ sở dữ liệu và buộc cơ sở dữ liệu phải chờ một khoảng thời gian (thường tính bằng giây) trước khi phản hồi.
- Thời gian phản hồi (ngay lập tức hay trễ theo khoảng thời gian được set) cho phép kẻ tấn công suy đoán kết quả truy vấn là TRUE hay FALSE.
- Kiểu tấn công này cũng tốn nhiều thời gian tương tự như Boolean-based SQLi.

### Out-of-band SQLi

- Out-of-band SQLi không phải dạng tấn công phổ biến, chủ yếu bởi vì nó phụ thuộc vào các tính năng được bật trên Database Server được sở dụng bởi Web Application.
- Kiểu tấn công này xảy ra khi hacker không thể trực tiếp tấn công và thu thập kết quả trực tiếp trên cùng một kênh (In-band SQLi), và đặc biệt là việc phản hồi từ server là không ổn định.
- Kiểu tấn công này phụ thuộc vào khả năng server thực hiện các request DNS hoặc HTTP để chuyển dữ liệu cho kẻ tấn công.
Ví dụ như câu lệnh xp_dirtree trên Microsoft SQL Server có thể sử dụng để thực hiện DNS request tới một server khác do kẻ tấn công kiểm soát, hoặc Oracle Database’s UTL HTTP Package có thể sử dụng để gửi HTTP request từ SQL và PL/SQL tới server do kẻ tấn công làm chủ.

## Cách SQL Injection hoạt động

Có nhiều kiểu tấn công bằng SQL Injection tuỳ thuộc vào Database Engine. Trước tiên mình sẽ giới thiệu về các thức tấn công thông qua Dynamic SQL Statement. Dynamic SQL Statement là câu lệnh SQL được tạo ra trong quá trình chạy chương trình với các parameters được truyền vào tự động thông qua một form của website.
Bạn có thể xem một đoạn code đơn gian bằng PHP mô tả môt form đăng nhập hệ thống ở dưới đây:

```html
<form action='signin.php' method="post">

        <input type="email" name="email" required="required"/>

        <input type="password" name="password"/>

        <input type="submit" value="Submit"/>

</form>
```

Người dùng nhập vào địa chỉ Email, mật khẩu và submit lên signin.php.
Giả sử trong file PHP signin.php xử lý logic như sau:

```php
SELECT * FROM leo.users WHERE email = '$_POST['email']' AND password = 'md5($_POST['password'])';
```

Đoạn mã trên thực hiện việc truy vấn dữ liệu từ bảng users với điều kiện là emai và password là những giá trị nhập vào từ form phía trên.

OK! mình đã xây dựng một chương trình để test, dù bạn không biết thông tin đăng nhập nhưng bạn cũng có thể dễ dàng vượt qua theo cách:
Mở Link dưới đây:
http://leo.890m.com/test/login.html
Nhập vào ô email với nội dụng: em@khongbiet.com' OR 1 = 1 LIMIT 1 -- ' ]
Nhập vào ô password với nội dụng bất kỳ, sau đó click vào nut Login.

![](https://labs.flinters.vn/wp-content/uploads/2016/05/Screen-Shot-2016-05-26-at-3.46.24-PM.png)

Awesome! chúng ta đã đăng nhập thành công.

Bây giờ mình sẽ giải thích cho các bạn nguyên nhân chúng ta có thể dễ dàng đăng nhập vào hệ thống mà thậm chí chúng ta không có thông tin đăng nhập.
Khi đăng nhập hệ thống, chương trình sẽ tự động tạo ra cậu lệnh truy vấn dữ liệu với tham số được truyền vào từ form login:

```php
SELECT * FROM leo.users WHERE email = $_POST['email'] AND password = md5($_POST['password']);
```

Với dữ liệu chúng ta vừa nhập, câu lệnh truy vấn sẽ là:

```php
SELECT * FROM leo.users WHERE email = 'em@0biet.com' OR 1 = 1 LIMIT 1 -- ' ]' AND password = 'em_biet_tuot';
```

Sau kỹ tự “--“, hệ thống sẽ hiểu đó là comment, chương trình sẽ không thực thi những gì phía sau nó. Câu truy vấn có thể rút gọn lại:

```php
SELECT * FROM leo.users WHERE email = 'em@0biet.com' OR 1 = 1 LIMIT 1
```

Điều kiện của câu lệnh truy vấn: **email = ’em@0biet.com’ OR 1 = 1**, nó luôn là **true**, đó là lý do vì sao chúng ta có thể vượt qua màn hình đăng nhập một cách dễ dàng.

Chúng ta cùng thử chạy câu lệnh truy vấn trên thông qua công cụ online rất tuyệt đó là sqlfiddle, các bạn có thể mở link mình đã làm để tham khảo http://sqlfiddle.com/#!9/c09905

![](https://labs.flinters.vn/wp-content/uploads/2016/05/Screen-Shot-2016-05-26-at-4.49.31-PM.png)

Đầu tiên chúng ta sẽ tạo bảng users thông qua cậu lệnh:

```SQL
CREATE TABLE `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(100) NULL,
    `password` VARCHAR(50) NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `users` (`email`, `password`) VALUES ('leo@g.com', md5('abc'));
```
Các bạn copy đoạn mã trên vào cột bên trái, sau đó click vào button **Build Schema**.
Tiếp theo ở cột bên phải chúng ta viết câu lệnh lấy toàn bộ dữ liệu từ table user:

```SQL
SELECT * FROM leo.users WHERE email = 'em@0biet.com' OR 1 = 1 LIMIT 1 -- ' ] AND password = 'em_biet_tuot';
```

HomeSecurityTìm hiểu SQL Injection qua ví dụ cụ thể
Tìm hiểu SQL Injection qua ví dụ cụ thểMay 26, 2016
sql-ịnection

Với yêu cầu từ các dự án của công ty, một trong những điểm bắt buộc trước khi release dự án là phải PASS qua “Security Testing”. Mình sẽ viết một loạt bài giới thiệu cũng như hướng dẫn thực hiện Security Testing, đồng thời chỉ ra cách thức để ngăn ngừa.

Trong bài viết này mình sẽ giới thiệu về SQL Injection, đây là một trong những kỹ thuật cơ bản mà Hacker thường xử dụng để tấn công vào website họ muốn. SQL Injection tận dụng sử lỏng lẻo về thiết kế của các website để thực hiện các truy vấn mang tính chất phá hoại.

SQL Injection là gì?
SQL viết tắt của Structured Query Language, nó được sử dụng để truy vấn, thao tác dữ liệu trong Database. SQL Injection là kỹ thuật tấn công nhằm biến các điều kiện trong câu lệnh SQL (SQL Statement) là luôn luôn đúng. (Vẫn hơi khó hiểu nhỉ ^^, các bạn sẽ hiểu rõ hơn ở phần example)

How to SQL Injection Works?
Có nhiều kiểu tấn công bằng SQL Injection tuỳ thuộc vào Database Engine. Trước tiên mình sẽ giới thiệu về các thức tấn công thông qua Dynamic SQL Statement. Dynamic SQL Statement là câu lệnh SQL được tạo ra trong quá trình chạy chương trình với các parameters được truyền vào tự động thông qua một form của website.
Bạn có thể xem một đoạn code đơn gian bằng PHP mô tả môt form đăng nhập hệ thống ở dưới đây:

<form action='signin.php' method="post">

        <input type="email" name="email" required="required"/>

        <input type="password" name="password"/>

        <input type="submit" value="Submit"/>

</form>
Người dùng nhập vào địa chỉ Email, mật khẩu và submit lên signin.php.
Giả sử trong file PHP signin.php xử lý logic như sau:

SELECT * FROM leo.users WHERE email = '$_POST['email']' AND password = 'md5($_POST['password'])';
Đoạn mã trên thực hiện việc truy vấn dữ liệu từ bảng users với điều kiện là emai và password là những giá trị nhập vào từ form phía trên.

OK! mình đã xây dựng một chương trình để test, dù bạn không biết thông tin đăng nhập nhưng bạn cũng có thể dễ dàng vượt qua theo cách:
Mở Link dưới đây:
http://leo.890m.com/test/login.html
Nhập vào ô email với nội dụng: em@khongbiet.com’ OR 1 = 1 LIMIT 1 — ‘ ]
Nhập vào ô password với nội dụng bất kỳ, sau đó click vào nut Login.

Screen Shot 2016-05-26 at 3.46.24 PM

Awesome! chúng ta đã đăng nhập thành công.

Bây giờ mình sẽ giải thích cho các bạn nguyên nhân chúng ta có thể dễ dàng đăng nhập vào hệ thống mà thậm chí chúng ta không có thông tin đăng nhập.
Khi đăng nhập hệ thống, chương trình sẽ tự động tạo ra cậu lệnh truyên vấn dữ liệu với tham số được truyền vào từ form login,

SELECT * FROM leo.users WHERE email = $_POST['email'] AND password = md5($_POST['password']);
Với dữ liệu chúng ta vừa nhập, câu lệnh truy vấn sẽ là:

SELECT * FROM leo.users WHERE email = 'em@0biet.com' OR 1 = 1 LIMIT 1 -- ' ]' AND password = 'em_biet_tuot';
Sau kỹ tự “–“, hệ thống sẽ hiểu đó là comment, chương trình sẽ không thực thi những gì phía sau nó. Câu truy vấn có thể rút gọn lại:

SELECT * FROM leo.users WHERE email = 'em@0biet.com' OR 1 = 1 LIMIT 1
Điều kiện của câu lệnh truy vấn: email = ’em@0biet.com’ OR 1 = 1, nó luôn là true, đó là lý do vì sao chúng ta có thể vượt qua màn hình đăng nhập một cách dễ dàng.

Chúng ta cùng thử chạy câu lệnh truy vấn trên thông qua công cụ online rất tuyệt đó là sqlfiddle, các bạn có thể mở link mình đã làm để tham khảo http://sqlfiddle.com/#!9/c09905

Screen Shot 2016-05-26 at 4.49.31 PM
Đầu tiên chúng ta sẽ tạo bảng users thông qua cậu lệnh:

CREATE TABLE `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(100) NULL,
    `password` VARCHAR(50) NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `users` (`email`, `password`) VALUES ('leo@g.com', md5('abc'));
Các bạn copy đoạn mã trên vào cột bên trái, sau đó click vào button Build Schema.
Tiếp theo ở cột bên phải chúng ta viết câu lệnh lấy toàn bộ dữ liệu từ table user:

SELECT * FROM leo.users WHERE email = 'em@0biet.com' OR 1 = 1 LIMIT 1 -- ' ] AND password = 'em_biet_tuot';

Click vào nút **Run SQL**, các bạn sẽ thấy dữ liệu mà chúng ta vừa thêm vào ở table phía dưới.

Ngoài cách tấn công trên, Hacker còn có thể sử dụng SQL Injection để thực hiện các hình thức phá hoại như:
- Xoá dữ liệu
- Cập nhật thay đổi dữ liệu
- Thêm mới dữ liệu vào hệ thống
- Thực hiện các commands trên server để tự động tải và cài đặt những phần mềm nguy hiểm hay virus.
- Lấy thông tin của khách hàng trên hệ thống như thông tin thẻ ngân hàng, thông tin đăng nhập.
