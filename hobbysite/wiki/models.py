from django.db import models
from django.urls import reverse

# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length = 255)
    category = models.ForeignKey(ArticleCategory, on_delete = models.SET_NULL, null = True, related_name = "articles")
    entry = models.TextField(null = True, blank = True)
    created_on = models.DateTimeField(null = False, auto_now_add = True)
    updated_on = models.DateTimeField(null = True, auto_now = True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('wiki:article', args = [self.pk])
    
    class Meta:
        ordering = ["-updated_on"]


