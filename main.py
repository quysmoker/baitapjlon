import time
import schedule
from setup_driver import init_driver
from tra_cuu import tra_cuu




# Hàm thực hiện tra cứu
def run_task():
    print("⏳ Đang thực hiện tra cứu phương tiện vi phạm...")

    driver = init_driver()
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

    while True:
        result = tra_cuu(driver, "29H10026", loai_phuong_tien_index=0)
        if result in ("success", "not_found", "error"):
            break
        print("🔁 Đang thử lại với CAPTCHA mới...")
        time.sleep(2)

    print("✅ Đã hoàn thành tra cứu.")
    time.sleep(10)
    driver.quit()




# Hàm chờ đến thời gian
def wait_until_time(target_time):
    while time.strftime("%H:%M") != target_time:
        print(f"⏳ Chờ đến {target_time}, hiện tại: {time.strftime('%H:%M')}...")
        time.sleep(60)
    print(f"Đã đến giờ {target_time}. Chạy tác vụ...")




# Đặt lịch chạy tác vụ  
schedule.every().day.at("06:00").do(run_task)
schedule.every().day.at("12:00").do(run_task)





# Vòng lặp kiểm tra và chạy tác vụ
while True:
    wait_until_time("06:00")
    schedule.run_pending()
    wait_until_time("12:00")
    schedule.run_pending()
