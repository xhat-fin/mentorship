from os import rename

from django.http import HttpResponse
from django.shortcuts import render
from .models import Mentor, Student

# Create your views here.

def index(request):
    return render(request, "mentors_and_students/index.html")


def get_mentors(request):
    mentors = Mentor.objects.all()

    data = []
    for ment in mentors:
        data.append({
            "id": ment.id,
            "name": ment.name,
            "sphere": ment.sphere,
            "experience": ment.experience
        })

    return render(request, 'mentors_and_students/mentors.html', {"data":data})

def get_students(request):
    students = Student.objects.all()
    data = []
    for std in students:
        data.append({
            "id": std.id,
            "name": std.name,
            "description": std.descriptions
        })
    return render(request, 'mentors_and_students/students.html', {"data": data})


def get_meetings(request):
    return HttpResponse("<h1 align='center'>Встречи</h1>")


def get_bids(request):
    return HttpResponse("<h1 align='center'>Заявки</h1>")


def get_student_by_id(request, id):
    student = Student.objects.get(id=id)
    data = {"id": student.id,
            "name": student.name,
            "description": student.descriptions}
    return render(request, "mentors_and_students/view_student.html", {"data":data})

def get_mentors_by_id(request, id):
    ment = Mentor.objects.get(id=id)
    data = {"id": ment.id,
            "name": ment.name,
            "sphere": ment.sphere,
            "experience": ment.experience}
    return render(request, "mentors_and_students/view_mentor.html", {"data":data})