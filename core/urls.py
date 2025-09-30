from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre_nosotros/',views.sobre_nosotros, name='sobre_nosotros'),
]

