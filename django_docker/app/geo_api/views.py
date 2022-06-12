from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer, AvailabilitySerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('__all__')
    search_fields = (
        "currency",
        "email",
        "language",
        "name",
        "phone_number",
    )

    @method_decorator(cache_page(60 * 60 * 1))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('__all__')
    search_fields = ("name",)

    @method_decorator(cache_page(60 * 60 * 1))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CheckAvailabilityList(APIView):

    @method_decorator(cache_page(60 * 60 * 1))
    def get(self, request, lat, lng):
        point = Point(lat, lng)
        service_areas = ServiceArea.objects.filter(geojson_information__contains=point)
        serializer = AvailabilitySerializer(service_areas, many=True)
        return Response(serializer.data)
