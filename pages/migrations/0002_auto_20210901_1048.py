# Generated by Django 3.1.7 on 2021-09-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimensreceivedcovid19',
            name='samplesreferredtoname',
            field=models.IntegerField(default=0),
        ),
    ]