# Public Facebook page scrapper

This is a public facebook page scrapper web app.

The service can be called via an endpoint `/api/scrape` to scrape public information like page name, description, email, phone number, etc ...

Results will be stored in a mongo database.


# Endpoint documentation:

Method: `POST`

Endpoint: `/api/scrape`

Payload: `{"page_link":"<FACEBOOK_PAGE_LINK>"}`

# Usage
### Via docker
`docker-compose up -d`

### Via python
`python3 -m venv ./venv`

`source ./venv/bin/activate`

`pip install -r requirements.txt`

`python main.py`

When running locally without docker please provide a valid mongodb connection URL in .env