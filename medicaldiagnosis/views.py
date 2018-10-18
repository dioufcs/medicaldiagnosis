from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
from django.core.validators import validate_email



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

def reset_password_view(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method == "POST":
        email = request.POST['email']
        #secret = request.POST['secret']
        try:
            validate_email(email)
        except ValidationError as e:
            errorMessage = "Your email is not valid"
            return render(request, 'registration/password_reset.html', {'errorMessage': errorMessage})
        else:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                errorMessage = "Your email does not exist in our data"
                return render(request, 'registration/password_reset.html', {'errorMessage': errorMessage})
            #else:
                #user_secret = user.user_info.secret_key
                #if user_secret != secret:
                    #errorMessage = "Your secret key does not match"
                    #return render(request, 'registration/password_reset.html', {'errorMessage': errorMessage})
            else:
                password = User.objects.make_random_password()
                msg_plain = render_to_string('password_reset.txt',
                    {'username': user.username, "password": password})


                try:
                    msg = EmailMessage(
                        'Request for resetting password',
                        msg_plain,
                        'dic1.2016.2017@gmail.com',
                        [email],
                    )
                    msg.send()
                except:
                    pass
                user.set_password(password)
                user.save()
                return render(request, 'registration/password_reset.html', {"successMessage": "success"})
    return render(request, 'registration/password_reset.html')

def password_change_view(request):
    if request.method == "POST":
        oldpassword = request.POST['oldpassword']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if ((password1 != password2) or (password1 == "")):
            errorMessage = "New password sould not be empty and should be the same than the repeated password"
            return render(request, 'registration/password_change.html', {"errorMessage": errorMessage})
        if request.user.check_password(oldpassword):
            request.user.password = password1
            successMessage = "Your password has been successfully changed"
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(password1)
            u.save()
            login(request, u)
            return render(request, 'registration/password_change.html', {"successMessage": successMessage})
        else:
            errorMessage = "Your current password is not correct. Please, provide a correct one"
            return render(request, 'registration/password_change.html', {"errorMessage": errorMessage})
    return render(request, 'registration/password_change.html')