from rest_framework import serializers
from .models import Task
from users.models import CustomUser

class TaskSerializer(serializers.ModelSerializer):
    assignee = serializers.EmailField()

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'deadline', 'assignee', 'created_by']

    def create(self, validated_data):
        email = validated_data.pop('assignee')
        assignee = CustomUser.objects.get(email=email)
        task = Task.objects.create(assignee=assignee, **validated_data)
        return task
