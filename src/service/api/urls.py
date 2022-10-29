from django.urls import path, include
from rest_framework import routers
from api.views import stats

router = routers.DefaultRouter()
router.register(r"price", stats.PriceViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
