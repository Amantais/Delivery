from django.urls import path, include 
from rest_framework.routers import DefaultRouter

from .views import CateogriesList, ProductViewSet, MainCommentViewSet

router = DefaultRouter()
router.register('main-comments', MainCommentViewSet)
router.register('', ProductViewSet)


urlpatterns = [
    path('categories/', CateogriesList.as_view()),
    path('', include(router.urls)),
]