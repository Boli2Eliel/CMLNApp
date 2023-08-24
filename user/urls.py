from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from user.views import view_user

# User
urlpatterns = [
    #path('register/', view_user.register, name="user-register"),
    path('success/', view_user.success, name="success"),

    path('profile/', view_user.profile, name='user-profile'),
    path('profile/update/', view_user.profile_update, name='user-profile-update'),

    #path('accounts/login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),

    # ResetPassword
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
         name='password_reset'),

    # ResetPasswordDone
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),

    # ResetPasswordConfirm
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),  # -->uidb64 and 'token' are sourced from the confirmview error by django admin

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),

]