import os
from pymongo import mongo_client
from dotenv import load_dotenv

load_dotenv()


MONGODB_URI = os.getenv('DATABASE_URL')

print(MONGODB_URI)

client = mongo_client.MongoClient(MONGODB_URI)

db = client['scrape_db']
FacebookPagesCollection = db.facebook_pages

