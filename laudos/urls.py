from django.urls import path

from . import views

urlpatterns = [
    path('', views.pageLaudos, name='laudos'),
    path('inserir_laudo/', views.insLaudo, name='ins_laudo'),
    path('update_laudo/<str:id>', views.upLaudo, name='up_laudo'),

    # Deletar itens do laudo
    path('delete_item/<str:id>', views.delItem, name='delete_item'),
]
