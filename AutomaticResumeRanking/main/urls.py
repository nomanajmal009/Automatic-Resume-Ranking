from django.urls import path
from django.conf.urls import url
from . import views
from main.resume_parser import resumeparse

urlpatterns = [
    path('',views.index,name='index'),
    path('uploadresumes',views.uploadresumes,name='uploadresumes'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('form',views.form,name='form'),
    path('upload',views.upload,name='upload')
    #url(r'^form/$', views.Form),
    #url(r'^upload/$', views.upload)

]
