
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

# Главная страница

def index(request):
    title = "Это главная страница проекта Yatube"
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context) 
    
def group_posts(request, slug):
    title = "Здесь будет информация о группах проекта Yatube"
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context) 



