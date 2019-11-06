from django.shortcuts import render
from rest_framework import generics,filters,viewsets
from search.models import Electric
from search.serializers import ElectricSerializer

class ElectricAPIView(viewsets.ModelViewSet):
    #filter_backends=(filters.SearchFilter,)
    queryset=Electric.objects.all()
    serialzer_class=ElectricSerializer
 