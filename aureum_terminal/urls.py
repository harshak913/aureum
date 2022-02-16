from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.SimpleRouter() --> use this before deployment since you want to hide API routes from user
router = routers.DefaultRouter() # disable this before deployment; ONLY use for testing since this displays all API routes
router.register(r'companies', views.CompanyViewSet, 'companies')
router.register(r'classification', views.CompanyClassificationViewSet, 'classification')
router.register(r'filings', views.ScrapeViewSet, 'filings')
router.register(r'stdbal', views.StandardBalanceViewSet, 'stdbal')
router.register(r'stdinc', views.StandardIncomeViewSet, 'stdinc')
router.register(r'stdcash', views.StandardCashFlowViewSet, 'stdcash')
router.register(r'bal', views.BalanceViewSet, 'bal')
router.register(r'inc', views.IncomeViewSet, 'inc')
router.register(r'cash', views.CashFlowViewSet, 'cash')
router.register(r'news', views.NewsViewSet, 'news')
router.register(r'stock', views.StockViewSet, 'stock')
router.register(r'hedge', views.HedgeViewSet, 'hedge')

urlpatterns = [
    path('', include(router.urls)),
]