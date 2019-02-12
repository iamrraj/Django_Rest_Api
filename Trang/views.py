from django.shortcuts import render
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
# snippets/views.py
from posts.api.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from .models import Trangle
from .serializers import SnippetSerializer

class TriangleList(generics.ListCreateAPIView):
    queryset = Trangle.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SnippetSerializer


class TriangleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trangle.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SnippetSerializer