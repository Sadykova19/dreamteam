from rest_framework import serializers
from .models import *


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'title', 'description', 'created_at', 'completed', 'updated_at', 'owner',)