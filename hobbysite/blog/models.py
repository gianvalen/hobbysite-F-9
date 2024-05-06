from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Article Categories"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    header_image = models.ImageField(upload_to='article_headers/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', '-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[self.pk])


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(null=False, auto_now_add=True)
    updated_on = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.article.title}"

    class Meta:
        ordering = ["created_on"]