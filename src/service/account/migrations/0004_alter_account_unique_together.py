# Generated by Django 4.1.2 on 2022-10-31 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_network_asset_networks'),
        ('account', '0003_alter_account_address'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('address', 'network')},
        ),
    ]
