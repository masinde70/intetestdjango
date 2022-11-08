from rest_framework import serializers
from .models import ToDoItem, ToDoList

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem, ToDoList
        fields = ("id", "title", "description")