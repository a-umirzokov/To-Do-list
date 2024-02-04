from django.urls import path
from todo_app import views as v

urlpatterns = [
    path('', v.TodoListView.as_view(), name='home'),
    path('list/<int:list_id>', v.ItemListView.as_view(), name='list'),
    path('list/add/', v.ListCreateView.as_view(), name='list-add'),
    path('list/<int:list_id>/delete/', v.ListDeleteView.as_view(), name='list-delete'),
    path('list/<int:list_id>/item/add/', v.ItemCreateView.as_view(), name='item-add'),
    path('list/<int:list_id>/item/<int:pk>/', v.ItemUpdateView.as_view(), name='item-update'),
    path('list/<int:list_id>/item/<int:pk>/delete/', v.ItemDeleteView.as_view(), name='item-delete'),
]