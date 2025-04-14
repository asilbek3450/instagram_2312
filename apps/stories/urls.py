from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoryViewSet, StoryLikeViewSet, StoryViewViewSet

router = DefaultRouter()
router.register(r'stories', StoryViewSet)
router.register(r'story-likes', StoryLikeViewSet)
router.register(r'story-views', StoryViewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
