from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='photos/', verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    count_of_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f"{self.title}: {self.content}./{self.created_at}"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title', 'created_at']
        permissions = [
            ('can_edit_articles', 'Can edit articles')
        ]
