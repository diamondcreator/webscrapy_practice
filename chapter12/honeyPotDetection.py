#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

if __name__ == '__main__':
    driver = webdriver.PhantomJS(
        executable_path=r'D:\Program Files\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
    driver.get('http://pythonscraping.com/pages/itsatrap.html')

    links = driver.find_elements_by_tag_name('a')
    for link in links:
        if not link.is_displayed():
            print('The link ' + link.get_attribute('href') + ' is a trap')

    fields = driver.find_elements_by_tag_name('input')
    for field in fields:
        if not field.is_displayed():
            print('Do not change value of ' + field.get_attribute('name'))
