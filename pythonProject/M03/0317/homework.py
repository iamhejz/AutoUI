from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://shop-xo.hctestedu.com/")
#
# try:

driver.find_element('link text','注册').click()
driver.find_element('link text','账号注册').click()
sleep(2)

# driver.find_element('name','accounts').send_keys('iamhejz')
# driver.find_element('name','pwd').send_keys('iamhejz')
# driver.find_element('link text','注册').click()
# sleep(2)
driver.find_element('link text','商城首页').click()
driver.find_element('link text','登录').click()
driver.find_element('name','accounts').send_keys('iamhejz')
driver.find_element('name','pwd').send_keys('iamhejz')
sleep(2)
driver.find_elements('//button[text()="登录"]')[0].click()
sleep(2)
# excepted = '退出'
# reality = driver.find_element('link text','退出').text
# assert excepted == reality,'登陆失败'
driver.quit()
# except Exception as e:
#     print("错误")
#     driver.quit()