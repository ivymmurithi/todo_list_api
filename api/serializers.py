from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email']

class TodoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','created_at','todo','done']
