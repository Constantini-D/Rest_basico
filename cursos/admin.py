from django.contrib import admin

from .models import Curso, Avaliacao, Aluno


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo','url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'inicio', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvalicaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'aluno', 'comentario', 'avaliacao', 'criacao', 'atualizacao', 'ativo') # mudei nome e email para aluno

