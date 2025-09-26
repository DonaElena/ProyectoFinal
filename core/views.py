from django.http import HttpResponse
from django.shortcuts import render
from inscripcion_newsletter.forms import NewsletterForm

# Create your views here.
def home (request):

    return render(request,'home.html')