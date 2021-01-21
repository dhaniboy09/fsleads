from rest_framework.routers import DefaultRouter
from core.api.leads import LeadsViewSet

v1_router = DefaultRouter()
v1_router.register(r'leads', LeadsViewSet, basename='leads-api')


