from django.contrib import admin

from .models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo','url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvalicaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'atualizacao', 'ativo')