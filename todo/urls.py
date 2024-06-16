
from django.contrib import admin
from django.urls import path
# from list_taches.views import taches, ajouter_tache, update_todo, delete_todo
from list_taches.views import todos, add_todo, update_todo, delete_todo

urlpatterns = [
    # path('', taches, name='taches'),
    path('', todos, name='todos'),
    # path('ajouter_tache/', ajouter_tache, name='ajouter_tache'),
    path('add-todo/', add_todo, name='add_todo'),
    path('update/<int:pk>/', update_todo, name='update_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
    path('admin/', admin.site.urls),
]
