from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'user_name', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            user_name=validated_data['user_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
