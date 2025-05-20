from rest_framework import serializers

from mentors_and_students.serializers import MentorSerializer, StudentSerializer
from .models import Meet
from mentors_and_students.models import Mentor, Student


class MeetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    id_mentor = serializers.PrimaryKeyRelatedField(queryset=Mentor.objects.all())
    id_student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    date_create = serializers.DateField(read_only=True)
    date_meet = serializers.DateField()


    def create(self, validated_data):
        return Meet.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.id_mentor = validated_data.get('id_mentor', instance.id_mentor)
        instance.id_student = validated_data.get('id_student', instance.id_student)
        instance.date_meet = validated_data.get('date_meet', instance.date_meet)

        instance.save()
        return instance