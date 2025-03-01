from django.urls import path
from .views import index

api_url = "http://127.0.0.1:8000/"

urlpatterns = [path("", index, name="index")]
