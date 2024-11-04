from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Users
from django.contrib.auth import login,logout
def users_list(request):
    users=Users.objects.all().order_by("-date")
    return render(request,'users/user_list.html',{'users':users})
def user_page(request,userid):
    user=Users.objects.get(userid=userid)
    return render(request,'users/user_page.html',{'user':user})
def user_register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("posts:list")
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())

            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("posts:list")
    else:

        form=AuthenticationForm()

    return render(request,'login.html',{'form':form})
def user_logout(request):
    if request.method=="POST":
        logout(request)
        return redirect("/")