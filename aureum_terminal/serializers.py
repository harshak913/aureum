from rest_framework import serializers
from .models import Company, News, Scrape, StandardBalance, StandardIncome, StandardCash, Balance, Income, CashFlow, NonStatement

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['cik', 'ticker', 'name', 'classification', 'classification_name', 'description']

class ScrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrape
        fields = ['cik', 'filing_type', 'year', 'file_name', 'accession_number', 'inter_or_htm', 'quarter']
    
class StandardBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardBalance
        fields = ['accession_number', 'header', 'standard_name', 'eng_name', 'acc_name', 'value', 'unit', 'year', 'statement', 'report_period', 'filing_type', 'quarter', 'id']

class StandardIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardIncome
        fields = ['accession_number', 'header', 'standard_name', 'eng_name', 'acc_name', 'value', 'unit', 'year', 'statement', 'report_period', 'filing_type', 'quarter', 'id']

class StandardCashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardCash
        fields = ['accession_number', 'header', 'standard_name', 'eng_name', 'acc_name', 'value', 'unit', 'year', 'statement', 'report_period', 'filing_type', 'quarter', 'id']

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['accession_number', 'member', 'header', 'eng_name', 'acc_name', 'value', 'unit', 'year', 'statement', 'report_period', 'filing_type', 'months_ended', 'row_order', 'member_order', 'header_order', 'id']

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['accession_number', 'member', 'header', 'eng_name', 'acc_name', 'value', 'unit', 'year', 'statement', 'report_period', 'filing_type', 'months_ended', 'row_order', 'member_order', 'header_order', 'id']

class CashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlow
        fields = ['accession_number', 'member', 'header', 'eng_name', 'acc_name', 'value', 'unit', 'year', 'statement', 'report_period', 'filing_type', 'months_ended', 'row_order', 'member_order', 'header_order', 'id']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['cik', 'title', 'link', 'date_published', 'source', 'id']

# Non-Statement Serializer
""" class NonStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonStatement
        fields = ['accession_number', 'member', 'header', 'eng_name', 'acc_name', 'value', 'unit', 'year', 'statement', 'report_period', 'filing_type', 'months_ended'] """