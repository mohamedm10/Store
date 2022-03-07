from calendar import c
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), 
                    password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('inventory:index', permanent=True)
        else:
            raise ValidationError('invalid credentials')
    return render(request, 'users/login.html')

@login_required()
def register(request):
    confirm_pass = request.POST.get('password-confirm')
    if request.method == 'POST' and request.POST.get('password') == confirm_pass:
        try:
            user = User.objects.create_user( 
            username = request.POST.get('username'), 
            email = request.POST.get('email'), 
            password = request.POST.get('password'), 
            is_staff = True
            )
            return redirect('inventory:index', permanent=True)
        except ValidationError as e:
            print(e)

    return render(request, 'users/register.html')

@login_required()
def signout(request):
    logout(request)
    return redirect('users:login', permanent=True)

def users(request):
    users = User.objects.all()
    
    context = {'users': users}
    return render(request, 'users/users.html', context)