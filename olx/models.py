from django.db import models


class Olx_items(models.Model):
    title = models.CharField(max_length=150)
    url = models.TextField()
    cost = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)