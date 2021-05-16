from .models import Company, Scrape, StandardBalance, StandardCash, StandardIncome, Balance, Income, CashFlow, News
from django.db.models import Q
from .serializers import CompanySerializer, ScrapeSerializer, StandardBalanceSerializer, StandardIncomeSerializer, StandardCashFlowSerializer, BalanceSerializer, IncomeSerializer, CashFlowSerializer, NewsSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Lets us access company serialized JSON data
class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        if 'cik' in self.kwargs:
            return Company.objects.filter(cik=self.kwargs['cik'])
        return Company.objects.all()

    lookup_field = 'cik'
    serializer_class = CompanySerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

# Lets us access scrape serialized JSON data for each company
class ScrapeViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):
        year = self.request.query_params.get('year', None)
        filing_type = self.request.query_params.get('type', None)

        # Generates a URL with extra parameters
        # In a URL, lookup_field specifies which main attribute (key or non-key) can be narrowed down using just one /
        # We can add extra fields in addition to the lookup_field by using the django-filter library and Q() module
        # /? indicates the beginning of variable inputs in a query
        # After the /?, additional inputs can be concatenated by using just &
        # For example, https://localhost:8000/filings/789019/?year=2009|2010|2011&type=10-k

        if 'cik' in self.kwargs:
            if year is not None:
                year = year.split('|')
                query = Q()
                for y in year:
                    query |= Q(year=y)
                if filing_type is not None:
                    return Scrape.objects.filter(Q(cik=self.kwargs['cik']) & query & Q(filing_type__icontains=filing_type)) #__icontains makes the type variable in the query case-insensitive
                return Scrape.objects.filter(Q(cik=self.kwargs['cik']) & query)
            return Scrape.objects.filter(cik=self.kwargs['cik'])
        return Scrape.objects.all()

    lookup_field = 'cik'
    serializer_class = ScrapeSerializer

    def retrieve(self, request, *args, **kwargs): # Change is here <<
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

# Lets us access scrape serialized JSON data for each company
class CompanyClassificationViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):

        if 'classification' in self.kwargs:
            return Company.objects.filter(classification=self.kwargs['classification'])
        return Company.objects.all()

    lookup_field = 'classification'
    serializer_class = CompanySerializer

    def retrieve(self, request, *args, **kwargs): # Change is here <<
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

# Lets us access standard balance serialized JSON data
class StandardBalanceViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        if 'accession_number' in self.kwargs:
            return StandardBalance.objects.filter(accession_number=self.kwargs['accession_number'])
        return StandardBalance.objects.all()
        
    lookup_field = 'accession_number'
    serializer_class = StandardBalanceSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

# Lets us access standard income serialized JSON data
class StandardIncomeViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        if 'accession_number' in self.kwargs:
            return StandardIncome.objects.filter(accession_number=self.kwargs['accession_number'])
        return StandardIncome.objects.all()
        
    lookup_field = 'accession_number'
    serializer_class = StandardIncomeSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

# Lets us access standard cash flow serialized JSON data
class StandardCashFlowViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        if 'accession_number' in self.kwargs:
            return StandardCash.objects.filter(accession_number=self.kwargs['accession_number'])
        return StandardCash.objects.all()
        
    lookup_field = 'accession_number'
    serializer_class = StandardCashFlowSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

# Lets us access balance serialized JSON data
class BalanceViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        if 'accession_number' in self.kwargs:
            return Balance.objects.filter(accession_number=self.kwargs['accession_number'])
        return Balance.objects.all()
        
    lookup_field = 'accession_number'
    serializer_class = BalanceSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

# Lets us access income serialized JSON data
class IncomeViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        if 'accession_number' in self.kwargs:
            return Income.objects.filter(accession_number=self.kwargs['accession_number'])
        return Income.objects.all()
        
    lookup_field = 'accession_number'
    serializer_class = IncomeSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

# Lets us access cash flow serialized JSON data
class CashFlowViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        if 'accession_number' in self.kwargs:
            return CashFlow.objects.filter(accession_number=self.kwargs['accession_number'])
        return CashFlow.objects.all()
        
    lookup_field = 'accession_number'
    serializer_class = CashFlowSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

# Lets us access news serialized JSON data
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        if 'cik' in self.kwargs:
            return News.objects.filter(cik=self.kwargs['cik'])
        return News.objects.all()
        
    lookup_field = 'cik'
    serializer_class = NewsSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)