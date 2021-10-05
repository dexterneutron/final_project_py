import decimal
from django.http import response
from django.shortcuts import render
from django.views.generic import TemplateView
from reader.models import Article
from django.http import HttpResponse


class MainPage(TemplateView):
    
    def get(self, request, **kwargs):
        #article = Article.objects    
        #article_content = Article.article_content
        #article_title = Article.article_title
        #article_source = Article.article_title
        article_list = Article.objects.all().values()
        context ={'articles':article_list}
        return render(request,'index.html', context)