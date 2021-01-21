from django.contrib import admin

# Register your models here.
from .models import PenaltyTaxRate
from .models import PenaltyDiscountRate


admin.site.register(PenaltyTaxRate)
admin.site.register(PenaltyDiscountRate)