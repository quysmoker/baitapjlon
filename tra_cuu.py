import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from giai_ma_captcha import giai_ma_captcha

def tra_cuu(dieu_khien, bien_kiem_soat, phuong_tien=0):
    # Nhập biển số xe
    bien_so = dieu_khien.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[1]/input')
    bien_so.clear()
    bien_so.send_keys(bien_kiem_soat)

    # Chọn loại phương tiện 
    danh_sach_phuong_tien = dieu_khien.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[2]/select')
    chon = Select(danh_sach_phuong_tien)
    chon.select_by_index(phuong_tien)

    # Nhận và nhập mã captcha
    ma_captcha = giai_ma_captcha(dieu_khien)
    print("CAPTCHA nhận được là:", ma_captcha)
    captcha_input = dieu_khien.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[3]/div/input')
    captcha_input.clear()
    captcha_input.send_keys(ma_captcha)

    # Nhấn nút tìm kiếm
    tim_kiem = dieu_khien.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/input[1]')
    tim_kiem.click()
    time.sleep(10)

    # Kiểm tra mã xác nhận
    try:
        thong_bao = dieu_khien.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[4]')
        if "Mã xác nhận sai" in thong_bao.text:
            print("Mã captcha sai. Đang tải lại trang để thử lại...")
            dieu_khien.refresh()
            return "retry"
    except:
        pass

    try:
        khong_tim_thay = dieu_khien.find_element(By.XPATH, '//*[@id="bodyPrint123"]/div')
        if "Không tìm thấy kết quả" in khong_tim_thay.text:
            print("Không tìm thấy kết quả vi phạm.")
            return "not_found"
    except:
        pass

    try:
        WebDriverWait(dieu_khien, 15).until(
            EC.presence_of_element_located((By.ID, "bodyPrint123"))
        )
        bien_ban_vi_pham = dieu_khien.find_elements(By.XPATH, '//div[@id="bodyPrint123"]//div[@class="row"]')

        # Lấy thông tin vi phạm
        for nhom in bien_ban_vi_pham:
            try:
                nhan = nhom.find_element(By.XPATH, './label/span').text.strip()
                if nhan == "Hành vi vi phạm:":
                    hanh_vi = nhom.find_element(By.XPATH, './div[@class="col-md-9"]').text.strip()
                    print(f"Hành vi vi phạm: {hanh_vi}")
                elif nhan == "Trạng thái:":
                    trang_thai = nhom.find_element(By.XPATH, './div[@class="col-md-9"]/span').text.strip()
                    print(f"Trạng thái: {trang_thai}")
            except Exception as e:
                print(f"Lỗi khi lấy dữ liệu: {str(e)}")
        return "success"
    
    except Exception as e:
        print("Gặp lỗi khi xử lý dữ liệu:", str(e))
        return "error"
