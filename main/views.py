from django.shortcuts import render
from . import models
from .serializer import TeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class TeacherList(APIView):
    def get(self, request):
        teachers = models.Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
