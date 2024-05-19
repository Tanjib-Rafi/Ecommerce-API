from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AddressListCreateView, AddressDetailView

urlpatterns = [
    path('addresses/', AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
