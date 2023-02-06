from posixpath import abspath
from typing import KeysView
from django.db.models.query import InstanceCheckMeta
from django.template import RequestContext
from numpy import dtype
import csv

from main import resume_parser
from .models import Document, Education, Experience, Resumes, Score, Skills,user_directory_path
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
import os,zipfile,subprocess,sys
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from pdf2docx import Converter,parse
from main.resume_parser import resumeparse
from .source import perform_parsing


# dataa = resumeparse.resumeparse.read_file(r'C:\Users\noman\Downloads\abhy.docx')
# for key, value in dataa.items():
#     print(key, ' : ')
#     for value in key:
#         print(value)




def index(request):
       return render(request,'index.html')

def uploadresumes(request): 
   return render(request,'uploadresumes.html')

def aboutus(request): 
    return render(request,'aboutus.html')

def iterator(lst):
    i=0
    for x in lst:
        print("***",i,"  ",x,"  ","***\n")
        i=i+1

def save_degree(lst,res):
    for x in lst:
        edu=Education()
        if x != None:
            edu.degree=x
            edu.resume_id=res
            edu.save()

def save_institute(lst,res):
    for x in lst:
        edu=Education()
        if x != None:
            edu.institute=x
            edu.resume_id=res
            edu.save()

def save_skills(lst,res):
    for x in lst:
        ski=Skills()
        if x != None:
            ski.total_skills=x
            ski.resume_id=res
            ski.save()

# def save_designitions(lst,res):
#     for x in lst:
#         exp=Experience()
#         exp.designition=x
#         exp.resume_id=res
#         exp.save()


def contactus(request): 
    return render(request,'contactus.html')


def form(request):
    return render(request, "index/form.html", {})


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.docx','.zip']
    if not ext.lower() in valid_extensions:
        #raise ValidationError('Unsupported file extension.')
        return 0

def validate_file_extension_zip(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.zip']
    if ext.lower() in valid_extensions:
        #raise ValidationError('Unsupported file extension.')
        return 1

# def validate_file_extension_pdf(value):
#     ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
#     valid_extensions = ['.pdf']
#     if ext.lower() in valid_extensions:
#         #raise ValidationError('Unsupported file extension.')
#         return 1



def calculate_experiec(a):
    if a != None:
        if a <=1:
            return 5
        elif a<5:
            return 10
        elif a <8:
            return 15
        else:
            return 20 


def calculate_uni_score(a):
    with open(r"C:\Users\noman\projects\AutomaticResumeRanking\main\Ranking.csv",newline='', encoding='cp1252',errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        score = 0
        for uni in a:
            for row in csv_reader:
                if(uni == row[0]):
                    score+=row[2]
                    break
        if(score<50):
            return 50
        else:
            return score



def calculate_degree_score(a):
    with open(r"C:\Users\noman\projects\AutomaticResumeRanking\main\dig.csv",newline='', encoding='cp1252',errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        score = 0
        for digi in a:
            dig = digi.lower()
            if(dig.find("bachelor")>=0 or dig.find("bachelor's")>=0 or dig.find("bachelors")>=0):
                score+= 15
            elif(dig.find("associate")>=0):
                score+= 20
            elif(dig.find("master")>=0 or dig.find("masters")>=0 or dig.find("master's")>=0):
                score+= 25
            elif(dig.find("doctoral")>=0):
                score+= 35
            else:
                for row in csv_reader:
                    if(row[0].lower().find(dig)>-1 or row[1].lower().find(dig)>-1):
                        score+=row[3]
            
        if(score<10):
            return 10
        else:
            return score


           





def perform_scoring(dic):
    edu =dic['degree']
    uni = dic['university']
    skils = dic['skills']
    exp = dic['total_exp']

    
def upload(request):
    if request.method == 'POST' and request.FILES.getlist("files"):
        files=request.FILES.getlist("files")
        Resumes.objects.all().delete()
        pre1='C:/Users/noman/projects/AutomaticResumeRanking/media/Users/user_'
        current_user1=request.user
        post1=current_user1.username
        path1=pre1+post1+'/'

        if(os.path.exists(pre1+post1)):
            filesToRemove = [os.path.join(path1,f) for f in os.listdir(path1)]
            for f in filesToRemove:
                os.remove(f)

       
        
    
        for f in files:
            if(validate_file_extension(f)==0):
                messages.info(request,'Include Invalid Format File')
                return redirect('uploadresumes')
        
        for f in files:
            if (validate_file_extension_zip(f)==1):
                pre='media/Users/user_'
                current_user=request.user
                post=current_user.username
                path=pre+post
                with zipfile.ZipFile(f) as item: # treat the file as a zip
                    item.extractall(path=path)  # extract it in the working directory
            else:
                newdoc = Document(docfile=f)
                newdoc.owner = request.user
                newdoc.save()

        #  Converting pdf files into docs   
        # pre2='C:/Users/noman/projects/AutomaticResumeRanking/media/Users/user_'
        # current_user2=request.user
        # post2=current_user2.username
        # path2=pre2+post2+'/'
        # for file in os.listdir(path2):
        #     if file.endswith('.pdf'):
        #         cv = Converter(path2+file)
        #         cv.convert((path2+file)+'.docx', start=0, end=None,multi_processing=True)
        #         cv.close()
        #         print(file)
        #         os.remove(os.path.join(path2, file))
        ####################################################################################
        dic=perform_parsing(path1)

        for dataa in dic:
            ###################################################################################3
            print("\n  ****  \n")
            print(dataa)
            res=Resumes()
            res.user = request.user
            if dataa['name'] != None:
                res.person_name=dataa['name']
                res.save()
            if dataa['email'] != None:
                res.contact=dataa['email']
                res.save()
            ###################################################################################
            exp=Experience()
            x=dataa['total_exp']
           
            if dataa['total_exp'] != None:
                exp.experience_time=dataa['total_exp']
                exp.resume_id=res
                exp.save()

            if dataa['designition'] != None:
                exp.designition=dataa['designition']
                exp.resume_id=res
                exp.save()

            ###################################################################################

            edu = dataa['degree']
            uni = dataa['university']
            skils = dataa['skills']
            des = dataa['designition']
            ####################################################################################
            save_degree(edu,res)
            save_institute(uni,res)
            save_skills(skils,res)
            # save_designitions(des,res)
            ####################################################################################
            
            

            temp_dd = calculate_uni_score(uni)
            temp_dd = temp_dd * (0.20)
            
            total = calculate_experiec(x) + calculate_degree_score(edu) + temp_dd + calculate_uni_score(uni) 


            sco=Score()
            sco.score=total
            sco.resume_id=res
            sco.save()
            ####################################################################################
        # resumes = Resumes.objects.all().filter(user_id=request.user.id)
        resumes = Resumes.objects.filter(user_id=request.user.id).order_by('-score_id__score')
        context={'resumes':resumes}
        return render(request,'Data.html',context)
    else:
        messages.info(request,'Input Files')
        return redirect('uploadresumes')



