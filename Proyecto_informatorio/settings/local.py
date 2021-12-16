#hice este archivo local para realizar las configuraciones en local sin tener que modificar el archivo settings principal que lo llamé "base.py"
#para saber porqué hice esto miren este video https://drive.google.com/file/d/1OV8Zo5wAqvD29VwsSz79xwocIkE5fzlo/view

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "NAME": "chaco17al30",
        "USER": "root",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "3306"
    }
}