from rest_framework import serializers
from .models import myProjects

class myProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = myProjects
        fields = ["name", "url", "description", "inDev", "image"]