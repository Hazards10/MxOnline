# Generated by Django 2.2 on 2019-08-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='手机号码'),
        ),
    ]
