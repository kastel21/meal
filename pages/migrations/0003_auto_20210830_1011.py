# Generated by Django 3.1.7 on 2021-08-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_customuser_lab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reasonsforfailurebrtivleid',
            name='lab',
        ),
        migrations.RemoveField(
            model_name='reasonsforfailurebrtivleid',
            name='user',
        ),
        migrations.RemoveField(
            model_name='specimensreceivedcovid19',
            name='lab',
        ),
        migrations.RemoveField(
            model_name='specimensreceivedcovid19',
            name='user',
        ),
        migrations.RemoveField(
            model_name='specimensruncovid19',
            name='dateofrecord',
        ),
        migrations.RemoveField(
            model_name='specimensruncovid19',
            name='lab',
        ),
        migrations.RemoveField(
            model_name='specimensruncovid19',
            name='reportingweek',
        ),
        migrations.RemoveField(
            model_name='specimensruncovid19',
            name='user',
        ),
        migrations.AddField(
            model_name='specimensrunbrtivleid',
            name='key',
            field=models.TextField(default='vl', max_length=5),
        ),
        migrations.AddField(
            model_name='specimensrunbrtivlweekly',
            name='key',
            field=models.TextField(default='vl', max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='lab',
            field=models.CharField(blank=True, choices=[('Victoria Falls', 'Victoria_Falls'), ('Bindura', 'Bindura')], max_length=200),
        ),
        migrations.AlterField(
            model_name='electricoutagebrtivlweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='electricoutagebrtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='generalbrticovid19',
            name='dayofweek',
            field=models.TextField(default='brti', max_length=30),
        ),
        migrations.AlterField(
            model_name='generalbrticovid19',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='generalcovid19',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='machinedowntimereagentstockouttoolbrticovid19',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='machinedowntimereagentstockouttoolcovid19',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reasonsforfailurebrtivleid',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reasonsforfailurebrtivlweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reasonsforfailurebrtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='specimensreceivedbrticovid19',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='specimensreceivedbrtivleid',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='specimensreceivedbrtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='specimensreceivedcovid19',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='specimensrecievedbrtivlweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='specimensrunbrticovid19',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtivleid',
            name='dayofweek',
            field=models.TextField(default='Total', max_length=30),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtivleid',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtivlweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='specimensrunbrtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='specimensruncovid19',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top3brtivlweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top3brtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top3covid19',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top4brtivlweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top4brtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top5brtivlweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top5brtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top61brtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top6brtivlweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top6brtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top7brtivlweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='top7brtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='topagesexdissagregationofallspecimensreceivedbrtivlweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='topagesexdissagregationofallspecimensreceivedbrtiweekly',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='topagesexdissagregationofallspecimensreceivedcovid19',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
