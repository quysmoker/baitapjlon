import time
import schedule
from setup_driver import init_driver
from tra_cuu import tra_cuu

# Hàm thực hiện tra cứu
def run_task():
    print("⏳ Đang thực hiện tra cứu phương tiện vi phạm...")

    # 1. Vào website đã chọn.
    driver = init_driver()
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

    # 2. Nhập các thông tin Biển số xe, chọn loại phương tiện, nhập mã bảo mật, bấm tìm kiếm.
    while True:
        result = tra_cuu(driver, "29H10024", loai_phuong_tien_index=0)
        if result in ("success", "not_found", "error"):
            break
        print("🔁 Đang thử lại với CAPTCHA mới...")
        time.sleep(2)

    # 3. Kiểm tra kết quả phạt nguội.
    print("✅ Đã hoàn thành tra cứu.")
    time.sleep(10)
    driver.quit()

# 4. Set lịch chạy 6h sáng và 12h trưa hằng ngày.
schedule.every().day.at("06:00").do(run_task)
schedule.every().day.at("12:00").do(run_task)

# Vòng lặp chính chạy liên tục và kiểm tra lịch
print("📅 Đang chạy lịch trình tra cứu... (Ctrl + C để dừng)")
while True:
    schedule.run_pending()
    time.sleep(30)  # Kiểm tra lịch mỗi 30 giây
