from django.shortcuts import render
from .serializers import FirmSerializer,CategorySerializer,ProductSerializer,BrandSerializer,PurchasesSerializer,SalesSerializer
from  rest_framework.viewsets import ModelViewSet
from .models import Firm, Category, Brand, Product, Purchases, Sales
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser




# Create your views here.

class FirmMVS(ModelViewSet):
    queryset=Firm.objects.all()
    serializer_class=FirmSerializer
    permission_classes = [IsAdminUser]


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        prd_id=serializer.validated_data["product_id"]
       
        stock=Product.objects.filter(id=prd_id)[0].stock

        if stock<serializer.validated_data["quantity"]:
            data={
                "message":f"we did nt have enough stock only {stock} left    "
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
