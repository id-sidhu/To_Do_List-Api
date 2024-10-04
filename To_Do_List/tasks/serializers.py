from rest_framework import serializers
from .models import Task
from django.utils import timezone
from datetime import date
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'task', 'description', 'date_created', 'due_date', 'user', 'is_overdue']

    def get_is_overdue(self, obj):
        if obj.due_date:
            return obj.due_date < timezone.now()
        return False
    
    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Due date connot be in past.")
        return value