
import http
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
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
                print("username allready taken")
            elif User.objects.filter(email=email).exists():
                print("email allready taken")
            user = User.objects.create_user(username=username, password= password1, first_name=first_name, last_name=last_name, email=email)
            user.save()
            print('user created')
        else:
            print("password not matching")
        return redirect("/")

    else:
        return render(request, 'register.html')