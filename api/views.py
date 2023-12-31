from rest_framework import generics, permissions
from .serializer import Todoserializer, TodoCompleteserializer
from todo.models import Todo
from django.utils import timezone
    
class TodoCompletedList(generics.ListAPIView):
    serializer_class = Todoserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')



class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = Todoserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=True)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        

class TodoetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Todoserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
    
class TodoComplete(generics.UpdateAPIView):
    serializer_class = TodoCompleteserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
    
    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()



 


