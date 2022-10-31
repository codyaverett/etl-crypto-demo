from rest_framework import serializers
from datetime import datetime

from account.models.account import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "address", "network", "watch", "updated_at", "created_at")
        lookup_field = "address"

    # Update a todoList updated_at field when it is updated
    def update(self, instance, validated_data):
        instance.updated_at = datetime.now()
        instance.save()
        return super().update(instance, validated_data)
