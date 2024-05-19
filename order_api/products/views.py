from rest_framework import generics, permissions
from .models import Product, Category, Brand, ProductVariation, Review, Wishlist
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer, ProductVariationSerializer, ReviewSerializer, WishlistSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

class BrandListCreateView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BrandSerializer

class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BrandSerializer

class ProductVariationListCreateView(generics.ListCreateAPIView):
    queryset = ProductVariation.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductVariationSerializer

class ProductVariationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductVariation.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductVariationSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewSerializer

class WishlistListCreateView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WishlistSerializer

class WishlistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WishlistSerializer
