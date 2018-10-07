from django.urls import path
from .views import gh_list_prof
from .views import gh_cad_prof
from .views import gh_upd_prof
from .views import gh_del_prof

urlpatterns = [
    path('list_prof/', gh_list_prof, name='gh_list_prof'),
    path('cad_prof/', gh_cad_prof, name='gh_cad_prof'),
    path('upd_prof/<int:id>', gh_upd_prof, name='gh_upd_prof'),
    path('del_prof/<int:id>', gh_del_prof, name='gh_del_prof'),
]
