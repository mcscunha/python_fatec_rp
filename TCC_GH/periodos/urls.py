from django.urls import path
from .views import list_per, ins_per, upd_per, del_per


urlpatterns = [
    path('list_per/', list_per, name='list_per'),
    path('cad_per/', ins_per, name='cad_per'),
    path('upd_per/<int:id>', upd_per, name='upd_per'),
    path('del_per/<int:id>', del_per, name='del_per'),
]
