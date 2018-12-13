from django.urls import path
from .views import list_disc, ins_disc, upd_disc, del_disc


urlpatterns = [
    path('list_disc/', list_disc, name='list_disc'),
    path('cad_disc/', ins_disc, name='cad_disc'),
    path('upd_disc/<int:id>', upd_disc, name='upd_disc'),
    path('del_disc/<int:id>', del_disc, name='del_disc'),
]
