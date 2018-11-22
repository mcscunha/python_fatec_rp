"""TCC_GH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import fncHello, listaLinks
from home import urls as urls_home
from grade_horario import urls as gh_urls
from cursos import urls as cur_urls


urlpatterns = [
    path('', include(urls_home)),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('hello/', fncHello),
    path('admin/', admin.site.urls),
    path('list_links/', listaLinks, name='list_links'),

    path('gh/', include(gh_urls)),
    path('cur/', include(cur_urls)),
]
