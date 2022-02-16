from django.contrib import admin
from .models import Company, Scrape, StandardBalance, StandardIncome, StandardCash, Balance, Income, CashFlow, NonStatement, HedgeData

# Register your models here.

admin.site.register(Company)
admin.site.register(Scrape)
admin.site.register(StandardBalance)
admin.site.register(StandardIncome)
admin.site.register(StandardCash)
admin.site.register(Balance)
admin.site.register(Income)
admin.site.register(CashFlow)
admin.site.register(HedgeData)
#admin.site.register(NonStatement)