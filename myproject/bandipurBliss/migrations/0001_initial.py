# Generated by Django 3.1.2 on 2020-11-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_num', models.IntegerField()),
                ('category', models.CharField(choices=[('BASIC', 'BASIC'), ('DELUX', 'DELUX'), ('PREMINUM', 'PRENIMUM')], max_length=9)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
