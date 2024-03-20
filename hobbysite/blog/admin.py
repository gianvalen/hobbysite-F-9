from django.contrib import admin
from .models import Article, ArticleCategory


class ArticleInLine(admin.TabularInline):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInLine]


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['title', 'created_on', 'updated_on'] 
    list_filter = ['created_on', 'updated_on'] 
    search_fields = ['title']

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)