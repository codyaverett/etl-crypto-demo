# Generated by Django 4.1.2 on 2022-10-31 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_network_asset_networks'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='asset',
            table='asset',
        ),
        migrations.AlterModelTable(
            name='network',
            table='network',
        ),
        migrations.AlterModelTable(
            name='price',
            table='asset_price',
        ),
        migrations.AlterModelTable(
            name='tradingpair',
            table='asset_tradingpair',
        ),
    ]
