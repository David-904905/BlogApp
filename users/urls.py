from django.urls import path
from . views import sign_up, login_view, user_logout, profile
from django.contrib.auth import views as auth_view
from . forms import CustomPasswordResetForm

urlpatterns = [
    path('sign-up', sign_up, name='sign-up'),
    path('login', login_view, name='login'),
    path('logout', user_logout, name='logout_link'),
    path('user-profile', profile, name='profile_link'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='users/password_reset.html', form_class=CustomPasswordResetForm), name='password_reset'),
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password+reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

]

