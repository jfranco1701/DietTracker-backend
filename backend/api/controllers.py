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
from rest_framework import viewsets


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
from rest_framework.decorators import action
from rest_framework.authentication import *

#filters
#from filters.mixins import *

from api.pagination import *
import json, datetime, pytz
from django.core import serializers
import requests

from api.models import Weight
from api.serializers import UserSerializer, WeightSerializer, MealSerializer, FavoriteSerializer

from rest_framework import permissions

def home(request):
   """
   Send requests to / to the ember.js clientside app
   """
   return render_to_response('ember/index.html',
               {}, RequestContext(request))

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'lastName': user.last_name,
        'firstName': user.first_name,
        'dateJoined': user.date_joined
    }

class Register(APIView):
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
    permission_classes = (IsAuthenticated,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

class WeightViewSet(viewsets.ModelViewSet):
    queryset = Weight.objects.all().order_by('-weightdate')
    serializer_class = WeightSerializer
    permission_classes = (IsAuthenticated,)
    filter_fields = ('weightdate',)
    filter_backends = (DjangoFilterBackend,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset \
            .filter(userid=self.request.user.id)

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = (IsAuthenticated,)
    filter_fields = ('mealdate', 'mealtype',)
    filter_backends = (DjangoFilterBackend,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset \
            .filter(userid=self.request.user.id)

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset \
            .filter(userid=self.request.user.id)
