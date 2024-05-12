from django.shortcuts import render, get_object_or_404
from django.views import View

from portfolio.models import Portfolio


class PortfolioView(View):
    def get(self, request):
        portfolios = Portfolio.objects.all()
        return render(request, 'portfolio/portfolio_list.html', {'portfolios': portfolios})


class PortfolioDetailView(View):
    def get(self, request, *args, **kwargs):
        portfolio = get_object_or_404(Portfolio, pk=kwargs['portfolio_id'], slug=kwargs['portfolio_slug'])
        return render(request, 'portfolio/detail_portfolio.html', {'portfolio': portfolio})
