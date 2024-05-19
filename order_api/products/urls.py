from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductListCreateView, ProductDetailView, CategoryListCreateView, CategoryDetailView, BrandListCreateView, BrandDetailView, ProductVariationListCreateView, ProductVariationDetailView, ReviewListCreateView, ReviewDetailView, WishlistListCreateView, WishlistDetailView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('brands/', BrandListCreateView.as_view(), name='brand-list-create'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('variations/', ProductVariationListCreateView.as_view(), name='variation-list-create'),
    path('variations/<int:pk>/', ProductVariationDetailView.as_view(), name='variation-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('wishlists/', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('wishlists/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
