'''
id\name
link
text
partial
tagname
class name
xpath
css selector

'''
from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('http://shop-xo.hctestedu.com/')

driver.find_element("//a[text()='注册']").click()


name =driver.find_element("//input[@name='username']")
name.send_keys("123456")
passwd =driver.find_element("name","password")
passwd.send_keys('dwdw')
submit = driver.find_element("name","signon")
submit.click()