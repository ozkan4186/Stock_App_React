from django.shortcuts import render
from .serializers import FirmSerializer
from  rest_framework.viewsets import ModelViewSet
from .models import Firm, Category, Brand, Product, Purchases, Sales




# Create your views here.

class FirmMVS(ModelViewSet):
    queryset=Firm.objects.all()
    serializer_class=FirmSerializer
