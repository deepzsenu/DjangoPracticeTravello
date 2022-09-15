
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']

        user = auth.authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid cretentials')
            return redirect('login')

    else:
        return render(request, 'login.html')
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1== password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username all ready taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email all ready taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password= password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                return redirect('login')
                # return redirect('/')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
        # return redirect("/")

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')