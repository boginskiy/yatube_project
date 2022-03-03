from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Главная страница проекта "YATUBE"')

def group_posts(request, slug):
    return HttpResponse(f'Сообщение от пользователя: {slug}')
