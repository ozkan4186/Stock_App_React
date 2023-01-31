from rest_framework import serializers
from .models import Firm,Category,Brand,Product,Purchases,Sales


class FirmSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Firm
        fields="__all__"


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields=("name","id")


class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Brand
        fields=("name","id")


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields=("name","id")