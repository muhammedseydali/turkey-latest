from django.urls import path, include

from rest_framework import routers

from . import views
from .views import Category_add, Product_Add, ListProducts, TrendingProducts

router = routers.SimpleRouter()
router.register(r'category', Category_add)
router.register(r'product', Product_Add)

app_name = "app"


urlpatterns = [
    path('', include(router.urls)),
    path('products', views.ListProducts.as_view()),
    path('trending-products', views.TrendingProducts.as_view())
]
