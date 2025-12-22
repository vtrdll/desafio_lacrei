from django.contrib import admin
from .models import Profissional


class ProfissionalAdmin(admin.ModelAdmin):

    list_display = ('nome', 'profissao')
    search_fields = ('nome', 'profissao')


admin.site.site_header = "Administração"
admin.site.register(Profissional, ProfissionalAdmin)
