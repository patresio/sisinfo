from django.urls import path

from . import views

urlpatterns = [
    path('', views.pageLaudos, name='laudos'),
    path('inserir_laudo/', views.insLaudo, name='ins_laudo'),
    # path('delete/<str:id>', views.delete_setor, name='del_setor'),
]
