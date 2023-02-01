from django.urls import  path,include
from rest_framework.routers import DefaultRouter
from .views import FirmMVS,ProductMVS,BrandMVS,CategoryMVS,PurchasesMVS,SalesMVS

router = DefaultRouter()
router.register("firms",FirmMVS)
router.register("categories",CategoryMVS)
router.register("brands",BrandMVS)
router.register("products",ProductMVS)
router.register("purchases",PurchasesMVS)
router.register("sales",SalesMVS)

urlpatterns = [
    path("stock/",include(router.urls))
]
