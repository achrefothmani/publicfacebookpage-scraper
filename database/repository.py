import logging
from sqlalchemy.orm import Session
from database.database import FacebookPagesCollection
from scraper.schema import PageInformationResponse

def insert_record(scraped_page: PageInformationResponse):
    try:
        FacebookPagesCollection.insert_one(scraped_page.model_dump())
    except Exception as e:
        logging.exception("Unable to insert into database " + str(e))
        raise Exception ("Unable to insert record into database")