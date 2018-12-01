from django.urls import path
from .views import list_sem, ins_sem, upd_sem, del_sem


urlpatterns = [
    path('list_sem/', list_sem, name='list_sem'),
    path('cad_sem/', ins_sem, name='cad_sem'),
    path('upd_sem/<int:id>', upd_sem, name='upd_sem'),
    path('del_sem/<int:id>', del_sem, name='del_sem'),
]
