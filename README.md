# Proyecto Informatorio: Chaco17al30

## Integrantes:
- Pereyra Marcos Gabriel
- Delgado Gonzalo Nicolas
- Barreto Santiago Emanuel

## Chaco17al30
En 2015, la ONU aprobó la Agenda 2030 sobre el Desarrollo Sostenible, una oportunidad para que los países y sus sociedades emprendan un nuevo camino con el que mejorar la vida de todos, sin dejar a nadie atrás. La Agenda cuenta con 17 Objetivos de Desarrollo Sostenible, que incluyen desde la eliminación de la pobreza hasta el combate al cambio climático, la educación, la igualdad de la mujer, la defensa del medio ambiente o el diseño de nuestras ciudades.\
Es por eso que decidimos crear un Blog que permita dar a conocer los 17 objetivos a la comunidad para que puedan espresar sus ideas de cómo poder lograrlo.\
Solo hay una manera en la que podremos defender este mundo, el único hogar que tenemos, y es aprender juntos a superar nuestras propias limitaciones y convencernos de que el cambio que necesitamos empieza por nosotros mismos.

## Detalles de la Configuración
_Este proyecto cuenta con la base de datos de MySQL, asi que para mayor fiabilidad recomendamos utilizar esa._

Para poder acceder a configuración debemos ir a la carpeta `settings/` 

_gráfico de cómo encontrarlo:_
```
Proyecto_informatorio/
        ├ apps/
        ├ media/
        ├ Proyecto_informatorio/
        |       └ settings/
        |       |       └ base.py
        |       └ __init__.py
        |       └ asgi.py
        |       └ urls.py
        |       └ views.py
        |       └ wsgi.py
        ├ static/
        ├ templates/
        ├ .gitignore
        ├ manage.py
        ├ README.md
        └ requirement.txt
```
Luego crear un archivo llamado `local.py` en donde importaremos todas las configuraciones de `base.py` de la siguiente manera y configuraremos la conexión a la base de datos con MySql _(en caso de ocupar otra base de datos averiguar por su cuenta)_:
```
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "NAME": "DATABASE_NAME",
        "USER": "USERNAME",
        "PASSWORD": "PASSWORD",
        "HOST": "localhost",
        "PORT": "3306"
    }
}
```
