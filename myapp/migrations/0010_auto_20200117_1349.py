# Generated by Django 2.2.9 on 2020-01-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200117_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
