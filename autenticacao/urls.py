from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('cadastro_usuario/', views.cadastroUsuario, name="cadastro_usuario"),
    # Habilitar usuarios
    path('disable_usuario/<str:id>', views.disableUsuario, name="disable_usuario"),
    path('enable_usuario/<str:id>', views.enableUsuario, name="enable_usuario"),
    # Login // Logout
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    # Perfil do Usuario
    path('perfil_usuario/<str:id>', views.perfilUsuario, name="perfil_usuario"),
    # Redefinir Senha
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm_view.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), name="password_reset_complete"),
]
