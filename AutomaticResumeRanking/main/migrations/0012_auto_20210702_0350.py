# Generated by Django 3.2.3 on 2021-07-01 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210702_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='education',
            name='institute',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='experience',
            name='designition',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='resumes',
            name='contact',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='resumes',
            name='person_name',
            field=models.CharField(max_length=150),
        ),
    ]
