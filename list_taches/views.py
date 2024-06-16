from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import ListeTaches
# from .models import Todo

# def taches(request):
#     taches = ListeTaches.objects.all()
#     return render(request, 'list_taches/taches.html', {'taches': taches})

def todos(request):
    # taches = ListeTaches.objects.all()
    todos = ListeTaches.objects.all()
    return render(request, 'list_taches/taches.html', {'todos': todos})



@require_http_methods(['POST'])
# def ajouter_tache(request):
def add_todo(request):
    todo = None
    titre = request.POST.get('title', '')
    if titre:
        # todo = ListeTaches.objects.create(titre=titre)
        todo = ListeTaches.objects.create(titre=titre)
    return render(request, 'list_taches/partials/tache.html', { 'todo': todo})


@require_http_methods(['PUT'])
def update_todo(request, pk):
    # todo = ListeTaches.objects.get(pk=pk)
    todo = ListeTaches.objects.get(pk=pk)
    todo.est_fait = True
    todo.save()
    return render(request, 'list_taches/partials/tache.html', { 'todo': todo})

@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    # todo = ListeTaches.objects.get(pk=pk)
    todo = ListeTaches.objects.get(pk=pk)
    todo.delete()

    return HttpResponse()

#pip install psycopg2 gunicorn django-heroku dj_database_url 