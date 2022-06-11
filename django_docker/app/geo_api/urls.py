from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from geo_api import views

urlpatterns = [
    path('providers/', views.ProviderList.as_view()),
    path('service_area', views.ServiceAreaList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)