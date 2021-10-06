from django.shortcuts import render
from django.views.generic import TemplateView
from reader.models import Article


class MainPage(TemplateView):
    
    def get(self, request, **kwargs):
        article_list = Article.objects.all().values()[::-1]
        context ={'articles':article_list}
        return render(request,'index.html', context)