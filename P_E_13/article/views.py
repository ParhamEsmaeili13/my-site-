from django.shortcuts import render, get_object_or_404
from django.views import View
from article.models import Article


class ArticleListView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'article/article_list.html', {'articles': articles})


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['article_id'], slug=kwargs['article_slug'])
        return render(request, 'article/detail_article.html', {'article': article})


