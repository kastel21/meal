# Generated by Django 3.1.7 on 2021-09-01 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20210901_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specimensreceivedbrtiweekly',
            name='totalsamplescurrentpluscarryoverdbs',
        ),
        migrations.RemoveField(
            model_name='specimensreceivedbrtiweekly',
            name='totalsamplescurrentpluscarryoverplasma',
        ),
        migrations.AddField(
            model_name='specimensreceivedbrtiweekly',
            name='totalsamplescurrentandcarryoverdbs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='specimensreceivedbrtiweekly',
            name='totalsamplescurrentandcarryoverplasma',
            field=models.IntegerField(default=0),
        ),
    ]
