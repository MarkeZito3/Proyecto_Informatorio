from django.contrib import admin


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    #permite modificar el display en admin
    list_display = ('title', 'id', 'status', 'author')
    #cuando se llenan los titulos de los post, tmb queremos
    #que los mismo sean un acceso url
    prepopulated_fields = {'slug': ('title',), }

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')

admin.site.register(models.category)
