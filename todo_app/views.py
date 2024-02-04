from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
)
from .models import TodoItem, ToDoList
from django.urls import reverse, reverse_lazy


class TodoListView(ListView):
    model = ToDoList
    template_name = "todo_app/home.html"

class ItemListView(ListView):
    model = TodoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list_id=self.kwargs['list_id'])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs['list_id'])
        return context

class ListCreateView(CreateView):
    model = ToDoList
    fields = ['title']

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Add a new list"
        return context

class ItemCreateView(CreateView):
    model = TodoItem
    fields = [
        'todo_list',
        'title',
        'description',
        'due_date',
    ]

    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        initial_data['todo_list'] = todo_list
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list.id])

class ListDeleteView(DeleteView):
    model = ToDoList
    success_url = reverse_lazy('home')
class ItemUpdateView(UpdateView):
    model = TodoItem
    fields = [
        'todo_list',
        'title',
        'description',
        'due_date',
    ]

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list.id])

class ItemDeleteView(DeleteView):
    model = TodoItem

    def get_success_url(self):
        return reverse('list', args=[self.kwargs['list_id']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context
