from django.urls import path
from .views import photo, profile, visit

urlpatterns = [
    path('profile', profile),
    path('photo', photo),
    path('visit', visit),
]
