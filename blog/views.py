from django.shortcuts import render, redirect
from . forms import *
from . models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
# You can use cripsy forms to style your form

@login_required(login_url='login')
def home(request):
    posts = PostModel.objects.all()
    form = PostModelForm()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/')
    context = {'posts': posts, 'form' : form}
    return render(request, 'blog/index.html', context)

@login_required(login_url='login')
def post_detail(request, pk):
    post  = PostModel.objects.get(id=pk)
    com_form = CommentForm()
    if request.method == 'POST':
        com_form = CommentForm(request.POST)
        if com_form.is_valid():
            comment = com_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post-detail-link', post.id)
    context = {
        'post':post,
        'c_form':com_form
    }
    return render(request, 'blog/post_detail.html', context)

@login_required(login_url='login')
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    pid = post.id
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail-link', pk=pid)
    else:
        form = PostEditForm(instance=post)
    context = {
        'post': post,
        'form':form
    }
    return render(request, 'blog/post_edit.html', context)
@login_required(login_url='login')
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    context = {'post' : post}

    if request.method == 'POST':
        post.delete()
        return redirect('homepage')
    
    return render(request, 'blog/post_delete.html', context)
