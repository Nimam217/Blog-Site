from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'successfully logged in')
                    
                
        form=AuthenticationForm()
        context={'form':form}
        return render(request,'accounts/login.html',context)

    else:
        return redirect('/')


@login_required
def logout_view(request):
    logout(request)
    messages.error(request,'you logged out')
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'successfully signed up')
                return redirect(reverse('accounts:login'))
            else:
                messages.error(request,'somethings went wrong')
                
        form=UserCreationForm()
        context={'form':form}       
        return render(request,'accounts/signup.html',context)
   
    else:
        return redirect('/')
    
@login_required
def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'password successfully changed')
            
        else:
            messages.error(request,'somethings went wrong')
    form=PasswordChangeForm(user=request.user)
    return render(request,'accounts/change_password.html',context={'form':form})
