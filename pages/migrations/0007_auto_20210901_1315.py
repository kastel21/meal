# Generated by Django 3.1.7 on 2021-09-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210901_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specimensreceivedbrtivleid',
            name='samplescarriedoverpreviouspreviousfailedsamplesdbs',
        ),
        migrations.RemoveField(
            model_name='specimensreceivedbrtivleid',
            name='samplescarriedoverpreviouspreviousfailedsamplesplasma',
        ),
        migrations.RemoveField(
            model_name='specimensrecievedbrtivlweekly',
            name='samplescarriedoverpreviouspreviousfailedsamplesdbs',
        ),
        migrations.RemoveField(
            model_name='specimensrecievedbrtivlweekly',
            name='samplescarriedoverpreviouspreviousfailedsamplesplasma',
        ),
        migrations.AddField(
            model_name='specimensreceivedbrtivleid',
            name='samplescarriedoverpreviousfailedsamplesdbs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='specimensreceivedbrtivleid',
            name='samplescarriedoverpreviousfailedsamplesplasma',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='specimensrecievedbrtivlweekly',
            name='samplescarriedoverpreviousfailedsamplesdbs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='specimensrecievedbrtivlweekly',
            name='samplescarriedoverpreviousfailedsamplesplasma',
            field=models.IntegerField(default=0),
        ),
    ]
