from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = 'username', 'reference_id'

    def validate(self, data):
        username = data.get('username', None)
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({ "success": False, "message": "user already exist" })
        
        return super().validate(data)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)