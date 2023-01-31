from django.urls import  path,include
from rest_framework.routers import DefaultRouter
from .views import FirmMVS

router = DefaultRouter()
router.register("firms",FirmMVS)

urlpatterns = [
    path("",include(router.urls))
]
