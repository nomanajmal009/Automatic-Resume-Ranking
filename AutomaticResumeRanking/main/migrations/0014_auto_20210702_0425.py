# Generated by Django 3.2.3 on 2021-07-01 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210702_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='institute',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
