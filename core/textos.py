import os
from CuerdApp import settings


def cargar_texto(nombre_texto):

    ruta_txt = os.path.join(settings.BASE_DIR, f'core/texto/{nombre_texto}')
    with open(ruta_txt, encoding='utf-8') as f:
        texto = f.read()
    return texto