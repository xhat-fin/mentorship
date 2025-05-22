from logging import exception
from urllib.parse import uses_params

from django.contrib.auth import user_logged_in
from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView, Response
from .models import Meet
from meetings.serializers import MeetSerializer
import requests as req
import os

# Create your views here.

class MeetAPIview(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        meet = Meet.objects.select_related('id_mentor', 'id_student')
        return Response(MeetSerializer(meet, many=True).data)


    def post(self, request):
        serializer = MeetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"meet": serializer.data})


class MeetAPIviewID(APIView):
    permission_classes = (IsAuthenticated,)

    def get_by_id(self, id):
        queryset = Meet.objects.get(id=id)
        return queryset


    def get(self, request, id):
        queryset = self.get_by_id(id)
        serializer = MeetSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({"error": "id not exists"})

        try:
            instance = Meet.objects.get(id=id)
        except:
            return Response({"error": "Object not exists"})

        serializer = MeetSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()

        return Response({"meet": serializer.data})



def auth_token():
    refresh_token = os.getenv('REFRESH')
    tokens = req.post(url='http://127.0.0.1:8000/api/token/refresh/', data={"refresh": refresh_token})
    if tokens.status_code == 200:
        access_tokens = tokens.json()
        print("получен новый токен access", access_tokens['access'])
        return tokens.json()['access']
    else:
        return {"error": tokens.json()}



#view
def get_meets(request):
    try:
        data = req.get('http://127.0.0.1:8000/meet/api/v1/meetlist/', headers={"Authorization": f"Bearer {os.getenv('access')}"})
        return render(request, "meetings/meets.html", {"data": data.json()})
    except:
        headers = {
            "Authorization": f"Bearer {auth_token()}"
        }
        data = req.get('http://127.0.0.1:8000/meet/api/v1/meetlist/', headers=headers)
        return render(request, "meetings/meets.html", {"data": data.json()})


def get_meets_by_id(request, id):
    try:
        data = req.get(f'http://127.0.0.1:8000/meet/api/v1/meetlist/{id}', headers={"Authorization": f"Bearer {os.getenv('access')}"})
        if data.status_code == 401:
            raise Exception
        data = data.json()
        return render(request, "meetings/meets_id.html", {"data":data})
    except:
        headers = {
            "Authorization": f"Bearer {auth_token()}"
        }
        data = req.get(f'http://127.0.0.1:8000/meet/api/v1/meetlist/{id}', headers=headers)
        data = data.json()
        return render(request, "meetings/meets_id.html", {"data":data})