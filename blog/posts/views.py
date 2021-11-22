from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .models import Post, Feature
from django.contrib import messages
from .forms import *


# Create your views here.
def home(request):
    features = Feature.objects.all()    #getting all data(objects) from DB
    return render(request, 'home.html', {'features': features})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:
        return render(request, 'register.html')


# 로그인 views
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


# 로그아웃 views
def logout(request):
    auth.logout(request)
    return redirect('/')


def blog(request):
    username = None
    if request.user.username:
        username = request.user.username
    posts = Post.objects.all()
    return render(request, 'blog.html', dict(posts=posts, username=username))
    # return render(request, 'blog.html', {'posts': posts})


def post(request, pk):
    username = None
    if request.user.username:
        username = request.user.username
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', dict(posts=posts, username=username))


def write(request):
    username = None
    if request.user.username:
        username = request.user.username

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = Form()
    return render(request, 'write.html', {'form':form, 'username':username})