from rest_framework import serializers
from datetime import datetime

from core.models.account import Account, AccountBalance


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("__all__")
        lookup_field = "address"

    # Update a todoList updated_at field when it is updated
    def update(self, instance, validated_data):
        instance.updated_at = datetime.now()
        instance.save()
        return super().update(instance, validated_data)


class AccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBalance
        fields = ("__all__")
        lookup_field = "pk"
