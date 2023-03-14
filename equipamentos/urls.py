from django.urls import path

from . import views


urlpatterns = [
    path('', views.equipamentos, name='equipamentos'),
    #path('edit/<str:id>', views.update_setor, name='up_setor'),
    #path('delete/<str:id>', views.delete_setor, name='del_setor'),
]
