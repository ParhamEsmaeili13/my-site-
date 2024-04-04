from django.urls import path
from . import views

app_name = 'contact_me'

urlpatterns = [
    path('', views.ContactMeView.as_view(), name='contact_me'),

]

