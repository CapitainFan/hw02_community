from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    latest = Post.objects.all()[:10]
    return render(request, 'posts/index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter()[:10]
    return render(request, 'posts/group_list.html',
                  {'group': group, 'posts': posts})
