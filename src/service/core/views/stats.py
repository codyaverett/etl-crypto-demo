from rest_framework import viewsets
# from rest_framework import permissions

from core.models.stats import Price
from core.serializers.stats import PriceSerializer

class PriceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows price to be viewed or edited
    """

    queryset = Price.objects.all().order_by("time")
    serializer_class = PriceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = "time"