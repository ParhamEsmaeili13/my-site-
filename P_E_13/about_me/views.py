from django.shortcuts import render
from django.views import View


class AboutMeView(View):
    def get(self, request):
        return render(request, 'about_me/about_me.html')
