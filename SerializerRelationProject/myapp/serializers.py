from pyexpat import model
from rest_framework import serializers

from myapp.models import Paradigram,Language,Programmer

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Language
        fields=('id','url','name','paradiagram')

class ParadigramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Paradigram
        fields=('id','url','name')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Programmer
        fields=('id','url','name','language')