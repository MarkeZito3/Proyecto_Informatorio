from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.home'

class BlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'
