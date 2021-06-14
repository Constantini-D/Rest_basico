from rest_framework import serializers

from .models import Curso, Avaliacao, Aluno


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only' : True}
        }
        model = Avaliacao
        fields = (
            'id', 'curso', 'aluno', 'comentario', 'avaliacao', 'criacao', 'ativo'
        )

        def validate_avaliacao(self, valor):
            if valor in range(1, 10):
                return valor
            raise serializers.ValidationError('A avaliacao está incorreta! ela precisa estar entre 1 a 9,9')


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = (
            'id', 'titulo', 'url', 'criacao', 'ativo'
        )


class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = (
            'id', 'nome', 'email', 'inicio', 'criacao', 'ativo'
        )