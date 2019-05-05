"""ihm_diner/diner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .views import *

urlpatterns = [
    path('', UserCreate.as_view(), name="login"),
    path('admin/', index, name='index'),
    path('regular/', index_regular, name='index_regular'),
    # Regular
    path('regular/sol_estudiante', SolicitudPlatoCreate.as_view(), name='sol_estudiante'),
    path('regular/list_solicitud/', SolicitudPlatoList.as_view(), name='list_solicitud'),
    path('regular/del_solicitud/<pk>', SolicitudPlatoDelete.as_view(),
         name='del_solicitud'),
    # Administrador
    # Plato
    path('admin/reg_plato/', PlatoCreate.as_view(), name='reg_plato'),
    path('admin/list_plato/', PlatoList.as_view(), name='list_plato'),
    path('admin/edit_plato/<pk>', PlatoUpdate.as_view(), name='edit_plato'),
    path('admin/del_plato/<pk>', PlatoDelete.as_view(), name='del_plato'),
    # Estudiante
    path('admin/reg_estudiante/', EstudianteCreate.as_view(), name='reg_estudiante'),
    path('admin/list_estudiante/', EstudianteList.as_view(), name='list_estudiente'),
    path('admin/edit_estudiante/<pk>', EstudianteUpdate.as_view(), name='edit_estudiante'),
    path('admin/del_estudiante/<pk>', EstudianteDelete.as_view(), name='del_estudiante')
]
