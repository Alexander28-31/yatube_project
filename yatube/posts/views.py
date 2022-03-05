
from cgitb import text
import re
from django.http import HttpResponse
from django.shortcuts import render


# Главная страница
def index(request):
    text = 'Это главная страница проекта Yatube'
    template = 'posts/index.html'
    context = {'title': text}
    return render(request, template, context)


# Страница со списком мороженого
def group_posts(request):
    text ='Здесь будет информация о группах проекта Yatube'
    template = 'posts/index.html'
    context ={'main': text}
    return render(request, template, context)
    

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)




