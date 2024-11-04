from django.shortcuts import render,redirect
from .models import Chat,User
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/login")
def index(request):
    return render(request, "chat/index.html")

@login_required(login_url="/users/login")
def room(request,room_name):
    chats=Chat.objects.filter(room_name=room_name)
    return render(request,"chat/room.html",{"room_name":room_name,"chats":chats})