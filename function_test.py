'''
Created on 2015年12月1日

@author: zhiwei
'''
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Django" in browser.title