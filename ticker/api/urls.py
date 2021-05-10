from django.urls import path, include
from rest_framework import routers
from .views import TickerViewSet, HistoryViewSet

router = routers.DefaultRouter()
router.register('ticker', TickerViewSet)
router.register('history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
