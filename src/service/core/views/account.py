from rest_framework import viewsets
from core.models.account import Account, AccountBalance
from core.serializers.account import AccountSerializer, AccountBalanceSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited
    """
    queryset = Account.objects.all().order_by("address")
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"
    

class AccountBalanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited
    """
    queryset = AccountBalance.objects.all().order_by("account")
    serializer_class = AccountBalanceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"