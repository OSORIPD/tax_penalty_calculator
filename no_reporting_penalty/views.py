from django.shortcuts import render
from .models import PenaltyTaxRate
from django.views.generic import ListView


class PenaltyTaxRateList(ListView):
    model = PenaltyTaxRate
    ordering = '-pk'
    # template_name = 'no_reporting_penalty/index.html'

# def index(request):

#     penaltyTaxRates = PenaltyTaxRate.objects.all() 

#     return render(
#         request,
#         'no_reporting_penalty/index.html',
#         {
#             'penaltyTaxRates' : penaltyTaxRates,
#         }
#     )


# def single_post_page(request, pk):
#     penaltyTaxRate = PenaltyTaxRate.objects.get(pk=pk)

#     return render(
#         request,
#         '/single_post_page.html',
#         {
#             'penaltyTaxRate' : penaltyTaxRate,
#         }
#     )