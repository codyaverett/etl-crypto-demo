from django.urls import path, include
from rest_framework import routers
from core.views import stats

router = routers.DefaultRouter()
router.register(r"price", stats.PriceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]