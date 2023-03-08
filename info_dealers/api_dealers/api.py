from info_dealers.models import Dealer
from rest_framework import viewsets, permissions
from info_dealers.api_dealers.serializers import DealerSerializer


class DealerViewSet(viewsets.ModelViewSet):

    queryset = Dealer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DealerSerializer
    lookup_field = 'id'
