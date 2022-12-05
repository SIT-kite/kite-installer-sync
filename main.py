import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from datetime import datetime
import os
from config import username, password
from download import assets_output_paths

driver = webdriver.Chrome()

driver.get('https://www.123pan.com/')

# 登录
driver.find_element(By.ID, 'basic_passport').send_keys(username)
driver.find_element(By.ID, 'basic_password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'loginBtn').click()
time.sleep(0.5)

# 点击新建文件夹
driver.find_element(By.CLASS_NAME, 'sysbut').click()
time.sleep(0.5)

# 输入新建文件夹名称
dir_name = datetime.now().strftime('%Y%m%d%H%M%S')
dir_name_input = driver.find_element(By.CSS_SELECTOR, 'div.ant-modal-body > input')
dir_name_input.clear()
dir_name_input.send_keys(dir_name)
time.sleep(0.5)
# 点击确定
driver.find_element(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary > span').click()
time.sleep(0.5)

# 寻找第一个文件夹点击确定
driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(2) > td.ant-table-cell.drag-visible > div > div > span').click()


def upload_file(file_path: str):
    # 悬浮上传按钮
    upload_btn = driver.find_element(By.CLASS_NAME, 'parmiryButton')
    ActionChains(driver).move_to_element(upload_btn).perform()
    time.sleep(0.5)

    # 上传文件
    file_uploader = driver.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(1) > span > div > input[type=file]')
    file_uploader.send_keys(file_path)
    time.sleep(0.5)


for output_path in assets_output_paths:
    upload_file(output_path)
time.sleep(0.5)

# 返回上一页
driver.back()
time.sleep(0.5)

# 点击分享
share_area = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(2) > td:nth-child(3) > div')
ActionChains(driver).move_to_element(share_area).perform()
driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(2) > td:nth-child(3) > div > div > div:nth-child(1)').click()
time.sleep(0.5)

# 选择永久有效
driver.find_element(By.CSS_SELECTOR, 'label:nth-child(4)').click()

# 选择无提取码
driver.find_element(By.CSS_SELECTOR, 'div:nth-child(4) > label:nth-child(1)').click()

# 点击创建链接
driver.find_element(By.CSS_SELECTOR, 'div.ant-modal-body > div:nth-child(2) > button > span').click()
time.sleep(0.5)

# 获取网盘链接
shared_link = driver.find_element(By.CSS_SELECTOR, 'div.ant-modal-body > div:nth-child(1) > span').text

print(f'网盘链接：{shared_link}')
