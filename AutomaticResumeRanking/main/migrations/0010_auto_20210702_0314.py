# Generated by Django 3.2.3 on 2021-07-01 22:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_auto_20210702_0303'),
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
            model_name='experience',
            name='experience_time',
            field=models.DecimalField(decimal_places=1, max_digits=10),
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
        migrations.AlterField(
            model_name='resumes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='skills',
            name='total_skills',
            field=models.CharField(max_length=1000),
        ),
    ]