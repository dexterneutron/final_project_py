import requests
from reader.models import Article

def _get_data_json():
    url = 'http://127.0.0.1:5000/api/feed'
    r = requests.get(url)
    try:
        r.raise_for_status()
        return r.json()
    except:
        return None
             
def update_data():
    json = _get_data_json()
    for el in json:
        try:
            new_article = Article()
            new_article.article_link = el['id']
            new_article.article_title = el['title']
            new_article.article_source = el['source']
            new_article.save()
            print("saving...\n" + new_article.article_title)
        except:
            print("error saving article\n")