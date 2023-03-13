from django.urls import path

from . import views


urlpatterns = [
    path('', views.suprimentos, name='suprimentos'),
    path('edit_material/<str:id>', views.update_suprimento, name='up_suprimento'),
    path('delete_material/<str:id>', views.delete_suprimento, name='del_suprimento'),

    path('processos/', views.processos, name='processos_licitatorios'),
    path('edit_processo/<str:id>', views.update_processo, name='up_processo'),
    path('delete_processo/<str:id>', views.delete_processo, name='del_processo'),

    path('cpucompleto/', views.cpucompleto, name='cpucompleto'),
]
