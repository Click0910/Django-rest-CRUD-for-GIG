from rest_framework import serializers
from info_dealers.models import Locations


class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Locations
    fields = '__all__'
    read_only_fields = ('id',)
