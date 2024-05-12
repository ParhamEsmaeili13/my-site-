from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.PortfolioView.as_view(), name='portfolio'),
    path('detail/<int:portfolio_id>/<slug:portfolio_slug>/', views.PortfolioDetailView.as_view(), name='detail_portfolio'),
]
