from django.urls import path, include
from accounts import urls as accounts_urls
from rest_framework import routers
from estates.viewssets import EstateViewSet
from accounts.viewssets import UserViewSet
from common.views import MediaViewSet

router = routers.DefaultRouter()
router.register('api/estates', EstateViewSet, basename="estate")
router.register('api/users', UserViewSet, basename='users')
router.register('api/media', MediaViewSet, basename='media')

urlpatterns = router.urls

urlpatterns += [
    path('api/', include(accounts_urls)),
]
