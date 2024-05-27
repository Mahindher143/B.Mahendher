from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import *
from .models import *


#CRUD oparations......
class List(generics.ListAPIView):
    queryset = Day_Store.objects.all()
    serializer_class = Day_StoreSerializer

class Detail(generics.RetrieveUpdateAPIView):
    queryset = Day_Store.objects.all()
    serializer_class = Day_StoreSerializer

class Create(generics.CreateAPIView):
    queryset = Day_Store.objects.all()
    serializer_class = Day_StoreSerializer

class Delete(generics.DestroyAPIView):
    queryset = Day_Store.objects.all()
    serializer_class = Day_StoreSerializer

