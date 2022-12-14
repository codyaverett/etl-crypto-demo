from core.views.account import AccountViewSet, AccountBalanceViewSet
from django.urls import path, include
from rest_framework import routers
from core.views import stats


router = routers.DefaultRouter()
router.register(r"accounts", AccountViewSet)
router.register(r"balances", AccountBalanceViewSet)
router.register(r"prices", stats.PriceViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
