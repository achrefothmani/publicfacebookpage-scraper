import unittest
from selenium import webdriver
from scraper.scraper import Scraper

class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        self.page_link = 'https://www.facebook.com/facebook'

    def test_scrape_page_name(self):
        scraper = Scraper(self.page_link, self.driver)
        page_name = scraper.get_page_name()
        self.assertIsInstance(page_name, str)