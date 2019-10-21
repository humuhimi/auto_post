import time,sys
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from requests import request as rq
from selenium.webdriver import Chrome,ChromeOptions
import chromedriver_binary

options = ChromeOptions()
options.add_argument('-headless')

driver = wd.Chrome()




