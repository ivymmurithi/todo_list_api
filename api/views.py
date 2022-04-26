from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

from api.models import Todo
from .serializers import UserSerializer, TodoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer