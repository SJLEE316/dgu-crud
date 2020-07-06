from django.urls import path
from .views import address, design, phone

app_name="home"
urlpatterns = [
    path('address', address, name="address"),
    path('design', design, name="design"),
    path('phone', phone, name="phone"),
]
