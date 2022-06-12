from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    
class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

class CheckAvailabilityList(APIView):
    def get(self, request, lat, lng):
        point = Point(lat,lng)
        service_areas = ServiceArea.objects.filter(geojson_information__contains=point)
        serializer = ServiceAreaSerializer(service_areas, many=True)
        return Response(serializer.data)
    
