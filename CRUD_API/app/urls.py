from django.urls import include, path
from app.views import ProductAPIView

urlpatterns = [path("products/", ProductAPIView.as_view(), name="product-list")]
