import requests
from reader.models import Article

def _get_data_json():
    url = 'http://127.0.0.1:5000/api/feed'
    r = requests.get(url)
    return r
    #try:
     #   r.raise_for_status()
      #  return r.json()
    #except:
     #   return None     

def update_data():
    json = _get_data_json()
    for el in json:
        new_article = Article()
        new_article.article_link = el['id']
        #new_article.article_link = el['title']
        #new_article.article_source = el['source']
        new_article.save()
    #if json is not None:
     #   try:
      #      for el in json:
       #         new_article = Article()
        #        new_article.article_link = el['id']
         #       new_article.article_link = el['title']
          #      new_article.article_source = el['source']
           #     new_article.save()
            #    print("saving...\n" + new_article)
        #except:
         #   print("error saving...\n" + new_article)