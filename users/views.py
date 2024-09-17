from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow anyone to access this endpoint
def create_user(request):
    # print("hello")
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_greeting(request):
    print(request.user)
    try:
        request.user.is_superuser
    except Exception as E:
        print(str(E))
        print("user is not superuser")
    return Response({"message": "Hello, authenticated user!"}, status=status.HTTP_200_OK)
