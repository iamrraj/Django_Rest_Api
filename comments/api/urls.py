from django.urls import path
from django.contrib import admin

from .views import (
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,
  

    )

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list'),
    path('create/', CommentCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', CommentDetailAPIView.as_view(), name='thread'),
    #path('(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
