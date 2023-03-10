from django.urls import path

from . import views


urlpatterns = [
    path('', views.diretorias, name='diretorias'),
    path('edit/<str:id>', views.update_diretoria, name='up_diretoria'),
    path('delete/<str:id>', views.delete_diretoria, name='del_diretoria'),
]
