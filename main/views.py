from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Post

# Create your views here.
#@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")
        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'main/home.html', {"posts":posts})

@login_required(login_url='/login')
@permission_required("main.add_post", login_url='/login', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {"form":form})

def user_profile(request, username):
    view_user = User.objects.get(username=username)
    posts = Post.objects.filter(author = view_user).order_by('-created_at')
    return render(request, 'main/user_profile.html', {"profile":view_user, "posts":posts})

def signin(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    
    return render(request, 'registration/signin.html', {"form": form})