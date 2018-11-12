#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import render_to_response
from django.template import RequestContext
from django_filters.rest_framework import DjangoFilterBackend


from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *

#REST API
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

#filters
#from filters.mixins import *

from api.pagination import *
import json, datetime, pytz
from django.core import serializers
import requests

from api.models import Weight
#from api.serializers import BreedSerializer
from api.serializers import UserSerializer, WeightSerializer

def home(request):
   """
   Send requests to / to the ember.js clientside app
   """
   return render_to_response('ember/index.html',
               {}, RequestContext(request))

class UserCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class Events(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

class WeightDetail(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Weight.objects.get(pk=pk)
        except Weight.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        weight = self.get_object(pk)
        serializer = WeightSerializer(weight)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        weight = self.get_object(pk)
        serializer = WeightSerializer(weight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        weight = self.get_object(pk)
        weight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WeightList(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, userid, startdate, enddate, format=None):
        weights = Weight.objects.filter(userid=userid).filter(weightdate__gte=startdate).filter(weightdate__lte=enddate)
        serializer = WeightSerializer(weights, many=True)
        return Response(serializer.data)

    def post(self, request, format='json'):
        serializer = WeightSerializer(data=request.data)
        if serializer.is_valid():
            weight = serializer.save()
            if weight:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
