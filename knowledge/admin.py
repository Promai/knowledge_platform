from django.contrib import admin
from .models import Knowledge, Category

class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')  # Отображаем заголовок и категорию в списке
    list_filter = ('category',)  # Добавляем фильтр по категориям
    search_fields = ('title', 'content')  # Добавляем поиск по заголовку и содержанию

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') # Отображаем название и описание в списке
    search_fields = ('name', 'description') # Добавляем поиск по названию и описанию

admin.site.register(Knowledge, KnowledgeAdmin)
admin.site.register(Category, CategoryAdmin)