from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # Use email for authentication since it's set as the USERNAME_FIELD
    user = authenticate(request, email=email, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_logout(request):
    # Get the token from the request header
    token = request.auth

    if token:
        # Delete the token to invalidate it
        token.delete()
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Token not provided."}, status=status.HTTP_400_BAD_REQUEST)