from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_on', 'updated_on')
    list_filter = ('created_by',)
    search_fields = ['name']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on', 'category')
    list_filter = ('status', 'category',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
