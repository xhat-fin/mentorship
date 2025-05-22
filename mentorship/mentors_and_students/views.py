from os import rename, access
import requests as req
from django.core.serializers import serialize
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import querystring
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from .models import Mentor, Student
from .serializers import MentorSerializer, StudentSerializer
from dotenv import load_dotenv
import os

load_dotenv()

# REST API

class MentorAPIview(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = Mentor.objects.all()

        return Response(MentorSerializer(queryset, many=True).data)


    def post(self, request):
        serializer = MentorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})


class StudentAPIview(APIView):
    permission_classes = (IsAuthenticated,)

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


    def put(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({"error": "id not exists"})

        try:
            instance = Mentor.objects.get(id=id)
        except:
            return Response({"error": "Object not exists"})

        serializer = MentorSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()

        return Response({"mentor": serializer.data})




class StudentAPIviewID(APIView):
    def get_by_id(self, id):
        queryset = Student.objects.get(id=id)
        return queryset


    def get(self, request, id):
        queryset = self.get_by_id(id)
        serializer = StudentSerializer(queryset)
        return Response(serializer.data)


    def put(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({"error": "id not exists"})

        try:
            instance = Student.objects.get(id=id)
        except:
            return Response({"error": "Object not exists"})

        serializer = StudentSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()

        return Response({"student": serializer.data})


def auth_token():
    refresh_token = os.getenv('REFRESH')
    tokens = req.post(url='http://127.0.0.1:8000/api/token/refresh/', data={"refresh": refresh_token})
    if tokens.status_code == 200:
        access_tokens = tokens.json()
        print("получен новый токен access", access_tokens['access'])
        return tokens.json()['access']
    else:
        return {"error": tokens.json()}

# view
def index(request):
    auth_token()
    return render(request, "mentors_and_students/index.html")


def get_mentors(request):
    try:
        mentors = req.get("http://127.0.0.1:8000/api/v1/mentorlist", headers={"Authorization": f"Bearer {os.getenv('access')}"})
        if mentors.status_code == 401:
            raise Exception
        data = mentors.json()
        return render(request, 'mentors_and_students/mentors.html', {"data":data})
    except:
        headers = {
            "Authorization": f"Bearer {auth_token()}"
        }
        mentors = req.get("http://127.0.0.1:8000/api/v1/mentorlist", headers=headers)
        data = mentors.json()
        return render(request, 'mentors_and_students/mentors.html', {"data": data})



def get_students(request):
    try:
        students = req.get("http://127.0.0.1:8000/api/v1/studentslist", headers={"Authorization": f"Bearer {os.getenv('access')}"})
        if students.status_code == 401:
            raise Exception
        data = students.json()
        return render(request, 'mentors_and_students/students.html', {"data": data})
    except:
        headers = {
            "Authorization": f"Bearer {auth_token()}"
        }
        students = req.get("http://127.0.0.1:8000/api/v1/studentslist", headers=headers)
        data = students.json()
        return render(request, 'mentors_and_students/students.html', {"data": data})


def get_student_by_id(request, id):
    try:
        data = req.get(f"http://127.0.0.1:8000/api/v1/student/{id}", headers={"Authorization": f"Bearer {os.getenv('access')}"})
        if data.status_code == 401:
            raise Exception
        return render(request, "mentors_and_students/view_student.html", {"data":data.json()})
    except:
        headers = {
            "Authorization": f"Bearer {auth_token()}"
        }
        data = req.get(f"http://127.0.0.1:8000/api/v1/student/{id}", headers=headers)
        return render(request, "mentors_and_students/view_student.html", {"data":data.json()})


def get_mentors_by_id(request, id):
    try:
        data = req.get(f"http://127.0.0.1:8000/api/v1/mentor/{id}", headers={"Authorization": f"Bearer {os.getenv('access')}"})
        if data.status_code == 401:
            raise Exception
        return render(request, "mentors_and_students/view_mentor.html", {"data":data.json()})
    except:
        headers = {
            "Authorization": f"Bearer {auth_token()}"
        }
        data = req.get(f"http://127.0.0.1:8000/api/v1/mentor/{id}", headers=headers)
        return render(request, "mentors_and_students/view_mentor.html", {"data":data.json()})