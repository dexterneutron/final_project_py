from bs4 import BeautifulSoup
import requests
 
VERGE_URL = 'https://www.theverge.com/rss/index.xml'
TECHCRUNCH_URL = 'https://techcrunch.com/feed/'
MASHABLE_URL = 'https://mashable.com/feeds/rss/all'


headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
        }
 
class ReadRss:
    def __init__(self, headers, url_list):
        self.reponse_objects = {}
        self.urls = {"verge":VERGE_URL,"techcrunch":TECHCRUNCH_URL, "mashable":MASHABLE_URL}
        for page in url_list:
            rss_url =  self.urls[page]       
            self.headers = headers
            try:
                r = requests.get(rss_url, headers = headers)
                self.reponse_objects[page] = r
            except Exception as e:
                print('Error fetching the URL: ', rss_url)
                print(e)

    def parse_articles(self):
        for key,value in self.reponse_objects.items():
            if key == "verge":
                try:    
                    soup = BeautifulSoup(value.text, 'lxml')
                except Exception as e:    
                    print('Could not parse the xml: ', self.url)
                    print(e)

                articles = soup.findAll('entry')
                self.articles_dicts = [{'title':a.find('title').getText(),
                'content':a.find('content').getText(),
                'published':a.find('published').getText(),
                'author':a.find('author').find('name').getText(),
                'id':a.find('id').getText(),
                } for a in articles]

            if key == "techcrunch":
                try:    
                    soup = BeautifulSoup(value.text, 'xml')
                except Exception as e:    
                    print('Could not parse the xml: ', self.url)
                    print(e)

                articles = soup.findAll('item')
                articles_dicts = [{'title':a.find('title').text,
                'content':a.find('content:encoded').text,
                'published':a.find('pubDate').text,
                'author':a.find('dc:creator').text,
                'id':a.find('link').text
                } for a in articles]

        return articles_dicts
 
if __name__ == '__main__':
 
    feed = ReadRss(headers, url_list = ["techcrunch"])
    #feed = feed.parse_articles()
    print(feed.parse_articles())