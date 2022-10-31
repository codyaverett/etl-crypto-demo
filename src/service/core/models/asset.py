from django.db import models
from .network import Network


class Asset(models.Model):
    id = models.AutoField(primary_key=True, 
                          auto_created=True)
    symbol = models.CharField(max_length=5, 
                              null=False)
    name = models.CharField(max_length=20, 
                            null=False)
    networks = models.ManyToManyField(Network,
                    verbose_name='supported networks')
    
    class Meta:
        db_table = 'asset'
    
    def __str__(self):
        return f'{self.name}: {self.symbol}'