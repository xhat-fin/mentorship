from rest_framework import serializers
from .models import Mentor, Student



class MentorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    sphere = serializers.CharField()
    experience = serializers.CharField()

    def create(self, validated_data):
        return Mentor.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sphere = validated_data.get('sphere', instance.sphere)
        instance.experience = validated_data.get('experience', instance.experience)

        instance.save()
        return instance




class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    descriptions = serializers.CharField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.descriptions = validated_data.get('descriptions', instance.descriptions)

        instance.save()
        return instance