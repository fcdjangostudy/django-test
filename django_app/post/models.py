from django.conf import settings
from django.db import models


class Post(models.Model):
    author = settings.AUTH_USER_MODEL
    photo = models.ImageField(
        upload_to='post',
        blank=True,
        null=True,
    )
    comment = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
