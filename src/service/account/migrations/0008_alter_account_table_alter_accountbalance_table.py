# Generated by Django 4.1.2 on 2022-10-31 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_rename_balance_accountbalance'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='account',
            table='accounts',
        ),
        migrations.AlterModelTable(
            name='accountbalance',
            table='account_balances',
        ),
    ]
