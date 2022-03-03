from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Главная страница
def index(request):
    return HttpResponse('Главная страница')

# Страница со списком мороженного
def ice_cream_list(request):
    return HttpResponse('Список мороженного')

# Страница с информацией об одном сорте мороженного
# view-функция принимает параметр pk из path()

def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженное номер {pk}')
