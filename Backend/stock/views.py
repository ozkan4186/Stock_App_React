from django.shortcuts import render
from .serializers import FirmSerializer,CategorySerializer,ProductSerializer,BrandSerializer,PurchasesSerializer,SalesSerializer
from  rest_framework.viewsets import ModelViewSet
from .models import Firm, Category, Brand, Product, Purchases, Sales




# Create your views here.

class FirmMVS(ModelViewSet):
    queryset=Firm.objects.all()
    serializer_class=FirmSerializer


class CategoryMVS(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class BrandMVS(ModelViewSet):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer


class ProductMVS(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PurchasesMVS(ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer


class SalesMVS(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
