"""apile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static
from pile import views
from pile.backends import MyRegistrationView
from django.contrib.auth.views import (PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView, )



urlpatterns = [
    path('', views.index, name='home'),
   
    path('accounts/password/reset/', PasswordResetView.as_view (template_name='registration/password_reset_form.html'), name="password_reset_form"),

    path('accounts/password/reset/done', PasswordResetDoneView.as_view (template_name='registration/password_reset_done.html'), name='password_reset_done'),

    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view (template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),

    path('accounts/password/done', PasswordResetCompleteView.as_view (template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),

    path('accounts/create_post/', views.create_post, name='create_post'),

    path('posts/<slug>/', views.post_detail, name='post_detail'),

    # path('posts/<slug>/create_comment/', views.create_comment, name='create_comment'),

    path('posts/<slug>/edit/', views.edit_post, name="edit_post"),

    path('posts/<int:post_id>/favorite/', views.change_favorite, name="change_favorite"),

    path('posts/<int:post_id>/delete', views.delete_post, name='delete_post'),

    path('posts/<int:comment_id>/deletecomment', views.delete_comment, name='delete_comment'),

    # path('favorites/', views.favorites_index, name='favorites_index'),

    path('accounts/', include('registration.backends.simple.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
