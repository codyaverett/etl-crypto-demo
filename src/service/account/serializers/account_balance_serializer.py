from rest_framework import serializers
from datetime import datetime

from account.models.account_balance import AccountBalance


class AccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBalance
        fields = ("id", "account", "amount", "time")
        lookup_field = "pk"
