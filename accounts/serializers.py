from rest_framework import serializers
from models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone', 'city', 'state', 'address']