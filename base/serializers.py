from rest_framework import serializers
from .models import Century, Madrasa, Alloma


class CenturySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    century = serializers.CharField(max_length=100, read_only=True)
    sum_madrasa = serializers.CharField(max_length=100, read_only=True)

class MadrasaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    relevant_century = serializers.CharField(read_only=True)

class AllomaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)
    madrasa_alloma = serializers.CharField(read_only=True)

class AllomaIDSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    birth_year = serializers.CharField(read_only=True)
    birth_area = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)
    madrasa_alloma = serializers.CharField(read_only=True)
    about = serializers.CharField(read_only=True)
    allomamenu = serializers.PrimaryKeyRelatedField(many=True, allow_empty=False, read_only=True)

