from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from myapp.models import Language,Programmer,Paradigram
from myapp.serializers import ParadigramSerializer,ProgrammerSerializer,LanguageSerializer
#from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

# Create your views here.
'''
class LanguageListNCreate(ListCreateAPIView):
    queryset=Language.objects.all()
    serializer_class=LanguageSerializer

class LanguageRetriveNUpdateNDelete(RetrieveUpdateDestroyAPIView):
    queryset=Language.objects.all()
    serializer_class=LanguageSerializer

class ProgrammerListNCreate(ListCreateAPIView):
    queryset=Programmer.objects.all()
    serializer_class=ProgrammerSerializer

class ProgrammerRetriveNUpdateNDelete(RetrieveUpdateDestroyAPIView):
    queryset=Programmer.objects.all()
    serializer_class=ProgrammerSerializer

class ParadigramListNCreate(ListCreateAPIView):
    queryset=Paradigram.objects.all()
    serializer_class=ParadigramSerializer

class ParadigramRetriveNUpdateNDelete(RetrieveUpdateDestroyAPIView):
    queryset=Paradigram.objects.all()
    serializer_class=ParadigramSerializer
'''
class LanguageView(viewsets.ModelViewSet):
    queryset=Language.objects.all()
    serializer_class=LanguageSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset=Programmer.objects.all()
    serializer_class=ProgrammerSerializer    

class ParadigramView(viewsets.ModelViewSet):
    queryset=Paradigram.objects.all()
    serializer_class=ParadigramSerializer    