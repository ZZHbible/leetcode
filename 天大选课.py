import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import ddddocr

url = "http://classes.tju.edu.cn/eams/homeExt.action"

driver = webdriver.Chrome(executable_path='/Users/zhangzhenhua/Downloads/chromedriver')

driver.get(url)

with open('./class.json') as f:
    message=json.load(f)
    id=message["id"]
    pwd=message["pwd"]

driver.find_element(by=By.ID, value="username").send_keys(id)
driver.find_element(by=By.ID, value="password").send_keys(pwd)
image = driver.find_element(by=By.ID, value="captcha_img")
image.screenshot("code.png")
ocr=ddddocr.DdddOcr()
with open("code.png",'rb') as f:
    image=f.read()
catch = ocr.classification(image)
driver.find_element(by=By.ID, value='captcha').send_keys(catch)
sleep(8)

driver.find_element(by=By.CLASS_NAME, value="btn-submit").click()

driver.implicitly_wait(2)
driver.get("http://classes.tju.edu.cn/eams/stdElectCourse.action")
driver.implicitly_wait(2)

driver.find_element(by=By.XPATH, value='//*[@id="electIndexNotice0"]/div[3]/form/a').click()
driver.switch_to.window(driver.window_handles[-1])
driver.implicitly_wait(10)
driver.find_element(by=By.CLASS_NAME, value='electTabSelected').click()
while True:
    driver.find_element(by=By.XPATH, value='//*[@id="electableLessonList"]/thead/tr[1]/th[2]/div/input').send_keys(
        "04914")
    driver.find_element(by=By.XPATH, value='//*[@id="electableLessonList"]/thead/tr[1]/th[3]/div/input').send_keys(
        "S212E037")
    driver.find_element(by=By.XPATH, value='//*[@id="electableLessonList"]/thead/tr[1]/th[4]/div/input').send_keys(
        "积极心理学")
    driver.find_element(by=By.XPATH, value='//*[@id="electableLessonList_filter_submit"]').click()
    sleep(0.5)
    try:
        if driver.find_element(by=By.XPATH, value='//*[@id="lesson431810"]/td[12]/a').text == "选课":
            driver.find_element(by=By.XPATH, value='//*[@id="lesson431810"]/td[12]/a').click()
            driver.switch_to.alert.accept()
    except:
        print("hello")
    finally:
        driver.find_element(by=By.XPATH, value='//*[@id="electableLessonList"]/thead/tr[1]/th[2]/div/input').clear()
        driver.find_element(by=By.XPATH, value='//*[@id="electableLessonList"]/thead/tr[1]/th[3]/div/input').clear()
        driver.find_element(by=By.XPATH, value='//*[@id="electableLessonList"]/thead/tr[1]/th[4]/div/input').clear()
