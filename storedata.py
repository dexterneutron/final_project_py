from rssparser import ReadRss, HEADERS
from pymongo import MongoClient

class MongoConnection:

    def __init__(self):
        CONNECTION_STRING = "mongodb://root:rootpassword@127.0.0.1:27017"
        self.client = MongoClient(CONNECTION_STRING)
        self.db = self.client.rss
        self.col = self.db.articles

def store_data():
    connection = MongoConnection()
    articles_coll = connection.col #Collection:articles

    feed = ReadRss(HEADERS, url_list = ["mashable","techcrunch","verge"])
    articles_list = feed.parse_articles()
    result = articles_coll.insert_many(articles_list)


def get_data():
    connection = MongoConnection()
    #CONNECTION_STRING = "mongodb://root:rootpassword@127.0.0.1:27017"
    #client = MongoClient(CONNECTION_STRING)
    #db = client.rss #Database name:rss
    articles_coll = connection.col #Collection:articles
    #for x in articles_coll.find():
    #    print(x)
    print(articles_coll.count())
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    # Get the database
    store_data()
    get_data()