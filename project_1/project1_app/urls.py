from django.urls import path, include
from rest_framework import routers
from .views import dataViewSet, ContactViewSet, NewsViewSet

router = routers.DefaultRouter()
router.register('data', dataViewSet)
router.register('Contact', ContactViewSet)
router.register('News', NewsViewSet)


urlpatterns = [
    path('api/', include(router.urls))
]