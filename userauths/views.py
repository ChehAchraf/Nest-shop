from django.shortcuts import render , redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate , logout , get_user_model
from django.contrib import messages
from django.conf import settings

User = get_user_model()

# Create your views here.

def register_view(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username} Your account was created seccessfully")
            new_user = authenticate(username=form.cleaned_data.get("username"),password=form.cleaned_data.get('password'))
            login(request,new_user)
            return redirect('core:index')
    else:
        form = UserRegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'userauths/sign-up.html',context)

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "easy captain, you already logged in 🙂")
        
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, f"user with {email} doenst exists")
            return redirect('userauths:sign-in')
            
        user = authenticate(request, email=email,password=password)
        
        if user is not None : 
            login(request,user)
            messages.success(request,"You logged in")
            return redirect("core:index")
        else:
            messages.warning(request,"user does not exists, create an account please 😁👌")
    context={
        
    }
            
    return render(request,"userauths/sign-in.html" , context)

def logout_view(request):
    logout(request)
    return redirect('userauths:sign-in')