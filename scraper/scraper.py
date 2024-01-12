
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scraper.models import Post
from utils.utils import extract_date, text_purify

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
        
    def get_latest_post(self) -> Post:
        element = self.scrape_by_xpath(posts_xpath)
        latest_post = Post()
        if element is not None:
            date = element.find_element(By.XPATH, ".//span[contains(@class, 'x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1tu3fi x3x7a5m x1nxh6w3 x1sibtaa xo1l8bm xi81zsa x1yc453h')]")
            description = element.find_element(By.XPATH, ".//div[contains(@class, 'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a')]")
            interactions = element.find_element(By.XPATH, ".//span[contains(@class, 'xrbpyxo x6ikm8r x10wlt62 xlyipyv x1exxlbk')]")
            latest_post.description = description.text
            latest_post.published_at = extract_date(date.text)
            latest_post.interactions = interactions.text
            return latest_post
        else:
            logging.error("Unable to get latest post")
            return latest_post