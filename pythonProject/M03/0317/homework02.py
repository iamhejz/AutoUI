from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://music.163.com/")
try:
    driver.find_element('link text','云推歌').click()
    handlers = driver.window_handles
    # driver.switch_to.window(handlers[1])
    driver.close()

except Exception as e:
    print("失败")
    driver.quit()
