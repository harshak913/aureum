# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

class Company(models.Model):
    cik = models.IntegerField(primary_key=True)
    ticker = models.CharField(unique=True, max_length=10, blank=True, null=True)
    name = models.CharField(max_length=445, blank=True, null=True)
    classification = models.IntegerField(blank=True, null=True)
    classification_name = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Scrape(models.Model):
    cik = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='cik_id')
    filing_type = models.CharField(max_length=45, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=445, blank=True, null=True)
    accession_number = models.CharField(primary_key=True, max_length=445)
    inter_or_htm = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    quarter = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scrape'


class Balance(models.Model):
    accession_number = models.ForeignKey(Scrape, on_delete=models.CASCADE, db_column='accession_number')
    member = models.CharField(max_length=500, blank=True, null=True)
    header = models.CharField(max_length=500, blank=True, null=True)
    eng_name = models.CharField(max_length=5000, blank=True, null=True)
    acc_name = models.CharField(max_length=5000, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    unit = models.CharField(max_length=500, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    statement = models.CharField(max_length=500, blank=True, null=True)
    report_period = models.DateField(blank=True, null=True)
    filing_type = models.CharField(max_length=45, blank=True, null=True)
    months_ended = models.CharField(max_length=500, blank=True, null=True)
    row_order = models.IntegerField(blank=True, null=True)
    member_order = models.IntegerField(blank=True, null=True)
    header_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balance'


class Income(models.Model):
    accession_number = models.ForeignKey(Scrape, on_delete=models.CASCADE, db_column='accession_number')
    member = models.CharField(max_length=500, blank=True, null=True)
    header = models.CharField(max_length=500, blank=True, null=True)
    eng_name = models.CharField(max_length=5000, blank=True, null=True)
    acc_name = models.CharField(max_length=5000, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    unit = models.CharField(max_length=500, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    statement = models.CharField(max_length=500, blank=True, null=True)
    report_period = models.DateField(blank=True, null=True)
    filing_type = models.CharField(max_length=45, blank=True, null=True)
    months_ended = models.CharField(max_length=500, blank=True, null=True)
    row_order = models.IntegerField(blank=True, null=True)
    member_order = models.IntegerField(blank=True, null=True)
    header_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'income'


class CashFlow(models.Model):
    accession_number = models.ForeignKey(Scrape, on_delete=models.CASCADE, db_column='accession_number')
    member = models.CharField(max_length=500, blank=True, null=True)
    header = models.CharField(max_length=500, blank=True, null=True)
    eng_name = models.CharField(max_length=5000, blank=True, null=True)
    acc_name = models.CharField(max_length=5000, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    unit = models.CharField(max_length=500, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    statement = models.CharField(max_length=500, blank=True, null=True)
    report_period = models.DateField(blank=True, null=True)
    filing_type = models.CharField(max_length=45, blank=True, null=True)
    months_ended = models.CharField(max_length=500, blank=True, null=True)
    row_order = models.IntegerField(blank=True, null=True)
    member_order = models.IntegerField(blank=True, null=True)
    header_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_flow'


class Dictionary(models.Model):
    standard_name = models.CharField(max_length=5000, blank=True, null=True)
    eng_name = models.CharField(max_length=5000, blank=True, null=True)
    acc_name = models.CharField(max_length=5000, blank=True, null=True)
    statement = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dictionary'


class MasterIdx(models.Model):
    master_file = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_idx'

class News(models.Model):
    cik = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='cik')
    title = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=10000, blank=True, null=True)
    date_published = models.CharField(max_length=50, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class NonStatement(models.Model):
    accession_number = models.ForeignKey('Scrape', on_delete=models.CASCADE, db_column='accession_number')
    member = models.CharField(max_length=500, blank=True, null=True)
    header = models.CharField(max_length=500, blank=True, null=True)
    eng_name = models.CharField(max_length=5000, blank=True, null=True)
    acc_name = models.CharField(max_length=5000, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    unit = models.CharField(max_length=500, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    statement = models.CharField(max_length=500, blank=True, null=True)
    report_period = models.DateField(blank=True, null=True)
    filing_type = models.CharField(max_length=45, blank=True, null=True)
    months_ended = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_statement'


class OldStandDict(models.Model):
    standard_name = models.CharField(max_length=5000, blank=True, null=True)
    acc_name = models.CharField(max_length=5000, blank=True, null=True)
    statement = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'old_stand_dict'


class StandardDict(models.Model):
    standard_name = models.CharField(max_length=5000, blank=True, null=True)
    acc_name = models.CharField(max_length=5000, blank=True, null=True)
    statement = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_dict'


class StandardBalance(models.Model):
    accession_number = models.ForeignKey(Scrape, on_delete=models.CASCADE, db_column='accession_number')
    header = models.CharField(max_length=5000, blank=True, null=True)
    standard_name = models.CharField(max_length=5000, blank=True, null=True)
    eng_name = models.CharField(max_length=5000, blank=True, null=True)
    acc_name = models.CharField(max_length=5000, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    unit = models.CharField(max_length=500, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    statement = models.CharField(max_length=500, blank=True, null=True)
    report_period = models.DateField(blank=True, null=True)
    filing_type = models.CharField(max_length=45, blank=True, null=True)
    quarter = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_balance'


class StandardIncome(models.Model):
    accession_number = models.ForeignKey(Scrape, on_delete=models.CASCADE, db_column='accession_number')
    header = models.CharField(max_length=5000, blank=True, null=True)
    standard_name = models.CharField(max_length=5000, blank=True, null=True)
    eng_name = models.CharField(max_length=5000, blank=True, null=True)
    acc_name = models.CharField(max_length=5000, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    unit = models.CharField(max_length=500, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    statement = models.CharField(max_length=500, blank=True, null=True)
    report_period = models.DateField(blank=True, null=True)
    filing_type = models.CharField(max_length=45, blank=True, null=True)
    quarter = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_income'


class StandardCash(models.Model):
    accession_number = models.ForeignKey(Scrape, on_delete=models.CASCADE, db_column='accession_number')
    header = models.CharField(max_length=5000, blank=True, null=True)
    standard_name = models.CharField(max_length=5000, blank=True, null=True)
    eng_name = models.CharField(max_length=5000, blank=True, null=True)
    acc_name = models.CharField(max_length=5000, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    unit = models.CharField(max_length=500, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    statement = models.CharField(max_length=500, blank=True, null=True)
    report_period = models.DateField(blank=True, null=True)
    filing_type = models.CharField(max_length=45, blank=True, null=True)
    quarter = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_cash'


# Authentication-related models
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

# Django-related models
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'