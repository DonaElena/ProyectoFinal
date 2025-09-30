from django.http import HttpResponse
from django.shortcuts import render
from core.textos import cargar_texto

# Create your views here.
def home (request):

    return render(request,'home.html')

def sobre_nosotros (request):

    contexto = {'filosofia': cargar_texto('filosofía.txt'),
                'quienes_somos': cargar_texto('quienes_somos.txt'),
                'propositos': cargar_texto('propositos.txt'),
                'valores_ambientales': cargar_texto('valores_ambientales.txt'),
                'valores_tecnicos': cargar_texto('valores_tecnicos.txt')}

    return render(request,'sobre_nosotros.html',contexto)