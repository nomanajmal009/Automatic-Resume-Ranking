from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def signout(request):
    auth.logout(request)
    return redirect('/')


def signin(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('signin')
    else:
        return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Already Exists')
            return redirect('signup')
        elif password1!=password2:
            messages.info(request,'Password Didn,t Matched')
            return redirect('signup')
        else:
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            user.save()
            print('User Created')
            return redirect('signin')
    else:
         return render(request,'signup.html')
