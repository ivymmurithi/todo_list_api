from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet, TodoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='api-auth'))
]