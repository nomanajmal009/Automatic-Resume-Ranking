from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.core.validators import EMPTY_VALUES, MaxValueValidator, MinValueValidator
from django.conf import settings
#from django.db.models.fields import UUIDField
#import uuid

def user_directory_path(instance, filename):
    return 'Users/user_{0}/{1}'.format(instance.owner.username, filename)

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to=user_directory_path)


class Resumes(models.Model):
    resume_id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=150,null=True, blank=True)
    contact=models.CharField(max_length=150,null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Education(models.Model):
    education_id = models.AutoField(primary_key=True)
    degree = models.CharField(max_length=250,null=True, blank=True, default='')
    institute = models.CharField(max_length=500,null=True, blank=True, default='')
    # ,default=None, null=False
    resume_id = models.ForeignKey(Resumes,related_name='edu_id',on_delete=CASCADE)


class Experience(models.Model):
    experience_id = models.AutoField(primary_key=True)
    experience_time = models.PositiveIntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)],null=True, blank=True,default=0)
    designition=models.CharField(max_length=500,null=True, blank=True, default='')
    resume_id = models.ForeignKey(Resumes,related_name='exp_id',on_delete=CASCADE)


class Skills(models.Model):
    skill_id = models.AutoField(primary_key=True)
    total_skills = models.CharField(max_length=1000,null=True, blank=True, default='')
    resume_id = models.ForeignKey(Resumes,related_name='ski_id',on_delete=CASCADE)


class Score(models.Model):
    score = models.PositiveIntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    resume_id = models.ForeignKey(Resumes,related_name='score_id',on_delete=CASCADE)
