# 🚦 Tra Cứu Vi Phạm Giao Thông Tự Động

Một công cụ Python giúp **tự động tra cứu vi phạm giao thông** từ trang web của cơ quan chức năng bằng cách sử dụng **Selenium** để tự động điều khiển trình duyệt và **OCR (pytesseract + OpenCV)** để giải mã CAPTCHA.

---

## 📌 Tính năng chính

- Tự động mở trình duyệt và truy cập trang tra cứu.
- Nhập biển số xe, loại xe và mã captcha.
- Giải mã CAPTCHA bằng OCR.
- Tự động lấy và hiển thị kết quả vi phạm (nếu có).
- Hỗ trợ chạy định kỳ theo thời gian cài sẵn.

---

## 🛠 Công nghệ sử dụng

- **Python 3**
- [Selenium](https://www.selenium.dev/) – Điều khiển trình duyệt tự động
- [pytesseract](https://github.com/madmaze/pytesseract) – Nhận dạng chữ từ ảnh CAPTCHA
- [OpenCV](https://opencv.org/) – Xử lý ảnh CAPTCHA
- [schedule](https://pypi.org/project/schedule/) – Lập lịch chạy định kỳ
- `time`, `re`, `cv2`, ...

---

## 📂 Cấu trúc dự án

├── giai_ma_captcha.py # Hàm giải mã CAPTCHA từ ảnh

├── setup_driver.py # Cấu hình và khởi tạo WebDriver (Chrome)

├── tra_cuu.py # Chức năng tra cứu vi phạm

├── main.py # File chạy chính

├── README.md # Tài liệu hướng dẫn sử dụng

├── requirements.txt # Danh sách thư viện cần cài


---

## 🚀 Hướng dẫn cài đặt và sử dụng



1. Cài đặt thư viện cần thiết
    ```bash
    pip install -r requirements.txt
2. Cài đặt Tesseract OCR
    ```bash
    🔧 Trên Windows
    Tải và cài từ: https://github.com/tesseract-ocr/tesseract
    Sau khi cài xong, cập nhật đường dẫn trong code:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    🐧 Trên Linux
    sudo apt update
    sudo apt install tesseract-ocr
3. Chạy chương trình
    ```bash
        python main.py
⚠️ Lưu ý
Không nên gửi quá nhiều yêu cầu liên tục để tránh bị chặn IP.
CAPTCHA có thể thay đổi định dạng, cần điều chỉnh thuật toán xử lý ảnh nếu lỗi.


📧 Thông tin liên hệ
Tác giả: Hồ Văn Quý
Email: vanquyh181@gmail.com
GitHub: https://github.com/quysmoker
