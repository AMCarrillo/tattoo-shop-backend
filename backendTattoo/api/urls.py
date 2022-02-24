
from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_create_contact_view, name="Contact"),
]