from django.shortcuts import render
from .models import PenaltyTaxRate
# Create your views here.

def index(request):

    penaltyTaxRates = PenaltyTaxRate.objects.all() 

    return render(
        request,
        'no_reporting_penalty/index.html',
        {
            'penaltyTaxRates' : penaltyTaxRates,
        }
    )


# def single_post_page(request, pk):
#     penaltyTaxRate = PenaltyTaxRate.objects.get(pk=pk)

#     return render(
#         request,
#         '/single_post_page.html',
#         {
#             'penaltyTaxRate' : penaltyTaxRate,
#         }
#     )