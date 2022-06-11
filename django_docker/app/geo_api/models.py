import uuid
from django.db import models
from django.contrib.gis.db import models as gis_models

class Provider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    phone_number = models.CharField(max_length=15)
    language = models.CharField(max_length=15)
    currency = models.CharField(max_length=2)

class ServiceArea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provider = models.ForeignKey(to=Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    geojson_information = gis_models.PolygonField()
