#
from selenium import webdriver
webdriver = webdriver.Chrome()

#窗口最大化,不要用：有可能存在bug会造成driver异常
# webdriver.maximize_window()
#设置窗体大小尺寸
webdriver.set_window_size(1024, 768)

#访问url及文件
webdriver.get("http://shop-xo.hctestedu.com/")

