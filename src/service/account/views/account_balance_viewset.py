from rest_framework import viewsets
from account.models.account_balance import AccountBalance
from account.serializers.account_balance_serializer import AccountBalanceSerializer

class AccountBalanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited
    """

    queryset = AccountBalance.objects.all().order_by("account")
    serializer_class = AccountBalanceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"
    