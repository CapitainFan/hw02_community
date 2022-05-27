from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    latest = Post.objects.all()[::-1]
    return render(request, 'posts/index.html', {'post': latest[:10]})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:10]
    return render(request, 'posts/group_list.html',
                  {'group': group, 'post': posts})
