# Generated by Django 3.2.3 on 2021-05-25 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('titulo', models.CharField(max_length=255)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('comentario', models.TextField(blank=True, default='')),
                ('avaliacao', models.DecimalField(decimal_places=1, max_digits=2)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='cursos.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='cursos.curso')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
    ]
