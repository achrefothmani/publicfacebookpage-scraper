from typing import List, Optional
from pydantic import BaseModel



class Post(BaseModel):
    """
    Page posts
    """
    published_at: Optional[str] = ""
    description: Optional[str] = ""
    interactions: Optional[str] = ""
    class Config:
        orm_mode = True



class PageLinkRequestPayload(BaseModel):
    """
    Used to be passed for the  scrape endpoint
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
    latest_post: Post


class ScrapeJobResponse(BaseModel):
    """
    Used to indicate the status of the scraping job
    """
    status: Optional[str] = ""
    message: Optional[str] = ""
    page_information: Optional[PageInformationResponse] = None


