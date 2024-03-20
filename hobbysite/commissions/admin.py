from django.contrib import admin

from .models import Commission, Comment


class CommentInline(admin.StackedInline):
    model = Comment


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [CommentInline]

    search_fields = ['title']
    list_display = ['title', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['entry', 'created_on', 'updated_on']


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)