from django.urls import path, include
from rest_framework import routers
from account.views.account_viewset import AccountViewSet
from account.views.account_balance_viewset import AccountBalanceViewSet


router = routers.DefaultRouter()
router.register(r"account", AccountViewSet)
router.register(r"balance", AccountBalanceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
