# from django.test import TestCase
# from django.urls import reverse
# from django.db.models import Q
# from rest_framework.test import APIClient, APIRequestFactory
# from rest_framework import status
# from geo_api.models import Provider, ServiceArea
# from .serializers import ProviderSerializer, ServiceAreaSerializer, AvailabilitySerializer

# class TestProviderViewSet(TestCase):

#     def setUp(self):
#         self.client = APIClient()
#         provider = Provider.objects.create(
#             name="Thomas Georgiadis",
#             email="tom@example.com",
#             phone_number="595003939",
#             language="greek",
#             currency="eur"
#         )
#         service_area = ServiceArea.objects.create(
#             provider=provider.id,
#             name="area_1",
#             price=100,
#             geojson_information={
#                 type: "Polygon", coordinates: [[[0, 0], [3, 6], [6, 1], [0, 0]], [[2, 2], [3, 3], [4, 2], [2, 2]]]
#             }
#         )

#     def test_provider_list(self):
#         result = self.client.get(reverse('provider'))
#         providers = Provider.objects.all()
#         serializer = ProviderSerializer(providers, many=True)
#         self.assertEqual(result.status_code, status.HTTP_200_OK)
#         self.assertEqual(result.data, serializer.data)