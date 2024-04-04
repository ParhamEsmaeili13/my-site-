from django.urls import path
from . import views

app_name = 'about_me'

urlpatterns = [
    path('', views.AboutMeView.as_view(), name='about_me')

]
