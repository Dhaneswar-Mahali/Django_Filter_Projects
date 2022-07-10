from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from Django_Filter_App.forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.models import User
from Django_Filter_App.filters import UserFilter
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="/login/")
def Search_view(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET,queryset=user_list)
    context = {
        "filter" : user_filter,
    }
    return render(request, 'filterapp/search.html', context)

def RegisterView(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            email = request.POST.get('email','')
            password1 = request.POST.get('password1','')
            password2 = request.POST.get('password2','')

            if User.objects.filter(username=username,email=email).exists():
                messages.warning(request,f'This Username/email Already Taken')
                return redirect('register')

            if password1 != password2:
                messages.warning(request, f'your password and confirm password must be same required')
                return redirect('register')

            User.objects.create_user(
                username=username,first_name=first_name,last_name=last_name,email=email,password=password2
            )
            messages.success(request,f'Your Registration Done Successfully')
            return redirect('login')



        else:
            context = {
                'error': 'Registration Not Done Successfully'
            }
            return render(request,'filterapp/register.html',context)
    else:
        form = UserRegisterForm()
        context = {
            "form": form
        }
        return render(request,'filterapp/register.html',context)


def LoginView(request):
    if request.method=="POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)#object/None value
            if user is None:
                messages.warning(request,f'Invalid UserName and Password')
                return redirect('login')
            else:
                login(request,user)
                messages.success(request,f'Your Login Done Successfully')
                return redirect('search')
        else:
            context = {
                "error" : 'Invalid UserName/Password Check Again'
            }
            return render(request, 'filterapp/login.html', context)

    else:
        form = UserLoginForm()
        context = {
            "form" : form,
            "error" : 'Login Not Done Successfully'
        }
        return render(request,'filterapp/login.html',context)



def LogoutView(request):
    messages.success(request,f'You are Successfully Logged Out Now')
    return redirect('login')


