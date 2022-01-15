from rest_framework import views, response, generics, filters
from .serializers import SubjectSerializer, Subject_InfoSerializer, Subject_Extra_InfoSerializer
from .models import Subject, Subject_Info, Subject_Extra_Info
from base.models import Alloma
from django.http import Http404


class SubjectAPIView(views.APIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    def get(self, request, pk):
        queryset = self.get_object(pk)
        query = Subject.objects.filter(menu_id=queryset.pk)
        serializer = SubjectSerializer(query, many=True)
        return response.Response(serializer.data)

    def get_object(self, pk):
        try:
            return Alloma.objects.get(pk=pk)
        except Alloma.DoesNotExist:
            raise Http404

class Subject_InfoAPIView(views.APIView):
    def get(self, request, pk):
        queryset = self.get_object(pk)
        query = Subject_Info.objects.filter(subject_id=queryset.pk)
        serializer = Subject_InfoSerializer(query, many=True)
        return response.Response(serializer.data)

    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404

class Subject_Extra_InfoAPIView(views.APIView):
    def get(self, request, pk):
        queryset = self.get_object(pk)
        query = Subject_Extra_Info.objects.filter(subject_id=queryset.pk)
        serializer = Subject_Extra_InfoSerializer(query, many=True)
        return response.Response(serializer.data)

    def get_object(self, pk):
        try:
            return Subject_Info.objects.get(pk=pk)
        except Subject_Info.DoesNotExist:
            raise Http404

