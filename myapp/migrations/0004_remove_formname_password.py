# Generated by Django 2.2.9 on 2020-01-15 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_formname_portfolio_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formname',
            name='password',
        ),
    ]
