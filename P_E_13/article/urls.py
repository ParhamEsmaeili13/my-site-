from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article'),
    path('detail/<int:article_id>/<slug:article_slug>/', views.ArticleDetailView.as_view(), name='detail_article'),
]
