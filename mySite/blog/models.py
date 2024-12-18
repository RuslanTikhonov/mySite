from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField("Название статьи", max_length=100, unique= True)
    text = models.TextField("Основной текст статьи")
    date = models.DateTimeField("Дата", default=timezone.now)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    views = models.IntegerField("Просмотры", default=1)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"