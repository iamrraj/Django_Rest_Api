# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Trang import views

urlpatterns = [
    path('api/triangle/', views.TriangleList.as_view()),
    path('api/triangle/<int:pk>/', views.TriangleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)