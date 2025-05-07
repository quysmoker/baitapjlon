import time
import pytesseract
import cv2
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





# Cấu hình Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def giai_ma_captcha(driver):
    
    captcha_img = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="imgCaptcha"]'))
    )
    captcha_img.click()
    time.sleep(1)
    # Lưu ảnh captcha
    captcha_img.screenshot("captcha.png")
    image = cv2.imread("captcha.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    captcha_text = pytesseract.image_to_string(thresh, config='--psm 6 --oem 3')
    # Loại bỏ các ký tự không phải chữ cái hoặc số, và loại bỏ khoảng trắng dư thừa
    captcha_text = re.sub(r'[^a-zA-Z0-9]', '', captcha_text).strip()
    return captcha_text
