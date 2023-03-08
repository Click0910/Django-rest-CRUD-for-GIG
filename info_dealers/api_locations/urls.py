from rest_framework import routers
from info_dealers.api_locations.api import LocationViewSet

router = routers.DefaultRouter()

router.register('api/location', LocationViewSet, 'location')
router.register('api/location/<int:id>', LocationViewSet, 'location by id')

urlpatterns = router.urls

