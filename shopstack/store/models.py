from django.db import models

from user.models import User


class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    owner = models.OneToOneField(User)

    def __unicode__(self):
        return self.name
