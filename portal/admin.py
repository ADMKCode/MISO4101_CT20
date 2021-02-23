from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Deportista, Deporte, Participacion, Lugar, Video, Comentario


# Register your models here.
@admin.register(Deportista)
class DeportistaAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'peso', 'estatura', 'get_lugar_nacimiento')

    def get_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    def get_lugar_nacimiento(self, obj):
        return obj.lugar_nacimiento

    get_name.short_description = 'Nombre'
    get_lugar_nacimiento.short_description = 'Lugar de Nacimiento'


#@admin.register(User)
#class UsuarioRegistradoAdmin(admin.ModelAdmin):
#    list_display = ('get_name', 'email')

#    def get_name(self, obj):
#        return f'{obj.user.first_name} {obj.user.last_name}'

#    get_name.short_description = 'Nombre'


@admin.register(Deporte)
class DeporteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'tipo')


@admin.register(Participacion)
class ParticipacionAdmin(admin.ModelAdmin):
    list_display = ('deportista', 'deporte', 'fecha', 'hora', 'modalidad', 'resultado')


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ['departamento', 'ciudad']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['participacion', 'url']


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['get_usuario', 'fecha', 'get_participacion']

    def get_usuario(self, obj):
        return obj.usuario_registrado

    get_usuario.short_description = 'Usuario'

    def get_participacion(self, obj):
        return obj.video.participacion

    get_participacion.short_description = 'Participacion'


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = ((None, {
        'classes': ('wide',),
        'fields': (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ),
    }),)
