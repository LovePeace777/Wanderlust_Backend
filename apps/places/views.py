from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import Placesserializers
from .models import Places
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class PlacesList(generics.ListAPIView):
    queryset = Places.objects.order_by('-created_at').all()
    serializer_class = Placesserializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'description']
