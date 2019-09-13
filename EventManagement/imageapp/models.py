from django.db import models
from datetime import datetime

from django.db.models import Q


class ImageQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(image_name__icontains=query) |
                         Q(uploader__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class ImageManager(models.Manager):
    def get_queryset(self):
        return ImageQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Picture(models.Model):
    image_name = models.CharField(max_length=2080, default=None, blank=True, null=True)
    image_file = models.ImageField(upload_to='images/')
    uploader = models.CharField(max_length=255, default=None, blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    objects = ImageManager()

