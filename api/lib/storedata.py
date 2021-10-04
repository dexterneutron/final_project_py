import json
from lib.rssparser import ReadRss
from pymongo import MongoClient
from bson import json_util

class MongoConnection:

    def __init__(self):
        CONNECTION_STRING = "mongodb://root:rootpassword@127.0.0.1:27017"
        self.client = MongoClient(CONNECTION_STRING)
        self.db = self.client.rss
        self.col = self.db.articles

def store_data():
    connection = MongoConnection()
    articles_coll = connection.col #Collection:articles

    feed = ReadRss(url_list = ["mashable","techcrunch","verge"])
    articles_list = feed.parse_articles()
    result = articles_coll.insert_many(articles_list)


def get_data():
    connection = MongoConnection()
    articles_coll = connection.col #Collection:articles
    articles = list(articles_coll.find({}))
    return json.loads(json_util.dumps(articles)) 

if __name__ == "__main__":    
    # Get the database
    store_data()
    get_data()