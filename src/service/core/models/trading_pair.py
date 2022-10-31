from django.db import models
from .asset import Asset


class TradingPair(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    numerator = models.ForeignKey(Asset,
                    related_name='numerator',
                    on_delete=models.CASCADE, 
                    null=False)
    denominator = models.ForeignKey(Asset,
                    related_name='denominator',
                    on_delete=models.CASCADE, 
                    null=False)
    
        
    class Meta:
        db_table = 'asset_tradingpair'
    
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'