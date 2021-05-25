from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-id']

    def __str__(self):
        return self.titulo


class Aluno(Base):
    nome = models.CharField(max_length=300)
    email = models.EmailField()
    inicio = Base.criacao

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f'{self.nome}'


class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, related_name='alunos', on_delete=models.CASCADE)
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['aluno', 'curso']

    def __str__(self):
        return f'{self.aluno} avaliou o curso {self.curso} com a nota {self.avaliacao}'


