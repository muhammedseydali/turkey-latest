
import datetime
from django.db.models import Q
from django.urls import reverse
from django.db import transaction
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from .function import generate_auto_id
from .models import Products, Category 
from .serializers import CategoryCreateSerializer, ProductSerializer,ProductRetrieveSerializer


class Category_add(ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    permission_classes = (AllowAny,)
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()

    # def get_serializer_context(self):
    #     return {
    #         'request':self.request,
    #         'user':self.request.user
    #     }
    def get_serializer_context(self):
       context = super().get_serializer_context()
       context.update({'request':self.request})
       return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        creator = request.user
        updater = creator
        category = Category.objects.create(creator=creator, updater=updater, auto_id=generate_auto_id(Category), **serializer.validated_data)
        return Response(CategoryCreateSerializer(category).data)
    

class Product_Add(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        creator = request.user
        updater = creator
        products = Products.objects.create(creator=creator, updater=updater, auto_id=generate_auto_id(Products), **serializer.validated_data)
        return Response(ProductSerializer(products).data)
    
class ListProducts(APIView):

    def get(self, request):
        """
        Return a list of all users.
        """
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request':request})
        return Response(serializer.data)

class TrendingProducts(APIView):

    def get(self, request):
        """
        Return a list of trending products.
        """
        products = Products.objects.filter(is_trending=True, is_deleted=False)
        serializer = ProductSerializer(products, many=True, context={'request':request})
        return Response(serializer.data)
    
# class Product_Add(ModelViewSet):
#     permission_classes = (AllowAny,)
#     serializer_class = ProductSerializer
#     queryset = Products.objects.all()

#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context.update({'request': self.request})
#         return context

#     def get_serializer_class(self):
#         if self.request.method in ['POST', 'PUT']:
#             return ProductSerializer
#         return ProductRetrieveSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         creator = request.user
#         updater = request.user
#         images = serializer.validated_data.pop('images', None)  # Assuming the images are uploaded as a list of files

#         with transaction.atomic():
#             print('herere')
#             product = Products.objects.create(
#                                             auto_id = generate_auto_id(Products),
#                                             creator=creator,
#                                             updater=updater,
#                                             **serializer.validated_data
#             )

#             if images:
#                 print(True)
#                 save_image(images, creator, updater, product)  # Function to save images
            
#             serialized_images_data = ProductImageSerializer(images, many=True, context={'request': request})

#             serialized_product = ProductRetrieveSerializer(product, context={'request': request})
#             response_data ={
#                 'product': serialized_product.data,
#             }
#             return Response(response_data)


