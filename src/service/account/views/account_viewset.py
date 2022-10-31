from rest_framework import viewsets
from account.models.account import Account
from account.serializers.account_serializer import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited
    """

    queryset = Account.objects.all().order_by("address")
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"
    