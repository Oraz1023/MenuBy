# Create your models here.
from django.db import models
from django.urls import reverse
from mptt.models import TreeForeignKey, MPTTModel


class MenuBy(MPTTModel):
    title = models.CharField(max_length=100)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse( 'menuby', kwargs={'pk': self.pk})

    class MPTTMeta:
        order_insertion_by = ['title']
