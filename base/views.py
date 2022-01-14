from rest_framework import views, response
from .models import Alloma, Century, Madrasa
from django.http import Http404
from .serializers import CenturySerializer, MadrasaSerializer, AllomaSerializer, AllomaIDSerializer

class CenturyAPIView(views.APIView):
    def get(self, request):
        query = Century.objects.all()
        serializer = CenturySerializer(query, many=True)
        return response.Response(serializer.data)

class MadrasaAPIView(views.APIView):
    def get(self, request):
        query = Madrasa.objects.all()
        serializer = MadrasaSerializer(query, many=True)
        return response.Response(serializer.data)

class AllomaAPIView(views.APIView):
    def get(self, request):
        query = Alloma.objects.all()
        serializer = AllomaSerializer(query, many=True)
        return response.Response(serializer.data)


class AllomaIDAPIView(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_object(pk)
        serializer = AllomaIDSerializer(queryset)
        return response.Response(serializer.data)

    def get_object(self, pk):
        try:
            return Alloma.objects.get(pk=pk)
        except Alloma.DoesNotExist:
            raise Http404

