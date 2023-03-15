from django.urls import path

from . import views


urlpatterns = [
    path('', views.equipamentos, name='equipamentos'),
    path('adicionar_equipamento/', views.addEquipamentos, name='add_equipamento'),


    path('adicionar_imagens/', views.addImagens, name='add_imagens')
    #path('edit/<str:id>', views.update_setor, name='up_setor'),
    #path('delete/<str:id>', views.delete_setor, name='del_setor'),
]
