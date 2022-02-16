from django.shortcuts import render


# Create your views here.


def index(requests):
    return render(requests, 'site/index.html', {})


def catalog(requests):
    return render(requests, 'site/catalog.html', {})


def contacts(requests):
    return render(requests, 'site/contacts.html', {})


def product(requests):
    return render(requests, 'site/product.html', {})


