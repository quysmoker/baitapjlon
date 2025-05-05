import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from giai_ma_captcha import giai_ma_captcha




def tra_cuu(driver, bien_so, loai_phuong_tien_index=0):
    license_plate_input = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[1]/input')
    license_plate_input.clear()
    license_plate_input.send_keys(bien_so)

    vehicle_type_dropdown = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[2]/select')
    select = Select(vehicle_type_dropdown)
    select.select_by_index(loai_phuong_tien_index)

    captcha_text = giai_ma_captcha(driver)
    print("🔐 CAPTCHA nhận được là:", captcha_text)

    captcha_input = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[3]/div/input')
    captcha_input.clear()
    captcha_input.send_keys(captcha_text)

    submit_button = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/input[1]')
    submit_button.click()

    time.sleep(10)

    try:
        alert = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[4]')
        if "Mã xác nhận sai" in alert.text:
            print("❌ Mã captcha sai. Đang tải lại trang để thử lại...")
            driver.refresh()
            return "retry"
    except:
        pass

    try:
        not_found_div = driver.find_element(By.XPATH, '//*[@id="bodyPrint123"]/div')
        if "Không tìm thấy kết quả" in not_found_div.text:
            print("📭 Không tìm thấy kết quả vi phạm.")
            return "not_found"
    except:
        pass

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "bodyPrint123"))
        )
        form_groups = driver.find_elements(By.XPATH, '//div[@id="bodyPrint123"]//div[@class="row"]')

        # Chỉ lấy "Hành vi vi phạm" và "Trạng thái"
        for group in form_groups:
            try:
                label = group.find_element(By.XPATH, './label/span').text.strip()
                if label == "Hành vi vi phạm:":
                    behavior = group.find_element(By.XPATH, './div[@class="col-md-9"]').text.strip()
                    print(f"Hành vi vi phạm: {behavior}")
                elif label == "Trạng thái:":
                    status = group.find_element(By.XPATH, './div[@class="col-md-9"]/span').text.strip()
                    print(f"Trạng thái: {status}")
            except Exception as e:
                print(f"⚠️ Lỗi khi lấy dữ liệu: {str(e)}")
        return "success"
    
    except Exception as e:
        print("⚠️ Gặp lỗi khi xử lý dữ liệu:", str(e))
        return "error"
