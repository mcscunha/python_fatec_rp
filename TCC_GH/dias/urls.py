from django.urls import path
from .views import list_dias, ins_dia, upd_dia, del_dia


urlpatterns = [
    path('list_dias/', list_dias, name='list_dias'),
    path('dia_cad_dia/', ins_dia, name='dia_cad_dia'),
    path('dia_upd_dia/<int:id>', upd_dia, name='dia_upd_dia'),
    path('dia_del_dia/<int:id>', del_dia, name='dia_del_dia'),

]
