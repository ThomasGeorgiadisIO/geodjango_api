from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('provider',views.ProviderViewSet)
router.register('service_area',views.ServiceAreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
