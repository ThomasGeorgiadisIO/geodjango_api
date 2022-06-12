from rest_framework import serializers
from .models import ServiceArea, Provider


class ServiceAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceArea
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = "__all__"


class AvailabilitySerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source='provider.name')

    class Meta:
        model = ServiceArea
        fields = (
            'name',
            'price',
            'provider_name',
        )
