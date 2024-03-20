# webdriver = webdriver.Edge()
#
# webdriver.get("http://www.baidu.com")
# el = webdriver.find_element('id','kw')
# el.send_keys("和珈增")
# el2 = webdriver.find_element('id','su')
# el2.click()
from selenium import webdriver
driver = webdriver(executable_path = "msedgedriver")
driver.execute("get", {'url': "http://www.baidu.com"})
driver.execute("id", {'url': "kw"})
