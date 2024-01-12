from typing import List, Optional
from pydantic import BaseModel

class PageLinkRequestPayload(BaseModel):
    """PageLink
    Description:
    This is a data model to be passed for the  scrape endpoint
    """
    page_link: str

class PageInformationResponse(BaseModel):
    """
    Page information after scraping
    """
    name: str
    likes: str
    followers: str
    description: str
    page_type: str
    phone_number: str
    email: str
    website: str

class ScrapeJobResponse(BaseModel):
    """ScrapeJobResponse
    Description:
    This is a data model to be used to indicate the status of the scraping job
    """
    status: Optional[str] = ""
    message: Optional[str] = ""
    page_information: Optional[PageInformationResponse] = None


