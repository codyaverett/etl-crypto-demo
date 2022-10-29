from django.contrib import admin
from api.models.asset import Asset
from api.models.network import Network
from api.models.trading_pair import TradingPair
from api.models.stats import Price

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("name", "symbol")
    list_filter = ("name", "symbol")
    search_fields = ("name", "symbol")    
    
@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("id", "name")
    search_fields = ("id", "name")
    list_per_page = 15

@admin.register(Price)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("pair", "time", "price")
    list_filter = ("pair", "time", "price")
    search_fields = ("pair", "time", "price")
    
@admin.register(TradingPair)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("id", "numerator", "denominator")
    list_filter = ("id", "numerator", "denominator")
    search_fields = ("id", "numerator", "denominator")
