from django.contrib import admin
from core.models.asset import Asset
from core.models.network import Network
from core.models.account import Account
from core.models.trading_pair import TradingPair


@admin.register(Account)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("address", "network", "watch", "created_at", "updated_at")
    list_filter = ("network", "watch")
    search_fields = ("id", "address")    
    list_per_page = 30


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("name", "symbol")
    list_filter = ("name", "symbol")
    search_fields = ("name", "symbol")    
    list_per_page = 30
    
    
@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("id", "name")
    search_fields = ("id", "name")
    list_per_page = 30
    
    
@admin.register(TradingPair)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("id", "numerator", "denominator")
    list_filter = ("id", "numerator", "denominator")
    search_fields = ("id", "numerator", "denominator")
    list_per_page = 30
