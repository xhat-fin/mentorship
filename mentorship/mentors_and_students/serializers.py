from rest_framework import serializers
from .models import Mentor, Student



class MentorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    sphere = serializers.CharField()
    experience = serializers.CharField()

    def create(self, validated_data):
        return Mentor.objects.create(**validated_data)



class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    descriptions = serializers.CharField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
