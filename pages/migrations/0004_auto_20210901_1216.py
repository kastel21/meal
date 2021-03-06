# Generated by Django 3.1.7 on 2021-09-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210901_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='specimensrunbrtivlweekly',
            name='ncsclosedthisweek',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='specimensrunbrtiweekly',
            name='ncsclosedthisweek',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtivleid',
            name='ncsclosedthisweek',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtivleid',
            name='ncsnotyetclosed',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtivleid',
            name='totalncsfromaudit',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtivlweekly',
            name='ncsnotyetclosed',
            field=models.TextField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtivlweekly',
            name='totalncsfromaudit',
            field=models.TextField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtiweekly',
            name='ncsnotyetclosed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtiweekly',
            name='totalncsfromaudit',
            field=models.IntegerField(default=0),
        ),
    ]
