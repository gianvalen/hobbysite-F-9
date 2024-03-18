from django.contrib import admin
from .models import Article, ArticleCategory


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'updated_on')
    list_filter = ('created_on', 'updated_on')
    search_fields = ('title',)
    date_hierarchy = 'created_on'


admin.site.register(ArticleCategory, ArticleCategoryAdmin)