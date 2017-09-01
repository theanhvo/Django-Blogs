from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __str__(self):
        return self.title
