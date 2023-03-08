from info_dealers.models import Locations
from rest_framework import viewsets, permissions
from info_dealers.api_locations.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):

    queryset = Locations.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LocationSerializer
    lookup_field = 'id'

