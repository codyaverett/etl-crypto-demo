from tabnanny import verbose
from django.db import models
from account.models.account import Account
from timescale.db.models.models import TimescaleModel, TimescaleDateTimeField

class AccountBalance(TimescaleModel):
    id = models.AutoField(primary_key=True, auto_created=True)
    
    amount = models.DecimalField(max_digits=50, decimal_places=20)
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    time = TimescaleDateTimeField(interval="5 minute")
    
    class Meta:
        db_table = 'account_balance'
        order_with_respect_to = 'account'
    
    def __str__(self):
        return f'{self.account}: {self.amount}'
    