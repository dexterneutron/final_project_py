from django.db import models

class Article(models.Model):
    article_link = models.URLField(max_length=500, primary_key=True)
    article_content = models.TextField
    article_title = models.CharField(max_length=500)
    article_source = models.CharField(max_length=50)
     
