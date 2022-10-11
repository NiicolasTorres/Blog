
from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate

from posts.models import Post
from .forms import UserRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from posts.views import post

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request,usuario)
            return redirect("index")

    else: 
        form = UserRegisterForm()
    
    context = {'form':form}
    return render(request, 'register.html',context)

def profile(request, username=None):
    current_user=request.user
    if username and username != current_user.username:
        user=User.objects.get(username=username)
        post = user.post.all()
    else:
        post=current_user.posts.all()
        user=current_user

    return render(request, 'profile.html',{'user':user, 'post':post})