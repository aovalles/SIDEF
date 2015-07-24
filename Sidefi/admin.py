from django.contrib import admin
from Sidefi.models import Regional, Distrito, Centro, Individuo, Altura, Peso, IMC, UserProfile, Visita, Parametros
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


#definir un inline admin descriptor para el modelo del perfil del usuario
class PerfilInline(admin.StackedInline):
    model = UserProfile
    #can_delete = False
    #verbose_name = "Perfil del usuario"

    #readonly_fields = ['telefon', 'extension', 'celular']

#Definir un nuevo usuario admin que hereda de UserAdmin
class UserAdmin(UserAdmin):
    inlines = (PerfilInline,)



class RegionalAdmin(admin.ModelAdmin): 
    list_display = ('nombre', 'ubicacion', 'direccion', 'telefono')
    search_fields = ('nombre', 'ubicacion', 'direccion') 
    list_filter = ('ubicacion',) 


class CentroAdmin(admin.ModelAdmin): 
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre',) 
    list_filter = ('distrito',) 


class DistritoAdmin(admin.ModelAdmin): 
    list_display = ('nombre', 'regional', 'direccion') 
    search_fields = ('nombre', 'direccion') 
    list_filter = ('regional',) 


class IndividuoAdmin(admin.ModelAdmin): 
    list_display = ('nombre', 'genero', 'fecha_nac', 'centro') 
    search_fields = ('nombre',) 
    list_filter = ('genero',) 


class AlturaAdmin(admin.ModelAdmin): 
    list_display = ('genero', 'edad', 'dem3', 'dem2', 'dem1', 'mediana','de1', 'de2', 'de3') 


class PesoAdmin(admin.ModelAdmin): 
    list_display = ('genero', 'edad', 'dem3', 'dem2', 'dem1', 'mediana','de1', 'de2', 'de3') 


class IMCAdmin(admin.ModelAdmin): 
    list_display = ('genero', 'edad', 'dem3', 'dem2', 'dem1', 'mediana','de1', 'de2', 'de3') 


class ParametroAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'fecha_ref', 'estatus')


class VisitaAdmin(admin.ModelAdmin):
    list_display = ('edad', 'pesoVisita', 'alturaVisita', 'imcVisita',
     'pesoReferencia', 'alturaReferencia', 'imcReferencia')
    

    search_fields = ('nombre',) 

admin.site.register(Regional, RegionalAdmin)
admin.site.register(Distrito, DistritoAdmin)
admin.site.register(Centro, CentroAdmin)
admin.site.register(Individuo, IndividuoAdmin)
admin.site.register(Visita, VisitaAdmin)
admin.site.register(Altura, AlturaAdmin)
admin.site.register(Peso)
admin.site.register(IMC)
admin.site.register(Parametros)
#admin.site.register(UserProfile, UserProfileAdmin)

# Registrar el nuevo modelo UserAdmin
admin.site.unregister(User)

admin.site.register(User, UserAdmin)