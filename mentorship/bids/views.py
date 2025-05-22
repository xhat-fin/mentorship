from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from .models import Bids
from bids.serializers import BidsSerializerC, BidsSerializerU
import requests as req
from dotenv import load_dotenv
import os

# Create your views here.

class BidsAPIview(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        bids = Bids.objects.select_related('id_mentor', 'id_student')
        return Response(BidsSerializerC(bids, many=True).data)


    def post(self, request):
        serializer = BidsSerializerC(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"bids": serializer.data})


class BidsAPIviewID(APIView):
    def get_by_id(self, id):
        queryset = Bids.objects.get(id=id)
        return queryset


    def get(self, request, id):
        queryset = self.get_by_id(id)
        serializer = BidsSerializerC(queryset)
        return Response(serializer.data)


    def put(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Bids.objects.get(id=id)
        except:
            return Response({"error": "Object not exists"})

        serializer = BidsSerializerU(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"bids": serializer.data})


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
def get_bids(request):
    try:
        data = req.get('http://127.0.0.1:8000/bids/api/v1/bidslist/', headers={"Authorization": f"Bearer {os.getenv('access')}"})
        if data.status_code == 401:
            raise Exception
        data = data.json()
        return render(request, "bids/bids.html", {"data": data})
    except:
        headers = {
            "Authorization": f"Bearer {auth_token()}"
        }
        data = req.get('http://127.0.0.1:8000/bids/api/v1/bidslist/', headers=headers)
        if data.status_code == 401:
            raise Exception
        data = data.json()
        return render(request, "bids/bids.html", {"data": data})


def get_bids_by_id(request, id):
    try:
        data = req.get(f'http://127.0.0.1:8000/bids/api/v1/bidslist/{id}', headers={"Authorization": f"Bearer {os.getenv('access')}"})
        if data.status_code == 401:
            raise Exception
        data = data.json()
        return render(request, "bids/bids_id.html", {"data":data})
    except:
        headers = {
            "Authorization": f"Bearer {auth_token()}"
        }
        data = req.get(f'http://127.0.0.1:8000/bids/api/v1/bidslist/{id}', headers=headers)
        if data.status_code == 401:
            raise Exception
        data = data.json()
        return render(request, "bids/bids_id.html", {"data":data})
