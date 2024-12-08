"""
URL configuration for mySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('reg/', include("users.urls")),
    path('profile/', userViews.profile, name='profile'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name="user"),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('pass-reset/', authViews.PasswordResetView.as_view(template_name='users/pass-reset.html'), name='pass-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='users/password-reset-confirm.html'), name='password_reset_confirm'),
    path('password-reset-done/', authViews.PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'), name='password_reset_done'),
    path('password-reset-complete/', authViews.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'), name='password_reset_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)