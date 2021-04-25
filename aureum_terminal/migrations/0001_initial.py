# Generated by Django 3.1.5 on 2021-04-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(blank=True, max_length=500, null=True)),
                ('header', models.CharField(blank=True, max_length=500, null=True)),
                ('eng_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('value', models.CharField(blank=True, max_length=500, null=True)),
                ('unit', models.CharField(blank=True, max_length=500, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('statement', models.CharField(blank=True, max_length=500, null=True)),
                ('report_period', models.DateField(blank=True, null=True)),
                ('filing_type', models.CharField(blank=True, max_length=45, null=True)),
                ('months_ended', models.CharField(blank=True, max_length=500, null=True)),
                ('row_order', models.IntegerField(blank=True, null=True)),
                ('member_order', models.IntegerField(blank=True, null=True)),
                ('header_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'balance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(blank=True, max_length=500, null=True)),
                ('header', models.CharField(blank=True, max_length=500, null=True)),
                ('eng_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('value', models.CharField(blank=True, max_length=500, null=True)),
                ('unit', models.CharField(blank=True, max_length=500, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('statement', models.CharField(blank=True, max_length=500, null=True)),
                ('report_period', models.DateField(blank=True, null=True)),
                ('filing_type', models.CharField(blank=True, max_length=45, null=True)),
                ('months_ended', models.CharField(blank=True, max_length=500, null=True)),
                ('row_order', models.IntegerField(blank=True, null=True)),
                ('member_order', models.IntegerField(blank=True, null=True)),
                ('header_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cash_flow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('cik', models.IntegerField(primary_key=True, serialize=False)),
                ('ticker', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=445, null=True)),
                ('classification', models.IntegerField(blank=True, null=True)),
                ('classification_name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('eng_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('statement', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'dictionary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(blank=True, max_length=500, null=True)),
                ('header', models.CharField(blank=True, max_length=500, null=True)),
                ('eng_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('value', models.CharField(blank=True, max_length=500, null=True)),
                ('unit', models.CharField(blank=True, max_length=500, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('statement', models.CharField(blank=True, max_length=500, null=True)),
                ('report_period', models.DateField(blank=True, null=True)),
                ('filing_type', models.CharField(blank=True, max_length=45, null=True)),
                ('months_ended', models.CharField(blank=True, max_length=500, null=True)),
                ('row_order', models.IntegerField(blank=True, null=True)),
                ('member_order', models.IntegerField(blank=True, null=True)),
                ('header_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'income',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterIdx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_file', models.CharField(blank=True, max_length=25, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'master_idx',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('link', models.CharField(blank=True, max_length=10000, null=True)),
                ('date_published', models.CharField(blank=True, max_length=50, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NonStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(blank=True, max_length=500, null=True)),
                ('header', models.CharField(blank=True, max_length=500, null=True)),
                ('eng_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('value', models.CharField(blank=True, max_length=500, null=True)),
                ('unit', models.CharField(blank=True, max_length=500, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('statement', models.CharField(blank=True, max_length=500, null=True)),
                ('report_period', models.DateField(blank=True, null=True)),
                ('filing_type', models.CharField(blank=True, max_length=45, null=True)),
                ('months_ended', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'non_statement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OldStandDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('statement', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'old_stand_dict',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Scrape',
            fields=[
                ('filing_type', models.CharField(blank=True, max_length=45, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('file_name', models.CharField(blank=True, max_length=445, null=True)),
                ('accession_number', models.CharField(max_length=445, primary_key=True, serialize=False)),
                ('inter_or_htm', models.CharField(blank=True, max_length=5, null=True)),
                ('status', models.CharField(blank=True, max_length=11, null=True)),
                ('quarter', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'scrape',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StandardBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=5000, null=True)),
                ('standard_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('eng_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('value', models.CharField(blank=True, max_length=500, null=True)),
                ('unit', models.CharField(blank=True, max_length=500, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('statement', models.CharField(blank=True, max_length=500, null=True)),
                ('report_period', models.DateField(blank=True, null=True)),
                ('filing_type', models.CharField(blank=True, max_length=45, null=True)),
                ('quarter', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'standard_balance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StandardCash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=5000, null=True)),
                ('standard_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('eng_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('value', models.CharField(blank=True, max_length=500, null=True)),
                ('unit', models.CharField(blank=True, max_length=500, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('statement', models.CharField(blank=True, max_length=500, null=True)),
                ('report_period', models.DateField(blank=True, null=True)),
                ('filing_type', models.CharField(blank=True, max_length=45, null=True)),
                ('quarter', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'standard_cash',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StandardDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('statement', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'standard_dict',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StandardIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=5000, null=True)),
                ('standard_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('eng_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('value', models.CharField(blank=True, max_length=500, null=True)),
                ('unit', models.CharField(blank=True, max_length=500, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('statement', models.CharField(blank=True, max_length=500, null=True)),
                ('report_period', models.DateField(blank=True, null=True)),
                ('filing_type', models.CharField(blank=True, max_length=45, null=True)),
                ('quarter', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'standard_income',
                'managed': False,
            },
        ),
    ]
