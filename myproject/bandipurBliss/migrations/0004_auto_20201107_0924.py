# Generated by Django 3.1.2 on 2020-11-07 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandipurBliss', '0003_auto_20201104_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='contact',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rooms',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
