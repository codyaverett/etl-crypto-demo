from django.urls import path, include
from rest_framework import routers
from account.views.accountViewSet import AccountViewSet

router = routers.DefaultRouter()
router.register(r"account", AccountViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
