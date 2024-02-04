from django.contrib import admin
from .models import ToDoList, TodoItem

admin.site.register(ToDoList)
admin.site.register(TodoItem)

