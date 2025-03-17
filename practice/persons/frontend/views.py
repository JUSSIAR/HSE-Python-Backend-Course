from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def persons_list(request):
    return render(request, 'list.html', context={})


def person_create(request):
    return render(request, 'create.html', context={})