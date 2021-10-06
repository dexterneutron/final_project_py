import decimal
from django.http import response
from django.shortcuts import render
from django.views.generic import TemplateView
from reader.models import Article
from django.http import HttpResponse


class MainPage(TemplateView):
    
    def get(self, request, **kwargs):
        article_list = Article.objects.all().values()[::-1]
        context ={'articles':article_list}
        return render(request,'index.html', context)