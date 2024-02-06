from rest_framework import serializers
from .models import task

class tasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ['title', 'content']