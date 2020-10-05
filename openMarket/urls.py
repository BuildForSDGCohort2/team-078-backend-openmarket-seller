from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.urls import router as profile_router
from store.urls import router as store_router

router = routers.DefaultRouter()
router.registry.extend(profile_router.registry)
router.registry.extend(store_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('api', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
