from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('pin/<int:pk>/', views.toggle_pin, name='toggle_pin'), 
    path('create/', views.create_note, name='create_note'),
    path('update/<int:pk>/', views.update_note, name='update_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
]
