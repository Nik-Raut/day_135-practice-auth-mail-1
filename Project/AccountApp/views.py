from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm



def registrationview(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='AccountApp/registration.html'
    context={'form':form}
    return render(request,template_name,context)


def loginview(request):
    if request.method == "POST":
        U = request.POST.get('un')
        P = request.POST.get('ps')
        user = authenticate(username=U,password=P)
        if user is not None:
            login(request,user)
            return redirect('home')
        else :
            messages.error(request,'Invalid Credentials')
    return render(request,'AccountApp/login.html')


def logoutview(request):
    logout(request)
    return redirect('login')


def changepasswordview(request):
    if request.method == "POST":

        UN = request.POST.get('un')
        OP= request.POST.get('ops')
        print('old p type:',type(OP),'old p:',OP)
        NP= request.POST.get('nps')
        print('New P type:', type(NP), 'New p:', NP)
        RP= request.POST.get('rnps')
        print('old p type:', type(NP), 'old p:', NP)
        user=authenticate(username=UN,password=OP)

        if user is not None:
            if NP == RP:
                user.set_password(NP)
                user.save()
                return redirect('login')
            else:
                messages.error(request, 'Password Not matched')
        else:
            messages.error(request, 'Invalid Credientials of Account')

    return render(request,'AccountApp/changepassword.html')


def passwordChangeview(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Your password was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'AccountApp/password-change.html', {
        'form': form
    })

