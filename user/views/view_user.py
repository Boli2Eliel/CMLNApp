from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

#Resgistration
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from user.forms.form_user import UserUpdateForm, ProfileUpdateForm



# Create your views here

"""def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})"""

"""def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})"""

@login_required()
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Oups ,Cet utilisateur existe déjà !')
            return redirect("user-register")
        #elif User.objects.filter(email=email).exists():
            #messages.info(request, 'Come On, Email was already Taken !')
            #return redirect("user-register")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email,)
            mydict = {'username': username,
                      'password': password,
                      'email': email,
                      }
            user.save()
            #html_template = 'register_email/register_email.html'
            #html_message = render_to_string(html_template, context=mydict)
            #subject = "Bienvenue à IT'Watch-Suite"
            #email_from = settings.EMAIL_HOST_USER
            #recipient_list = [email]
            #message = EmailMessage(subject, html_message,
                                   #email_from, recipient_list)
            #message.content_subtype = 'html'
            #message.send()
            messages.success(request, 'Utilisateur enregistré avec success !')
            return redirect("user-register")
    else:
        return render(request, 'user/register.html')

def success(request, username=None):
    user = User.objects.create_user(username=username)
    mydict = {'username': username}
    return render(request, "user/success.html", mydict)


#========PROFIL & PROFILE UPDATE=========

@login_required()  # on met ce "decorators" partout où l'on veut que le user soit connecté avant d'y acceder
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid:
            profile_form.save()
            return redirect('user-profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user)

    context ={
        'profile_form': profile_form
    }
    return render(request, 'user/profile.html', context)

@login_required() #"LOGIN_URL = 'user-login'" # for decorators a été ajouté dans le settings
def profile_update(request):
    if request.method == 'POST':
        #user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        #if user_form.is_valid and profile_form.is_valid:
        if profile_form.is_valid:
            #user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

    context ={
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'user/profile_update.html', context)

# ========END PROFILE & PROFILE UPDATE========
