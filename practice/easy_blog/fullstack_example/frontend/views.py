from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def article_list(request):
    return render(request, 'list.html', context={})


def article_create(request):
    return render(request, 'create.html', context={})