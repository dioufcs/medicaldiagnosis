from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

def login_view(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #next_page = request.POST['next_page']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #if next_page:
                #return HttpResponseRedirect(next_page)
            return redirect(settings.LOGIN_REDIRECT_URL)
        #else:
            #error_message = "User does not exist. Please try again!"
            #return render(request, 'registration/login.html',
                          #{'usernameTyped': username, 'errorMessage': error_message})
    #if request.GET.get('next'):
        #next_page = request.GET.get('next')
        #return render(request, 'registration/login.html', {"next_page": next_page})
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    #request.session['lastConnectionDate'] = str(datetime.datetime.now())
    return redirect('home')

def home_view(request):
	 return render(request, 'home.html')