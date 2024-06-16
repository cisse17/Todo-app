from django.db import models

class ListeTaches(models.Model):
    titre = models.CharField(max_length=255)
    est_fait =models.BooleanField(default=False)

# class Todo(models.Model):
#     title = models.CharField(max_length=255)
#     is_done =models.BooleanField(default=False)
