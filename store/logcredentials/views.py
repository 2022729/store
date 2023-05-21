from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def computer(request):
  return render(request,"Computer.html")
def commerce(request):
  return render(request,"Commerce.html")
def chemistry(request):
  return render(request,"Chemistry.html")
def zoology(request):
  return render(request,"Zoology.html")
def english(request):
  return render(request,"English.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']

        email=request.POST['email']
        password=request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email address already exist")
                return redirect( 'register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
           messages.info(request,"Password not matching")
           return redirect('register')
        return redirect('/')
    return render(request,"register.html")
