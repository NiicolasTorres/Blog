
from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.shortcuts import redirect

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