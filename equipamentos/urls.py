from django.urls import path

from . import views


urlpatterns = [
    path('', views.equipamentos, name='equipamentos'),
    path('add_equipamento/', views.addEquipamentos, name='add_equipamento'),
    path('view_equipamento/<str:id>', views.viewEquipamento, name='view_equipamento'),
    path('del_equipamento/<str:id>', views.delEquipamento, name='del_equipamento'),
    # path('edit/<str:id>', views.update_setor, name='up_setor'),
    # path('delete/<str:id>', views.delete_setor, name='del_setor'),
    
    # Imagens
    path('del_imagem/<str:id>/<str:fk>', views.delImagem, name='del_imagem'),
]
