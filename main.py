from typing import Union
import uvicorn
from fastapi import FastAPI
from database.repository import insert_record

from scraper.schema import PageInformationResponse, PageLinkRequestPayload, ScrapeJobResponse
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
    driver_options.add_argument("--headless")

    selenium_driver = SeleniumWebDriver(driver_options)
    driver = selenium_driver.get_driver()

    scraper = Scraper(page_link.page_link, driver)
    
    # try:
    #     scraper.close_popup()
    # except Exception as e:
    #     logging.exception('Unable to scrape page: ', str(e))
    #     response.message = "Unable to scrape page"
    #     response.status = "failed"
    #     return response
    
    name = scraper.get_page_name()
    likes = scraper.get_likes_count()
    followers = scraper.get_followers_count()
    description = scraper.get_description()
    page_type = scraper.get_page_type()
    address = scraper.get_address()
    phone_number = scraper.get_phone_number()
    email = scraper.get_email()
    website = scraper.get_website()
    latest_post = scraper.get_latest_post()

    selenium_driver.close_driver()

    page_information = PageInformationResponse(name=name, likes=likes, followers=followers, description=description,
                                               page_type=page_type, address=address, phone_number=phone_number, email=email,
                                               website=website, latest_post=latest_post)
    
    print(page_information)
    try:
        insert_record(page_information)
        response.status = "OK"
    except:
        response.status = "failed"
        response.message = "Unable to insert record into database"

    response.page_information = page_information
    
    return response



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
