from django.shortcuts import render
from django.views import View


class ContactMeView(View):

    def get(self, request):
        return render(request, 'contact_me/contact_me.html')
