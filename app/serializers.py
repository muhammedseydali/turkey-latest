from django.contrib.auth.models import User

from rest_framework import serializers

from . models import Category, Products
from .function import generate_auto_id
from operator import attrgetter


class CategoryCreateSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(required=False)

    class Meta:
        model=Category
        fields=['auto_id' ,'id', 'name', 'description', 'is_deleted']

class ProductSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(required=False)
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model=Products
        fields=['auto_id', 'id', 'name', 'category', 'description', 'mrp', 'image', 'is_active', 'is_deleted']
    

class ProductRetrieveSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(required=False)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ['auto_id', 'id', 'name', 'category', 'description', 'mrp', 'image', 'is_active', 'is_deleted']

    def get_image(self, instance):
        product_image = instance.productimages_set.first()  # Access the related ProductImages instance
        if product_image and product_image.image:
            request = self.context.get('request')
            image_url = product_image.image.url
            if request is not None:
                return request.build_absolute_uri(image_url)
            return image_url
        return None

