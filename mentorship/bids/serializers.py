from rest_framework import serializers
from rest_framework.response import Response

from .models import Bids
from mentors_and_students.models import Mentor, Student


class BidsSerializerC(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    id_mentor = serializers.PrimaryKeyRelatedField(queryset=Mentor.objects.all())
    id_student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    date_create = serializers.DateField(read_only=True)
    status_completed = serializers.BooleanField(read_only=True)


    def create(self, validated_data):
        return Bids.objects.create(**validated_data)



class BidsSerializerU(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    id_mentor = serializers.PrimaryKeyRelatedField(queryset=Mentor.objects.all())
    id_student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    date_create = serializers.DateField(read_only=True)
    status_completed = serializers.BooleanField()


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.id_mentor = validated_data.get('id_mentor', instance.id_mentor)
        instance.id_student = validated_data.get('id_student', instance.id_student)
        instance.status_completed = validated_data.get('status_completed', instance.status_completed)
        instance.save()

        return instance