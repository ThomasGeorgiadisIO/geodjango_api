from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProviderList(APIView):
    """
    List all Providers, or create a new Provider.
    """
    def get(self, request, format=None):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceAreaList(APIView):
    """
    List all ServiceAreas, or create a new ServiceArea.
    """
    def get(self, request, format=None):
        serviceAreas = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(serviceAreas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
