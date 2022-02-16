from django.db.models import fields
from rest_framework import serializers
from .models import Company, News, Scrape, StandardBalance, StandardIncome, StandardCash, Balance, Income, CashFlow, NonStatement, StockData, HedgeData

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['cik', 'ticker', 'name', 'classification', 'classification_name', 'description', 'hq', 'website', 'full_time_employees', 'logo_url', 'open', 'prev_close', 'avg_volume_10_days', 'day_high', 'day_low', 'year_high', 'year_low', 'market_cap']

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

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockData
        fields = ['cik', 'date', 'open', 'high', 'low', 'close', 'adj_close', 'volume', 'period', 'interval', 'id']

class HedgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HedgeData
        fields = ['cik', 'fund_name', 'stock_name', 'class_field', 'cusip', 'amount_in_1000', 'number_of_shares', 'put_call', 'filing_date', 'aum_in_1000', 'fund_positions', 'shr_qoq_change_pct', 'percentage_holding', 'average_price_per_share', 'price_qoq_change_pct', 'shr_qoq_change_val', 'shr_qoq_change_capital', 'total_quarterly_capital_change']

# Non-Statement Serializer
""" class NonStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonStatement
        fields = ['accession_number', 'member', 'header', 'eng_name', 'acc_name', 'value', 'unit', 'year', 'statement', 'report_period', 'filing_type', 'months_ended'] """