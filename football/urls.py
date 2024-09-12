# football/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, TeamViewSet, PlayerViewSet, AreaViewSet

router = DefaultRouter()
router.register(r'matches', MatchViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'areas', AreaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
