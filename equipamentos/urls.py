from django.urls import path

from . import views


urlpatterns = [
    # Equipamentos
    path('', views.equipamentos, name='equipamentos'),
    path('add_equipamento/', views.addEquipamentos, name='add_equipamento'),
    path('view_equipamento/<str:id>',
         views.viewEquipamento, name='view_equipamento'),
    path('del_equipamento/<str:id>', views.delEquipamento, name='del_equipamento'),
    path('up_equipamento/<str:id>', views.upEquipamento, name='up_equipamento'),

    # Imagens
    path('del_imagem/<str:id>/<str:fk>', views.delImagem, name='del_imagem'),
    path('inserir_imagens/<str:fk>', views.insImagens, name='ins_imagens'),
]
