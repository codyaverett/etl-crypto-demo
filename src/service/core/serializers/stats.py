from rest_framework import serializers
from core.models.stats import Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            "id",
            "pair",
            "time",
            "price",
        )
        lookup_field = "time"
