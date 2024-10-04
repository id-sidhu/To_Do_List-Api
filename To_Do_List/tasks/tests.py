from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class TaskTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            'task': 'Test Task',
            'description': 'It is test going on',
            'user': self.user.id
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().task, 'Test Task')

    def test_get_tasks(self):
        Task.objects.create(task = 'Test Task',
            description = 'It is test going on',
            user = self.user)
        
        url = reverse('task-list')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)