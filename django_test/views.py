import http

from django.http import HttpResponse

from django.shortcuts import render


def saludo(request):
    return HttpResponse("hola estoy probanmdo devuelta")


def comer(request):
    return HttpResponse("adoro comer comida")


def plantilla(request):
    return render(request, 'plantilla.html', context={})

