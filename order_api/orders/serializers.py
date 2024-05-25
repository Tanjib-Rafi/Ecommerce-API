from rest_framework import serializers
from django.utils import timezone
from .models import Order, OrderItem, Cart, CartItem, Coupon
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'variation', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'billing_address', 'shipping_address', 'tracking_number', 'payment_gateway_transaction_id', 'status', 'order_total', 'items', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['order_total'] = sum(item.price * item.quantity for item in instance.items.all())
        return representation

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'variation', 'quantity', 'price']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'cart_items', 'created_at', 'updated_at']

    def validate(self, attrs):
        items = self.initial_data.get('cart_items', [])
        if not items:
            raise serializers.ValidationError("Cart is empty")

        product_ids = [item.get('product') for item in items]
        if len(product_ids) != len(set(product_ids)):
            raise serializers.ValidationError("Cart contains duplicate items")

        for item in items:
            product_id = item.get('product')
            quantity = item.get('quantity')
            if not Product.objects.filter(id=product_id).exists():
                raise serializers.ValidationError(f"Product with id {product_id} does not exist")
            product = Product.objects.get(id=product_id)
            if product.stock < quantity:
                raise serializers.ValidationError(f"Not enough stock available for {product.name}")

        return attrs


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'discount_percentage', 'expiry_date']

    def validate_expiry_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Coupon has expired")
        return value

    def validate(self, attrs):
        code = attrs.get('code')
        if code:
            try:
                coupon = Coupon.objects.get(code=code)
                if coupon.expiry_date < timezone.now().date():
                    raise serializers.ValidationError("Coupon has expired")
            except Coupon.DoesNotExist:
                raise serializers.ValidationError("Invalid coupon code")
        return attrs
