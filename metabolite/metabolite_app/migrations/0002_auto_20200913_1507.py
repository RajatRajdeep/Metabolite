# Generated by Django 3.1.1 on 2020-09-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metabolite_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
