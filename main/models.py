from django.db import models

# Create your models here.

class UrlDb(models.Model):
    url = models.URLField(blank=False)
    short_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)