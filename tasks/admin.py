from django.contrib import admin
from .models import Task


# Create a ModelAdmin class to customize how the model is displayed in the admin interface
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'deadline', 'assignee', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'assignee')
    search_fields = ('title', 'description', 'assignee__username', 'assignee__email')

# Register the Task model with the TaskAdmin class
admin.site.register(Task, TaskAdmin)
