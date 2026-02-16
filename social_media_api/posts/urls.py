from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router automatically creates URLs for all CRUD operations
router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
