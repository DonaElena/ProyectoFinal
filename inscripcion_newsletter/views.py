from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from inscripcion_newsletter.forms import NewsletterForm
from inscripcion_newsletter.email import enviar_correo_bienvenida

def inscripcion_newsletter(request):

    if request.method=='POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email_usuario=form.cleaned_data['email']
            enviar_correo_bienvenida(email_usuario)
            messages.success(request,'Bienvenido/a a nuestro Newsletter!!')
    return redirect(request.META.get('HTTP_REFERER','/'))








# Create your views here.
