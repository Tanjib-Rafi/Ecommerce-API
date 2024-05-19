from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PaymentListCreateView, PaymentDetailView

urlpatterns = [
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
