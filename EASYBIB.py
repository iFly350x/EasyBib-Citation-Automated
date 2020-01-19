from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import sys
from selenium.webdriver.remote.webelement import WebElement

class citations():

    def __init__(self):
        browser = webdriver.Chrome()
        self.browser = browser

    def begin_site(self):
        browser = self.browser
        browser.get('http://www.easybib.com/')
        button = browser.find_element_by_xpath('//a[contains(text(),"Create citations")]')
        button.click()

    def initilize_search(self):
        browser = self.browser
        try:
            website_button = browser.find_element_by_xpath('//button[contains(text(),"Website")]')
            website_button.click()
        except:
            time.sleep(30)
            website_button = browser.find_element_by_xpath('//button[contains(text(),"Website")]')
            website_button.click()

    def send_text(self, citation):
        browser = self.browser
        time.sleep(1)
        search_bar: WebElement = browser.find_element_by_xpath('.//*[@class="sc-jtHxuu kwNxaU"]')
        search_bar.send_keys(citation)

    def serach_citations(self):
        browser = self.browser
        serach = browser.find_element_by_xpath('//button[contains(text(),"Search")]')
        serach.click()
        time.sleep(2)
        intialize_citation = browser.find_element_by_xpath('.//*[@class="sc-iujRgT fEkeUc"]//button')
        intialize_citation.click()
        try:
            time.sleep(3)
            continue_citation = browser.find_element_by_xpath('.//*[@class="submit-eval sc-gisBJw flNamk"]')
            continue_citation.click()
        except ElementClickInterceptedException:
            time.sleep(4)
            continue_citation = browser.find_element_by_xpath('.//*[@class="submit-eval sc-gisBJw flNamk"]')
            continue_citation.click()
        try:
            time.sleep(8)
            compelte_citation = browser.find_element_by_xpath('(.//*[@class="sc-fjdhpX dqCjFG"]//button)[2]')
            compelte_citation.click()
        except ElementClickInterceptedException:
            time.sleep(10)
            compelte_citation = browser.find_element_by_xpath('(.//*[@class="sc-fjdhpX dqCjFG"]//button)[2]')
            compelte_citation.click()

    def create_new(self):
        browser = self.browser
        time.sleep(2)
        try:
            create_new_citation = browser.find_element_by_xpath('.//*[@class="sc-fZwumE fbkySJ"]')
            create_new_citation.click()
        except:
            time.sleep(30)
            create_new_citation = browser.find_element_by_xpath('.//*[@class="sc-fZwumE fbkySJ"]')
            create_new_citation.click()

    def citations_list(self):
        with open('citations.txt', 'r') as file:
             return file.read().splitlines()

site = citations()
for _ in range(1):
    site.begin_site()
for citation in site.citations_list():
    site.initilize_search()
    site.send_text(citation)
    time.sleep(2)
    site.serach_citations()
    time.sleep(2)
    site.create_new()