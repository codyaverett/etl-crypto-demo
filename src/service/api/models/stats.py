from django.db import models
from timescale.db.models.models import TimescaleModel, TimescaleDateTimeField

from .trading_pair import TradingPair

class Price(TimescaleModel):
    id = models.AutoField(primary_key=True)
    pair = models.ForeignKey(TradingPair, 
                on_delete=models.CASCADE, 
                null=False)
    time = TimescaleDateTimeField(interval="1 minute")
    price = models.DecimalField(max_digits=50, decimal_places=20)

    def __str__(self):
        return f'{self.pair}: {self.price}'