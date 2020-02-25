from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'), name='logout'),
    path('accounts/signup', views.sign_up, name='signup'),
    path('accounts/edit_profile', views.edit_profile, name='edit_profile'),
    # path('password-reset', auth_views.password_reset, name='password_reset'),
    # path('password-reset/done', auth_views.password_reset_done, name='password_reset_done'),
    # path('password-reset/confirm/<int:id>', auth_views.password_reset_confirm, name='password_reset_confirm'),
    # path('password-reset/complete', auth_views.password_reset_complete, name='password_reset_complete'),
]
