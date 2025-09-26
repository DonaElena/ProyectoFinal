from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import os

def enviar_correo_bienvenida(email_usuario):
    ruta_txt = os.path.join(settings.BASE_DIR, 'inscripcion_newsletter/email/texto_email.txt')
    with open(ruta_txt, encoding='utf-8') as f:
        email_txt=f.read()

    ruta_html = os.path.join(settings.BASE_DIR, 'inscripcion_newsletter/email/html_email.html')
    with open(ruta_html, encoding='utf-8') as f:
        html_email = f.read()

    asunto= '¡Bienvenido/a a nuestro Newsletter!'
    mi_email= settings.DEFAULT_FROM_EMAIL
    destinatario = [email_usuario]

    email = EmailMultiAlternatives(asunto,email_txt,mi_email,destinatario)
    email.attach_alternative(html_email,'text/html')
    email.send()

