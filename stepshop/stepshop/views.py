from django.shortcuts import render


def index(request):
    return render(request, 'stepshop/index.html')


def contacts(request):
    return render(request, 'stepshop/contact.html')


def about(request):
    return render(request, 'stepshop/about.html')
