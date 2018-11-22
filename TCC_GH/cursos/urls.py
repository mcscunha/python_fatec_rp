from django.urls import path
from .views import list_cursos

urlpatterns = [
    path('list_cursos/', list_cursos, name='list_cursos'),

]
