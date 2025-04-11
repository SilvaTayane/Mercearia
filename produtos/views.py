from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def visualizarloja(request):
    return render(request, 'loja/loja.html')

