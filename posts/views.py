from pyexpat.errors import messages
from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import CommentForm, PostForm
from django.shortcuts import redirect
from login.models import User


# Create your views here.

def index(request):
    post = Post.objects.all()

    return render(request, 'index.html',{'post':post})

def post_detail(request,post_id):

    post = Post.objects.get(id=post_id)

    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.save()
            return redirect('post_detail',post_id= post_id)

    else:
        form = CommentForm
    
    return render(request, 'post_detail.html',{'post':post, 'comments':comments,'form':form})

def post(request):
    current_user=get_object_or_404(User, pk=request.user.pk)
    if request.method =='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=current_user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request,'post.html',{'form' : form})