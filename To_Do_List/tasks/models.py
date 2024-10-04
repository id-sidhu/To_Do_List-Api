from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxLengthValidator
import uuid

# Create your models here.
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task=models.CharField(max_length=128, db_index=True)
    description=models.TextField(blank=True, null=True, validators=[MaxLengthValidator(500)])
    date_created=models.DateTimeField(auto_now=True)
    due_date=models.DateTimeField(blank=True, null=True) 
    user=models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)


    STATUS_CHOICES = [
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

    def __str__(self):
        return self.task
    
    class Meta:
        ordering = ['due_date']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

        constraints = [
            models.UniqueConstraint(fields=['user', 'task'], name='unique_task_per_user')
        ]
    
    def is_overdue(self):
        if self.due_date and self.due_date < timezone.now():
            return True
        return False