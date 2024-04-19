from django.shortcuts import render
from django.views import View
from portfolio.models import Portfolio


class PortfolioView(View):
    def get(self, request):
        portfolios = Portfolio.objects.all()
        return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})


