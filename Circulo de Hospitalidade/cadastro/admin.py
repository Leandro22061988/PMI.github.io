from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Sobrescreve o título exibido na interface administrativa
    admin.site.site_header = 'Administração da Aplicação de  Refugiados'

# Registra o modelo CustomUser com a classe de administração personalizada
admin.site.register(CustomUser, CustomUserAdmin)
