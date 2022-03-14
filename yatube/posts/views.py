from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Post, Group
from django.shortcuts import render, get_object_or_404

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {'posts': posts,}
    return render(request, 'posts/index.html', context)
    #template = 'posts/index.html'
    #title = 'Последние обновления на сайте'
    #main_page = 'Это главная страница проекта Yatube'
    #context = {'title': title, 'main_page':  main_page}
    #return render(request, template, context)


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

    #template = 'posts/group_list.html'
    #title = 'Лев Толстой – зеркало русской революции.'
    #second_page = 'Здесь будет информация о группах проекта Yatube'
    #context = {'title': title, 'second_page': second_page, 'slug': slug}
    #return render(request, template, context)

    #posts = Post.objects.order_by('-pub_date')[:10]

#def group_posts(request, slug):
    #return HttpResponse(f'Сообщение от пользователя: {slug}')




