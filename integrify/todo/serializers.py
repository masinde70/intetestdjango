from rest_framework import serializers
from .models import* 

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = (
            "id",
            "title",
            "description",
        )