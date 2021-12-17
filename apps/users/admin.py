"""# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from apps.users.models import Profile


@admin.register(Profile) #Registra el modelo para que luego pueda verse
class ProfileAdmin(admin.ModelAdmin):
   

    list_display = ('pk', 'user', 'photo')  #Mostrara lista de usuarios
    list_display_links = ('pk', 'user',) #Editar campos especificos de un usuario
    list_editable = ('photo',) #editar la foto de un usuario

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
    )


    list_filter = (
        'user__is_active',
        'user__is_staff',
        'date_modified',
    )
    #Fieldsets = Permite customizar como se visualizarán los datos en el panel, en nuestro caso, profile
 #y metadata serían las cabeceras de los campos y dentro de fields si los datos están dentro
  #de una tupla aparecerán horizontalmente (nuestro caso), sino verticalmente.
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'photo', 'website'),),
        }),
        ('Extra info', {
            'fields': (('date_modified'),),
        })
    )

    readonly_fields = ('date_modified',) #Los datos que se añadan se mostraran como lectura

class ProfileInline(admin.StackedInline):
    #creamos el modelo que queremos añadir al modelo padre

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
   

    inlines = (ProfileInline,)

    #metemos los datos que queremos qeu se muestren al listar los usuarios
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)   
"""