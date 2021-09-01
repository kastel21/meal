# Generated by Django 3.1.7 on 2021-08-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210831_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='electricoutagebrtivleid',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='electricoutagebrtivlweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='electricoutagebrtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='generalbrticovid19',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='generalcovid19',
            name='dateofrecord',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='generalcovid19',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='generalcovid19',
            name='reportingweek',
            field=models.TextField(default='.', max_length=30),
        ),
        migrations.AddField(
            model_name='generalcovid19',
            name='user',
            field=models.TextField(default='root', max_length=25),
        ),
        migrations.AddField(
            model_name='machinedowntimereagentstockouttoolbrticovid19',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='machinedowntimereagentstockouttoolcovid19',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='reasonsforfailurebrtivlweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='reasonsforfailurebrtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='specimensreceivedbrticovid19',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='specimensreceivedbrtivleid',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='specimensreceivedbrtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='specimensrecievedbrtivlweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='specimensrunbrticovid19',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='specimensrunbrtivleid',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='specimensrunbrtivlweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='specimensrunbrtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top3brtivlweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top3brtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top3covid19',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top4brtivlweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top4brtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top5brtivlweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top5brtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top61brtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top6brtivlweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top6brtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top7brtivlweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='top7brtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='topagesexdissagregationofallspecimensreceivedbrtivlweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='topagesexdissagregationofallspecimensreceivedbrtiweekly',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AddField(
            model_name='topagesexdissagregationofallspecimensreceivedcovid19',
            name='lab',
            field=models.TextField(default='brti', max_length=30),
        ),
    ]