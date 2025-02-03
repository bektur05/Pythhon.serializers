from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'rating', RatingViewSet, basename='rating')
router.register(r'review', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListAPIViewSet.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('category/', CategoryListAPIView.as_view(), name='category_list '),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
]