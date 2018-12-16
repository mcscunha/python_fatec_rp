from django.urls import path
from .views import list_disp, ins_disp, upd_disp, del_disp


urlpatterns = [
    path('list_disp/', list_disp, name='list_disp'),
    path('cad_disp/', ins_disp, name='cad_disp'),
    path('upd_disp/<int:id>', upd_disp, name='upd_disp'),
    path('del_disp/<int:id>', del_disp, name='del_disp'),
]
