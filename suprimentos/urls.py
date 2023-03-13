from django.urls import path

from . import views


urlpatterns = [
    path('', views.suprimentos, name='suprimentos'),
    #path('edit/<str:id>', views.update_setor, name='up_setor'),
    #path('delete/<str:id>', views.delete_setor, name='del_setor'),

    path('processos/', views.processos, name='processos_licitatorios'),
]
