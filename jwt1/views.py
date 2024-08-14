from django.shortcuts import render
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from models import *
from .serializers import *
from rest_framework.views import APIView

# Create your views here
class BankViewset(APIView):
 permission_classes = [IsAdminUser]