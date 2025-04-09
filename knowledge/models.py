from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Knowledge(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='knowledges', verbose_name="Категория")

    class Meta:
        verbose_name = "Знание"
        verbose_name_plural = "Знания"

    def __str__(self):
        return self.title