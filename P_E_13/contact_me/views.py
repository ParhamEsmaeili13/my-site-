from django.shortcuts import render, redirect
from django.views import View
from .forms import UserContactForm
from django.contrib import messages


class ContactMeView(View):
    def get(self, request):
        return render(request, 'contact_me/contact_me.html')

    def post(self, request):
        form = UserContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your message was sent successfully! I reply you soon', extra_tags='success')
        else:
            messages.error(request, 'not a valid message', extra_tags='danger')
        return redirect('contact_me:contact_me')
