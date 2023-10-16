from rest_framework import serializers
from todo.models import Todo

class Todoserializer(serializers.ModelSerializer):
    class Meta:

        read_only_fields = ("created", "datecompleted")  #???????????????????????
        model = Todo
        fields =['id', 'title', 'memo', 'created', 'datecompleted', 'important']

class TodoCompleteserializer(serializers.ModelSerializer):
    class Meta:

        fields = ['id']
        model = Todo
        read_only_fields =['title', 'memo', 'created', 'datecompleted', 'important']
