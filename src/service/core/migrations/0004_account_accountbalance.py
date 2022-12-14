# Generated by Django 4.1.2 on 2022-11-04 01:42

from django.db import migrations, models
import django.db.models.deletion
import timescale.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_asset_table_alter_network_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('address', models.CharField(db_index=True, max_length=42)),
                ('watch', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.network')),
            ],
            options={
                'db_table': 'account',
                'unique_together': {('address', 'network')},
            },
        ),
        migrations.CreateModel(
            name='AccountBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=20, max_digits=50)),
                ('time', timescale.db.models.fields.TimescaleDateTimeField(interval='5 minute')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account')),
            ],
            options={
                'db_table': 'account_balance',
            },
        ),
    ]
