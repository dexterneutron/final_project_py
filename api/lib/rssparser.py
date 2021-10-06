from bs4 import BeautifulSoup
import requests
 
VERGE_URL = 'https://www.theverge.com/rss/index.xml'
TECHCRUNCH_URL = 'https://techcrunch.com/feed/'
MASHABLE_URL = 'https://mashable.com/feeds/rss/all'
 
class ReadRss:
    HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
        }
    def __init__(self, url_list):
        self.reponse_objects = {}
        urls = {"verge":VERGE_URL,"techcrunch":TECHCRUNCH_URL, "mashable":MASHABLE_URL}
        
        for page in url_list:
            rss_url =  urls[page]       
            try:
                r = requests.get(rss_url, headers = self.HEADERS)
                self.reponse_objects[page] = r
            except Exception as e:
                print('Error fetching the URL: ', rss_url)
                print(e)

    def parse_articles(self):
        
        all_articles = []

        for key,value in self.reponse_objects.items():
          #Each RSS site has its own structure, so, it's needed to parse each of them separately
            if key == "verge":
                try:    
                    soup = BeautifulSoup(value.text, 'lxml')
                except Exception as e:    
                    print('Could not parse the xml: ', self.url)
                    print(e)

                articles = soup.findAll('entry')
                articles_dicts = [{'source':'The Verge',
                'title':a.find('title').getText(),
                'published':a.find('published').getText(),
                'author':a.find('author').find('name').getText(),
                'id':a.find('id').getText(),
                } for a in articles]
                all_articles.append(articles_dicts)

            elif key == "techcrunch":
                try:    
                    soup = BeautifulSoup(value.text, 'xml')
                except Exception as e:    
                    print('Could not parse the xml: ', self.url)
                    print(e)

                articles = soup.findAll('item')
                articles_dicts = [{'source':'Techcrunch',
                'title':a.find('title').text,
                'published':a.find('pubDate').text,
                'author':a.find('dc:creator').text,
                'id':a.find('link').text
                } for a in articles]
                all_articles.append(articles_dicts)

            elif key == "mashable":
                try:    
                    soup = BeautifulSoup(value.text, 'xml')
                except Exception as e:    
                    print('Could not parse the xml: ', self.url)
                    print(e)

                articles = soup.findAll('item')
                articles_dicts = [{'source':'Mashable',
                'title':a.find('title').text,
                'published':a.find('pubDate').text,
                'id':a.find('link').text
                } for a in articles]
                all_articles.append(articles_dicts)
            
            #Finally we merge the list into one
            output_list = []
            for list in all_articles:
                output_list.extend(list)

        return output_list
 
if __name__ == '__main__':
 
    feed = ReadRss(url_list = ["mashable","techcrunch","verge"])
    print(feed.parse_articles())