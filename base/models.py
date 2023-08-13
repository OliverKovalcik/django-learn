from django.db import models

# Create your models here.
class Article(models.Model):
    # id
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    perex = models.CharField(max_length=250)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # author
    # category
    # theme
    def __str__(self):
        return self.name

