from os import rename
import requests as req
from django.core.serializers import serialize
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import querystring
from rest_framework.views import APIView, Response

from .models import Mentor, Student
from rest_framework import generics
from .serializers import MentorSerializer, StudentSerializer


# REST API

class MentorAPIview(APIView):
    def get(self, request):
        queryset = Mentor.objects.all()

        return Response(MentorSerializer(queryset, many=True).data)


    def post(self, request):
        serializer = MentorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})


class StudentAPIview(APIView):
    def get(self, request):
        queryset = Student.objects.all()

        return Response(StudentSerializer(queryset, many=True).data)


    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})


class MentorAPIviewID(APIView):
    def get_by_id(self, id):
        queryset = Mentor.objects.get(id=id)
        return queryset


    def get(self, request, id):
        queryset = self.get_by_id(id)
        serializer = MentorSerializer(queryset)
        return Response(serializer.data)



class StudentAPIviewID(APIView):
    def get_by_id(self, id):
        queryset = Student.objects.get(id=id)
        return queryset


    def get(self, request, id):
        queryset = self.get_by_id(id)
        serializer = StudentSerializer(queryset)
        return Response(serializer.data)




# view
def index(request):
    return render(request, "mentors_and_students/index.html")


def get_mentors(request):
    mentors = req.get("http://127.0.0.1:8000/api/v1/mentorlist")
    data = mentors.json()
    return render(request, 'mentors_and_students/mentors.html', {"data":data})


def get_students(request):
    students = req.get("http://127.0.0.1:8000/api/v1/studentslist")
    data = students.json()
    return render(request, 'mentors_and_students/students.html', {"data": data})


def get_student_by_id(request, id):
    data = req.get(f"http://127.0.0.1:8000/api/v1/student/{id}")
    return render(request, "mentors_and_students/view_student.html", {"data":data.json()})


def get_mentors_by_id(request, id):
    data = req.get(f"http://127.0.0.1:8000/api/v1/mentor/{id}")
    return render(request, "mentors_and_students/view_mentor.html", {"data":data.json()})


def get_bids(request):
    return HttpResponse("<h1 align='center'>Заявки</h1>")
