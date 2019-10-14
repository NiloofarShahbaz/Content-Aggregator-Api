from django.db import models
from django.conf import settings


class Site(models.Model):
    name = models.CharField(max_length=150, unique=True)
    url = models.URLField()
    icon = models.ImageField()
    users = models.ManyToManyField(to=settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Link(models.Model):
    title = models.TextField()
    url = models.URLField()
    site = models.ForeignKey(to=Site, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.site) + self.title
