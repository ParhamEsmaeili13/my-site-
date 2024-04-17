from django.shortcuts import render, get_object_or_404
from django.views import View
from article.models import Article


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'article/article.html', {'articles': articles})


class ArticleDetailView(View):
    def get(self, request, article_id):
        article = get_object_or_404(Article, pk=article_id)
        return render(request, 'article/detail_article.html', {'article': article})


