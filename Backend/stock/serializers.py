from rest_framework import serializers
from .models import Firm, Category, Brand, Product, Purchases, Sales



class FirmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Firm
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()  # read_only

    class Meta:
        model = Category
        fields = ("id", "name", "product_count")
        
    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count()




class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ("name", "id")


class ProductSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    brand=serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ("name", "id", "category", "category_id", "brand", "brand_id", "stock",)


class PurchasesSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    firm=serializers.StringRelatedField(read_only=True)
    firm_id=serializers.IntegerField()
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()
    product = serializers.StringRelatedField(read_only=True)
    product_id = serializers.IntegerField()

    class Meta:
        model = Purchases
        fields = ("id", "user", "category", "firm", "firm_id", "brand",
                  "brand_id", "product", "product_id" ,"quantity", "price", "total_price")

    def get_category(self, obj):
        return obj.product.category.name

    def get_total_price(self, obj):
        return obj.quantity*obj.price


class SalesSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()


    category = serializers.SerializerMethodField()
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()
    product = serializers.StringRelatedField(read_only=True)
    product_id = serializers.IntegerField()
    
     

    class Meta:
        model = Sales
        fields = ("id", "user", "category",  "brand",
                  "brand_id", "product", "product_id", "quantity", "price", "total_price")

    def get_category(self, obj):
        return obj.product.category.name


    def get_total_price(self, obj):
        return obj.quantity*obj.price
