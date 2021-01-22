from .models import PenaltyTaxRate
from django.views.generic import ListView
from django.views.generic import DetailView


class PenaltyTaxRateList(ListView):
    model = PenaltyTaxRate
    ordering = '-pk'
    # template_name = 'no_reporting_penalty/index.html'


class PenaltyTaxRateDetail(DetailView):
    model = PenaltyTaxRate


