from django.shortcuts import render
from .models import Task
from rest_framework import status
from .serializers import TaskSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



# Create your views here.
class CustomGenericAPIView(generics.GenericAPIView):
    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if response.status_code == status.HTTP_403_FORBIDDEN:
            response.data = {
                'detail': 'You do not have permisson to perform this action. Please ensure you are task owner.'
            }
        return response

class TaskAPIView(generics.ListCreateAPIView):
    queryset =  Task.objects.select_related('user')
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['due_date', 'user']
    search_fields = ['task', 'description']
    ordering_fields = ['due_date', 'task', 'date_created']
    permission_classes = [permissions.IsAuthenticated]

    # def get(self, request):
    #     tasks = Task.objects.all()
    #     serializer = TaskSerializer(tasks, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = TaskSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDetailView(CustomGenericAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    # def get_object(self, pk):
    #     try:
    #         return Task.objects.get(pk=pk)
    #     except Task.DoesNotExist:
    #         raise Http404
        
    # def get(self, request, pk):
    #     task = self.get_object(pk)
    #     serializer = TaskSerializer(task)
    #     return Response(serializer.data)
    
    # def put(self, request, pk):
    #     task = self.get_object(pk)
    #     serializer = TaskSerializer(task, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, pk):
    #     task = self.get_object(pk)
    #     serializer = TaskSerializer(task, data=request.data)
    #     task.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def handle_exception(self, exc):
    #     response = super().handle_exception(exc)
    #     if response.status_code == status.HTTP_403_FORBIDDEN:
    #         response.data = {
    #             'detail': 'You do not have permisson to perform this action. Please ensure you are task owner.'
    #         }
    #     return response