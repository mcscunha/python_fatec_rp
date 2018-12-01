from django.urls import path
from .views import list_cursos
from .views import ins_cur
from .views import upd_curso
from .views import del_curso

urlpatterns = [
    path('list_cursos/', list_cursos, name='list_cursos'),
    path('cur_cad_cur/', ins_cur, name='cur_cad_curso'),
    path('cur_upd_curso/<int:id>', upd_curso, name='cur_upd_curso'),
    path('cur_del_curso/<int:id>', del_curso, name='cur_del_curso'),

]
