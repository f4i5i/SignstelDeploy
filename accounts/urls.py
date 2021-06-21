from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from accounts import views
from django.conf.urls.static import static


urlpatterns = [
    path('register/',views.registerPage, name='register'),
    path('activate/<uidb64>/<token>',views.VerificationView.as_view(), name='activate'),
    path('login/',views.loginPage, name='login'),
    path('user/', views.userPage, name="user-page"),
    path('profile/', views.profile,name='profile'),
    path('logout/',views.logoutUser, name='logout'),
    path('password-reset/', 
            auth_views.PasswordResetView.as_view(
                template_name='accounts/password_reset.html'),
                name='password_reset'),
    path('password-reset/done/', 
            auth_views.PasswordResetDoneView.as_view(
                template_name='accounts/password_reset_done.html'),
                name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
            auth_views.PasswordResetConfirmView.as_view(
                template_name='accounts/password_reset_confirm.html'),
                name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'),
             name='password_reset_complete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)