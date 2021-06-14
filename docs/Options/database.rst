
****************************
Database Configuration REST
****************************

Create the models of the API
----------------------------

The models file is importante bacause it's this file that create the database of the API

First off all, in this project we need to create a Parents class named ``Base`` that will receive the data time of the  file creation ``criacao`` and the actualization ``atualizao`` and if the user it's online ``ativo``.

.. code:: python

    class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

After that we will create a child class named ``Curso``. This class will be responsible this Class will be responsible to receive a course name ``titulo`` and
url address ``url``

.. code:: python

    class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-id']

    def __str__(self):
        return self.titulo

The ``class Meta`` is responsible to give the verbose name to the API, verbose_name is a human-readable name for the field. If the verbose name isn’t given, Django will
automatically create it using the field’s attribute name, converting underscores to spaces.
And the function  ``def __str__(self):`` will print the variable ``titulo``.

The same thing will happen with the class Alunos

.. code:: python

    class Aluno(Base):
    nome = models.CharField(max_length=300)
    email = models.EmailField()
    inicio = Base.criacao

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f'{self.nome}'

In the ``class Avaliacao(Base):`` the variable will correlate the variable ``curso`` and ``aluno`` with the class ``Avaliacao`` and ``Aluno``.

In the ``class Meta`` the variable ``unique_together`` will be responsible to Sets of field names that, taken together, must be unique.

Create the Serializer of the API
_________________________________

Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered
into JSON, XML or other content types.

The serializer will receive the class created in the models and will be responsible to change the value os the class to a JSON type.
This file will also be responsible to allow conditions as if, for, ... (we gonna see a exemple latter in the ``def validate_avaliacao``

.. code:: python

    from .models import Curso, Avaliacao, Aluno

The down below code will show how the serializer works

.. code:: python

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

In the ``class Meta`` in the class AvaliacaoSerializar, will receive the Class Avaliacao from models and his
components as id, curso, aluno ...
Also will receive a extra_kwargs that will be responsible to online write in the email field

The function `validate_avalicao`  will be responsible to see if the variable `data` is in the range of 1 and 10, if not, the function will show a warning message
the others class will do the same thing as the ``AvaliacaoSerializer``

Create the Views of the API
___________________________

The view function is a Python function that takes a Web request and returns a Web response.

In this program, we will need to import the following things

.. code:: python

    from .models import Curso, Avaliacao, Aluno

import the class from the models

.. code:: python

    from .serializers import CursoSerializer, AvaliacaoSerializer, AlunoSerializer

Import the class created in the serializer file

.. code:: python

    from rest_framework import viewsets

The ``ViewSet`` function is a abstract logic of a CRUD function

.. code:: python

    from rest_framework.decorators import action

Use the decorators to  import a ``action`` command, that latter will be used to create a new route

.. code:: python

    from rest_framework.response import Response

``Response`` is a type of TemplateResponse that takes unrendered content and uses content negotiation to determine the correct content
type to return to the client.

Views class code
------------------

.. code:: python

    class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get']) # decorator que cria uma nova rota
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)

All the class will receive the imported viewsets, and the class will receive all values of the respective class from the models
and will set in a variable named `queryset`

the decorator ``@action`` will be responsible  to create a path using `get` methods to the `avaliacao` action.

.. code:: python

    class AvaliacaoViewSet(viewsets.ModelViewSet): #  se não quiser alguma função, basta usar o mixins. do botão ctrl no model viewSet no lugar do "viewsets.ModelViewSet
        queryset = Avaliacao.objects.all()
        serializer_class = AvaliacaoSerializer


    class AlunoViewSet(viewsets.ModelViewSet):
        queryset = Aluno.objects.all()
        serializer_class = AlunoSerializer

And this two class will do the same thing, they'll receive the serializer content, and will use the viewset class to create a CRUD action.

Create the urls in the core program
------------------------------------

This urls will be responsible to import the class from the views
.. code:: python

    from .views import CursoViewSet, AvaliacaoViewSet, AlunoViewSet

And the following function will help the user to create a simple router
.. code:: python

    from rest_framework.routers import SimpleRouter

After this, you'll just need to do the following process

.. code:: python

    router = SimpleRouter()
    router.register('cursos', CursoViewSet)
    router.register('avaliacoes', AvaliacaoViewSet)
    router.register('alunos', AlunoViewSet)

And import this to the urls app and add the route to the urlpatterns

.. code:: python

    from cursos.urls import router
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/', include(router.urls))
    ]