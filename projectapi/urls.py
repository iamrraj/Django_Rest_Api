"""projectapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework_jwt.views import obtain_jwt_token

from account.views import (login_view, register_view, logout_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('trangle.urls')),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('api/auth/token/', obtain_jwt_token),
    path('api/users/', include(("account.api.urls","api/users/"), namespace='users-api')),
    path('api/comments/', include(("comments.api.urls","api/comments/"), namespace='comments-api')),
    path('api/posts/', include(("posts.api.urls","api/posts/"), namespace='posts-api')),
    path('', include('Trang.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)