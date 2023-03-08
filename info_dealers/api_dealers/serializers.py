from rest_framework import serializers
from info_dealers.models import Dealer


class DealerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dealer
    fields = '__all__'
    read_only_fields = ('id',)

