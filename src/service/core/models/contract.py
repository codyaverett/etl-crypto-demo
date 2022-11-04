from timescale.db.models.models import TimescaleModel, TimescaleDateTimeField
from core.models.account import Account
from django.db import models


class Contract(models.Model):
    
    id = models.AutoField(primary_key=True, auto_created=True)
    address = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    functions = models.ManyToManyField('ContractFunction', blank=True)
    modifiers = models.ManyToManyField('ContractModifier', blank=True)
    nodes = models.ManyToManyField('ContractNode', blank=True)
    
    class Meta:
        db_table = 'contract'
        unique_together = ('address', 'name')

    def __str__(self):
        return f'{self.name}'
    

class ContractFunction(models.Model):
    
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'contract_function'
        unique_together = ('contract', 'name')

    def __str__(self):
        return f'{self.name}'


# class ContractModifier(ContractFunction):
    
#     class Meta:
#         db_table = 'contract_modifier'
#         unique_together = ('contract', 'name')
        
#     def __str__(self):
#         return f'{self.name}'


# class ContractStateVariables(models.Model):
    
#     id = models.AutoField(primary_key=True, auto_created=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
#     access = models.CharField(max_length=255, blank=True, null=True)
    
#     class Meta:
#         db_table = 'contract_state_variables'
#         unique_together = ('contract', 'name')

#     def __str__(self):
#         return f'{self.name}'
    

# class ContractNode(models.Model):
    
#     id = models.AutoField(primary_key=True, auto_created=True)
    
#     name = models.CharField(max_length=255, blank=True, null=True)
    
#     contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    
#     class Meta:
#         db_table = 'contract_node'
#         unique_together = ('contract', 'name')

#     def __str__(self):
#         return f'{self.name}'