from django.urls import path
from .views import dongari, volun

app_name="button"
urlpatterns = [
    path('dongari', dongari, name="dongari"),
    path('volun', volun, name="volun"),
]
