from rest_framework import serializers
from .models import *


class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']


class UserProfileOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']



class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['image']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%d-%m-%Y')
    user = UserProfileReviewSerializer()
    class Meta:
        model = Review
        fields = ['user', 'text', 'date']


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class ProductListSerializer(serializers.ModelSerializer):
    photos = ProductPhotoSerializer(read_only=True, many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id',  'product_name', 'category', 'photos', 'price']


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_product = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'category_product']


class ProductDetailSerializer(serializers.ModelSerializer):
    photos = ProductPhotoSerializer(read_only=True, many=True)
    category = CategorySerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    owner = UserProfileOwnerSerializer()
    product_review = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['product_name', 'category', 'product_video', 'photos',  'price', 'article', 'description',
                  'check_original', 'created_date', 'owner', 'product_review']


