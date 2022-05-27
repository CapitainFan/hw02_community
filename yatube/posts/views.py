from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    latest = Post.objects.all()[:10]
    return render(request, 'index.html', {'post': latest})


def group_posts(request, slug):
    template = 'posts /group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = Group.__str__
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
