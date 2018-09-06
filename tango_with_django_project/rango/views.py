
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': "Olá BSI6, este texto veio da view!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'autor': 'Felipe Tiago Guimarães'}
    return render(request, 'rango/about.html', context=context_dict)
