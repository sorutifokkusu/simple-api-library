from django.urls import path,include
from rest_framework import routers
from .views import BookViewSet,CategoryViewSet,SearchViewSet

router = routers.DefaultRouter()

router.register(r'books', BookViewSet,basename="books")
router.register(r'categories',CategoryViewSet,basename="categories")
router.register(r'search',SearchViewSet,basename="search")

urlpatterns = [
    path('',include(router.urls))
]