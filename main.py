from typing import Union
import uvicorn
from fastapi import FastAPI

from models import PageInformationResponse, PageLinkRequestPayload, ScrapeJobResponse
from selenium.webdriver.chrome.options import Options
from scraper.scraper import Scraper, SeleniumWebDriver
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
                

app = FastAPI()

@app.get("/")
@app.get("/api/health")
def health():
    return {"Status": "OK"}


@app.post("/api/scrape")
def scrape(page_link: PageLinkRequestPayload):

    response = ScrapeJobResponse()
    
    driver_options = Options()
    #driver_options.add_argument("--headless")

    driver = SeleniumWebDriver(driver_options)
    driver = driver.get_driver()

    scraper = Scraper(page_link.page_link, driver)
    try:
        scraper.close_popup()
    except Exception as e:
        logging.exception('Unable to scrape page: ', str(e))
        response.message = "Unable to scrape page"
        response.status = "failed"
        return response
    
    name = scraper.get_page_name()
    likes = scraper.get_likes_count()
    followers = scraper.get_followers_count()
    description = scraper.get_description()
    page_type = scraper.get_page_type()
    address = scraper.get_address()
    phone_number = scraper.get_phone_number()
    email = scraper.get_email()
    website = scraper.get_website()

    page_information = PageInformationResponse(name=name, likes=likes, followers=followers, description=description,
                                               page_type=page_type, address=address, phone_number=phone_number, email=email,
                                               website=website)
    response.page_information = page_information
    response.status = "OK"
    
    return response



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
