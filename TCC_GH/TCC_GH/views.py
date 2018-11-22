# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


def fncHello(request):
    return render(request, 'index.html')
    #return HttpResponse('<h1>Ola, pagina de resposta</h1><br><b>Em negrito</b><br>Normal.')


def listaLinks(request):
    return render(request, 'lista_links.html')
