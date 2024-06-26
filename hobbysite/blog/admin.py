from django.contrib import admin
from .models import ArticleCategory, Article, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class ArticleInLine(admin.TabularInline):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInLine]


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [CommentInLine]
    search_fields = ["title",]
    list_display = ["title", "created_on"]
    list_filter = [ "created_on","updated_on",]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)