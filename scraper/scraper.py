import time
from bs4 import BeautifulSoup
import requests
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from utils.utils import text_purify, todigit

from .constants import *


class SeleniumWebDriver():
    """
        Initialize a selenium chrome driver on a new instance
    """

    def __init__(self, options):
        driver=webdriver.Chrome(options=options)
        self.driver = driver

    def get_driver(self):
         return self.driver

    def close_driver(self):
         self.driver.close()


class Scraper():
    """
        Contains scraping method to scrape a public facebook page
    """

    def __init__(self, page_link: str, driver):        
        self.driver = driver
        self.driver.get(page_link)
        self.page_source = self.driver.page_source
        self.page_link = page_link

    def scrape_by_xpath(self, xpath: str):
        try:
            web_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return web_element
        except Exception as e:
            logging.exception('Unable to scrape xpath: ' +  xpath + ' '+str(e))
            return None
        
    def scrape_by_classname(self, class_name: str):
        try:
            web_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
            return web_element
        except Exception as e:
            logging.exception('Unable to scrape class_name: ' +  class_name + ' '+str(e))
            return None
        
    def close_popup(self):
        xpath = "//div[@role='button' and @aria-label='Close']"
        try:
            element = self.scrape_by_xpath(xpath)
            element.click()
        except Exception as e:
            logging.exception('Unable to scrape xpath (popupclose): ' +  xpath + ' '+str(e))
            raise Exception("Unable to close popup")

    def get_page_name(self) -> str:
        element = self.scrape_by_xpath(name_xpath)
        if element is not None:
            return text_purify(element.text)
        else:
            return "N/A"
        
    def get_likes_count(self) -> str:
        element = self.scrape_by_xpath(likes_xpath)
        if element is not None:
            return text_purify(element.text)
        else:
            return "N/A"
        
    def get_followers_count(self) -> str:
        element = self.scrape_by_xpath(followers_xpath)
        if element is not None:
            return text_purify(element.text)
        else:
            return "N/A"
        
    def get_description(self) -> str:
        element = self.scrape_by_xpath(description_xpath)
        if element is not None:
            return text_purify(element.text)
        else:
            return "N/A"
        
    def get_page_type(self) -> str:
        element = self.scrape_by_xpath(page_type_xpath)
        if element is not None:
            return text_purify(element.text)
        else:
            return "N/A"
        
    def get_address(self) -> str:
        element = self.scrape_by_xpath(address_xpath)
        if element is not None:
            return text_purify(element.text)
        else:
            return "N/A"
        
    def get_phone_number(self) -> str:
        element = self.scrape_by_xpath(phone_number_xpath)
        if element is not None:
            return text_purify(element.text)
        else:
            return "N/A"
        
    def get_email(self) -> str:
        element = self.scrape_by_xpath(email_xpath)
        if element is not None:
            return text_purify(element.text)
        else:
            return "N/A"
        
    def get_website(self) -> str:
        element = self.scrape_by_xpath(website_xpath)
        if element is not None:
            return text_purify(element.text)
        else:
            return "N/A"
        
    # def get_latest_posts(self) -> list:
    #     element = self.scrape_by_classname(class_name=post_class_name)
    #     if element is not None:
    #         return text_purify(element.text)
    #     else:
    #         return "N/A"