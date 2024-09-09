from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'city', 'country')

    def validate(self, data):
        # Check for unique username
        if CustomUser.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError({'username': 'A user with this username already exists.'})

        # Check for unique email
        if CustomUser.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError({'email': 'A user with this email already exists.'})

        return data

    def create(self, validated_data):
        print("create method")
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
