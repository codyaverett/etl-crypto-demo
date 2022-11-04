from timescale.db.models.models import TimescaleModel, TimescaleDateTimeField
from core.models.network import Network
from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    
    address = models.CharField(db_index=True, 
                               max_length=42,
                               null=False)
    
    network = models.ForeignKey(Network,
                                on_delete=models.CASCADE)
    
    watch = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    
    class Meta:
        db_table = 'account'
        unique_together = ('address', 'network')

    def __str__(self):
        return f'{self.address}'
    

class AccountBalance(TimescaleModel):
    id = models.AutoField(primary_key=True, auto_created=True)
    
    amount = models.DecimalField(max_digits=50, decimal_places=20)
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    time = TimescaleDateTimeField(interval="5 minute")
    
    class Meta:
        db_table = 'account_balance'
    
    def __str__(self):
        return f'{self.account}: {self.amount}'