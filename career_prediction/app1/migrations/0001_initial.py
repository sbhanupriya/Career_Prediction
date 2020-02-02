# Generated by Django 2.2.7 on 2019-11-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osmarks', models.IntegerField()),
                ('algomarks', models.IntegerField()),
                ('progmarks', models.IntegerField()),
                ('softmarks', models.IntegerField()),
                ('cnmarks', models.IntegerField()),
                ('electromarks', models.IntegerField()),
                ('coamarks', models.IntegerField()),
                ('mamarks', models.IntegerField()),
                ('commmarks', models.IntegerField()),
                ('workcap', models.IntegerField()),
                ('logical', models.IntegerField()),
                ('hackathon', models.IntegerField()),
                ('coding', models.IntegerField()),
                ('pubspeaking', models.IntegerField()),
                ('canwork', models.CharField(max_length=20)),
                ('selflearn', models.CharField(max_length=20)),
                ('extracurr', models.CharField(max_length=20)),
                ('certificates', models.CharField(max_length=200)),
                ('workshop', models.CharField(max_length=200)),
                ('talent', models.CharField(max_length=20)),
                ('olympiad', models.CharField(max_length=20)),
                ('readwrite', models.CharField(max_length=20)),
                ('retention', models.CharField(max_length=20)),
                ('interestsub', models.CharField(max_length=200)),
                ('interestca', models.CharField(max_length=200)),
                ('jobstudy', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('seniorhelp', models.CharField(max_length=200)),
                ('games', models.CharField(max_length=20)),
                ('prefsalarywork', models.CharField(max_length=20)),
                ('singlemingle', models.CharField(max_length=20)),
                ('gentlestubborn', models.CharField(max_length=20)),
                ('managetech', models.CharField(max_length=20)),
                ('hardsmart', models.CharField(max_length=20)),
                ('teamplayer', models.CharField(max_length=20)),
                ('introvert', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=250)),
            ],
        ),
    ]
