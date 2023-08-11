# Blind SQL injection with time delays

Bài lab này yêu cầu ta khai thác lỗ hổng SQL injection để gây ra độ trễ 10s

Sau một hồi mò mẫm thì mình biết được trang web sử dụng **PostgreSQL** nhưng mình thử payload `' SELECT pg_sleep(10)` thì không được, xem người khác làm thì học dùng cái này:

**`'||pg_sleep(10)--`**
Trong ngôn ngữ SQL, dấu "||" được sử dụng để nối các chuỗi ký tự. Trong trường hợp này, chuỗi ký tự "pg_sleep(10)" được nối vào chuỗi ký tự trước đó, với ý nghĩa là thực hiện một hàm pg_sleep() trong hệ quản trị cơ sở dữ liệu PostgreSQL với đối số là 10 giây.