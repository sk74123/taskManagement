from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    print(request.user)
    user = request.user  # Get the logged-in user
    data = request.data.copy()
    data['created_by'] = user.id  # Set the created_by field to the logged-in user

    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)