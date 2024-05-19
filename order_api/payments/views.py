from rest_framework import generics, permissions
from .models import Payment
from .serializers import PaymentSerializer

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer
