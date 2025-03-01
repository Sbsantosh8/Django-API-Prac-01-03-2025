from rest_framework import serializers
from app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    print("from Product seriaizers...........")

    class Meta:
        model = Product
        fields = "__all__"
