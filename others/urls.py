from django.urls import path
from .views import photo, profile, visit

app_name="others"
urlpatterns = [
    path('profile', profile, name="profile"),
    path('photo', photo, name="photo"),
    path('visit', visit, name="visit"),
]
