from django.urls import path
from .views import optimize_route, map_view

urlpatterns = [
    path('', map_view),
    path('api/optimize/', optimize_route),
]